===================
DTL Reference Guide
===================

.. contents:: Table of Contents


Introduction
===================

The Data Transformation Langauge (DTL) has been created as a means to allow developers to clearly describe transformations that should be performed on sets of data in order to create new datasets. 

Core Concepts
-------------

DTL allows developers to describe a data transform. A DTL processor applies the transform to a stream of data. For each entity in the stream the same transform is applied. The result of processing is a stream of new entities.  

A DTL transform describes how to construct a new entity. It can assume that it is provided a 'source' entity from which it can use property values. A transform can also perform queries that range across data in the datahub. These queries must start from the source entity.

DTL consists of 'functions' that can pick and transform data and 'hops' that can traverse the data in the datahub. In combination these offer a powerful way to construct new data entities from existing data. DTL functions are composable and thus allowing complex computation to be expressed.

Syntax
------

DTL uses a JSON syntax to describe the transforms to perform. In general DTL uses functions over keywords and as such there are just a few terms that are baked into the language. 

An example using the 'add' transform:

  ["add", "name", "_S.firstname"]

And composing functions:

  ["add", "name", ["concat", ["_S.firstname", " ", "_S.lastname"]]]

Input Streams
-------------

For a DTL processor to produce new entities it must be supplied a stream of source entities. DTL can only be applied to entities being sourced from a datahub dataset. When defining a DTL transform it is possible to process entities from many streams.

A DTL script must specify which datasets should be used as a source. This can be a list of datasets.

::

  {
    "datasets": ["people"]  
  }

  
Annotated Example
===================

Lets say that we have two datasets ``person`` and ``orders``, and that
we want to transform the *persons* by joining in their *orders* and
apply a few other transform functions. In this section you'll find a
complete DTL document that takes entities from the ``person`` dataset,
joins them with entities from the ``orders`` dataset and creates new
entities from them.

Given the following *source entity* (from the ``person`` dataset):

::

    {
      "_id": "1",
      "name": "John Smith",
      "age": 25
    }

We then want to transform it into the following *target entity*:

::

    {
      "_id": "1",
      "type": "customer",
      "name": "JOHN SMITH",
      "orders": [
        {"_id": 100, "amount": 320 },
        {"_id": 200, "amount": 500 }
      ],
      "order_count": 2
    }

Using the DTL document below we can transform the source entity into
the target entity:

::

    {
        "dataset": "person",
        "transforms": {
            "default": [
                ["copy", "_id"],
                ["add", "type", "customer"],
                ["add", "name", ["upper", "_S.name"]],
                ["add", "orders",
                  ["sorted", "_.amount", ["apply", "order", ["hops", {
                    "datasets": ["orders o"],
                    "where": [
                      ["eq", "_S._id", "o.cust_id"]
                    ]
                }]]]],
                ["add", "order_count", ["count", "_T.orders"]],
                ["filter", ["gt", "_T.order_count", 10]]
            ],
            "order": [
                ["copy", "_id"],
                ["add", "amount", "_S.amount"]
            ]
        }
    }

Explanation:

1. | The DTL will read and transform source entities from the ``person``
     dataset.

2. | There are two named ``transforms`` specified in the DTL document:
     ``default`` and ``order``. The ``default`` named transform is
     mandatory and is the one that is applied to the entities in the
     ``person`` dataset.

3. | ``["copy", "_id"]`` copies the ``_id`` property from the source
     entity to the target entity.

4. | ``["add", "type", "customer"]`` adds the ``type`` property to the target
     entity with the literal value ``"customer"``.

5. | ``["add", "name", ["upper", "_S.name"]]`` add the ``name``
     property to the target entity by uppercasing the name in the source
     entity.

   ::
   
       ["add", "orders",
         ["sorted", "_.amount", ["apply", "order", ["hops", {
           "datasets": ["orders o"],
           "where": [
             ["eq", "_S._id", "o.cust_id"]
           ]
       }]]]]

6. | The expression above adds the ``orders`` property to the target
     entity. It does this by joining the source entity's ``_id``
     property with the ``cust_id`` property of entities in the
     ``orders`` dataset. The join is done by the ``hops`` function,
     which takes a list of ``datasets``, assigns aliases to them, which
     then get exposed as variables that you can use in expressions in
     the ``where`` clause. The result of the ``hops`` is a list of
     order entities:

   ::

    [{
      "_id": 200,
      "amount": 500
      "order_lines": [...],
      "cust_id": "1"
    },
    {
      "_id": 100,
      "amount": 320,
      "order_lines": [...],
      "cust_id": "1"
    }]

   | The ``order`` transform is then applied using the ``apply`` function.
     The result of this is a list of orders with two properties: ``_id``
     and ``amount``:

   ::

    [{
      "_id": 200,
      "amount": 500
    },
    {
      "_id": 100,
      "amount": 320
    }]

   | The order entites are then ``sorted`` by their ``amount``
     property before being assigned to the ``orders`` property on the
     target entity:

   ::

    [{
      "_id": 100,
      "amount": 320
    },
    {
      "_id": 200,
      "amount": 500
    }]

7. | ``["add", "order_count", ["count", "_T.orders"]]`` adds the
     ``order_count`` property to the target entity. Note that the value
     is the number of order entities in the target entity's ``orders``
     property. Note that we can access properties on the target entity
     once we've added them.

8. | Stop processing if the ``["filter", ["gt", "_T.order_count", 10]]``
     evaluates to true. If the filter is false the target entity is not
     emitted / created.

Things to note:

- Transform functions are applied in the order given. The order is
  significant, and one transform can use target entity properties
  created by earlier transform function.
  
- The filter function can be used to stop transformation of individual
  entities, effectively filtering them out of the output stream.


Variables
=========

There are three variables in the Data Transformation Language. These
are ``_S``, ``_T`` and ``_``. They refer to the source entity, target
entity and the current value respectively. ``_S`` and ``_T`` appear in
pairs inside each applied transform. ``_`` is used to refer to the
current value in functional expressions.

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Variable
     - Description
     - Examples
       
   * - ``_S``
     - Refers to the source entity. This is the entity on which the
       DTL transform operate. Note that with the ``apply`` function
       you can apply nested transforms, where each of the values
       given to ``apply`` is made a source entity for that nested
       transform.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater than 26.

   * - ``_T``
     - Refers to the target entity. This is the entity that is the
       primary target entity of transforming the source entity. Note
       that the ``create`` transform can be used to emit entities
       in addition to just the target entity.
     - | ``["length", "_T.description", 100]``
       |
       | The target entity's ``description`` field must have a length of
         more than 100 characters.

   * - ``_``
     - Refers to the current entity. This variable is only available
       inside a few functions that take a function expression as an
       argument. Examples of such functions are ``filter``, ``sorted``
       ``min``, ``max``, and ``coalesce``.
     - | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Filters out the order entities that have an amount of less than
         100, i.e. the filter function returns only the orders that have
         an amount of greater than 100. As you can see the ``_`` variable
         refers to the individual order entities, one at a time.


Path Expressions and Hops
=========================

There are three ways that one can access properties on entities:

1. **Property path strings**: ``"_S.order.amount"``, which will start
   from the ``_S`` variable (the source entity), and then traverse to
   the ``order`` property and then to the ``amount`` property. The end
   result is a list of amounts. Note that property path strings
   function can only access property on the entity it operates on,
   including nested entities.

2. **The "path" function**: ``["path", "foo.bar", ["sorted",
   "_.amount", "_S.foos"]]``, which will first evaluate the rightmost
   expression. Then it will traverse the path given in the first
   argument for each of them and return the end result. Note that the
   ``path`` function can only access property on the entity it
   operates on, including nested entities.

3. **The "hops" function**:

   ::
      
       ["hops", {
           "datasets": ["orders o"],
           "where": [
             ["eq", "_S._id", "o.cust_id"]
           ]
       }]

   The ``hops`` function can be used to perform joins across two or
   more datasets, so if you want to navigate beyond the current entity
   use ``hops``.


Notation
==========

Argument types
--------------

In the function tables below you'll see argument lists like this
``CONDITION(boolean-expression{1}), THEN(transforms{1}), ELSE(transforms{0|1})``.

``CONDITION``, ``THEN`` and ``ELSE`` are logical names that have no
meaning other than so that we can refer to them by name. Inside the
parenthesis is the type of argument, i.e. ``boolean-expression`` and
``transforms``. The numbers inside the curly braces is the cardinality
of the argument. Here are some cardinalites that you'll come across:

#. ``{0|1}``: zero or one, i.e. optional.

#. ``{1}``: exactly one

#. ``{2}``: two

#. ``{>=0}``: zero or more

#. ``{>=1}``: one or more

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Argument type
     - Description
     - Examples
       
   * - ``boolean-expression``
     - | Refers to an expression that returns a single boolean value.
     - | ``["eq", "_S.type", "person"]``
       
   * - ``value-expression``
     - | Refers to an expression that returns null, a single value or a
         list of values.
     - | ``["values", 1, 2, 3]``
       
   * - ``function-expression``
     - | Refers to a value expression argument that operates on a list
         of values, and exposes the ``_`` current value variable for
         each of them.
     - | ``["upper", "_.name"]``
       
   * - ``string``
     - | Refers to a constant string literal.
     - | ``"Jupiter"``
       
   * - ``wildcard-string``
     - | Refers to a constant string pattern literal that can include
         the ``*`` and ``?`` wildcard characters.
     - | ``"alpha_*"`` or ``"person"``

   * - ``wildcard-string-list``
     - | Same as ``wildcard-string``, but a list of them.
     - | ``["alpha_*", "beta_*"]``
       
   * - ``transforms``
     - | A single transform function, or a list of them.
     - | ``[["add", "type", "person"],``
       |  ``["copy", ["name", "age"]]]]``
       |
       | or
       |
       | ``["add", "type", "person"]``


Transforms
==========

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``if``
     - | *Arguments:*
       |   CONDITION(boolean-expression{1}),
       |   THEN(transforms{1}),
       |   ELSE(transforms{0|1})
       |
       | If CONDITION evaluates to *true* then apply the transforms in THEN.
         If CONDITION evaluates to *false* then apply the transforms in ELSE.
         Note that THEN and ELSE can contain empty lists of transforms.
     - | ``["if", ["eq", "_S.type", "person"],``
       |      ``[["add", "type", "person"],``
       |       ``["copy", ["name", "age"]]]]``
       |
       | If the source entity's ``type`` field is equal ``person`` then apply
         the ``add`` and ``copy`` transforms. There is no else clause given,
         which is effectively the same as an empty list with no transforms.
       |
       | ``["if", ["gt", "_S.age", 18],``
       |      ``["add", "type", "adult"],``
       |      ``["add", "type", "child"]]``
       |
       | If the source entity's ``age`` is greater than 18 then add ``type``
         field with value ``adult``, if not add ``child``.
       
   * - ``filter``
     - | *Arguments:*
       |   FILTER(boolean-expression{0|1})
       |
       | If the evaluation of the FILTER expresion returns false, then stop
         applying transformations. If the processing is stopped then *no*
         target entity is emitted for the source entity. Note that any entities
         already emitted by ``create`` will not be stopped. If the FILTER argument
         is not given then the filter evaluates to false, so it effectively stops
         the processing of the source entity.
     - | ``["filter", ["gt", "_S.age", 42]]``
       |
       | Continue processing only if the source entity's age is greater than 42.
       |
       | ``["filter", ["eq", "_S.type", "person]]``
       |
       | Continue processing only if the source entity's type is ``person``.
       |
       | ``["filter"]``
       |
       | Stop processing.
       
   * - ``add``
     - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field to the target entity with the values returned
         by evaluating the VALUES expression.
     - | ``["add", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity.
       |
       | ``["add", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity. The value is
         the uppercased version of the source entity's ``name`` property.
       
   * - ``default``
     - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field to the target entity with the values returned
         by evaluating the VALUES expression, unless the property already exists.
         ``default`` behaves exactly like ``add``, except that it does not add
         the property if the property already exists on the target entity. If
         the property exists it does nothing.
     - | ``["default", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity, if
         the propery does not exists.
       |
       | ``["default", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity, if
         the propery does not exists.. The value is
         the uppercased version of the source entity's ``name`` property.
       
   * - ``remove``
     - | *Arguments:*
       |   PROPERTY(wildcard-string{1})
       |
       | Removes the PROPERTY field from the target entity. The PROPERTY can
         be pattern with ``*`` and ``?`` characters in it. The pattern must match
         the full property names.
     - | ``["remove", "age"]``
       |
       | Removes the ``age`` property from the target entity.
       |
       | ``["remove", "temp_*"]``
       |
       | Removes all properties matching the ``temp_*`` wildcard pattern from
         the target entity.
       
   * - ``copy``
     - | *Arguments:*
       |   INCLUDE_PROPERTIES(wildcard-string-list{1})
       |   EXCLUDE_PROPERTIES(wildcard-string-list{1})
       |
       | Copies properties in INCLUDE_PROPERTIES from the source entity to the
         target entity. Any properties matching any ofthe EXCLUDE_PROPERTIES
         patterns are not included. INCLUDE_PROPERTIES and EXCLUDE_PROPERTIES
         can be a single string or a list of strings, where the strings are
         patterns. ``*`` and ``?`` are valid pattern characters.
     - | ``["copy", "age"]``
       |
       | Copies the ``age`` property from the source entity to the target entity.
       |
       | ``["copy", "a*", "ab*"]``
       |
       | Copies all properties starting with ``a`` from the source entity to the
         target entity, but not those starting with ``ab``.
       |
       | ``["copy", ["a*", "b*"], ["ab*", "ba*"]]``
       |
       | Copies all properties starting with ``a`` or ``b`` from the source entity
         to the target entity, but not those starting with ``ab`` or ``ba``.
       
   * - ``rename``
     - | *Arguments:*
       |   PROPERTY1(string{1})
       |   PROPERTY2(string{1})
       |
       | Copies the PROPERTY1 field from the source entity to the PROPERTY2 field
         on the target entity. This is effectively a way to copy and rename
         properties from the source entity to the target entity. No wildcard
         patterns are supported.
     - | ``["rename", "age", "current_age"]``
       |
       | Copies the ``age`` field from the source entity and adds it as
         ``current_age`` on the target entity.
       
   * - ``merge``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity, unless the property already exists. This means that
         properties from earlier value entities win over later ones.
     - | ``["merge", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target,
         unless the property exists already.
       |
       | ``["merge", ["values", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=1`` and ``b=3`` to the target entity. Note that
         ``a=2`` is not added because the ``a`` property already exists.
       
   * - ``merge-union``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity. If the property already exists on the target entity, add
         the new values to the existing list of values.
     - | ``["merge", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
         Merge the property values if the property already exists.
       |
       | ``["merge", ["values", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=[1, 2]`` and ``b=[3]`` to the target entity.
       
   * - ``create``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES emit them as new entities to the DTLs output
         pipeline. Note that these new entites *must* have an ``_id`` property.
     - | ``["create", "_S.orders"]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities.
       |
       | ``["create", ["apply", "order", "_S.orders"]]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities,
         but apply the ``order`` transform to them first.
       

Expression language
===================


Logical
---------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``and``
     - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns true only if all arguments evaluate to true.
     - | ``["and",``
       |    ``["gt", "_S.age", 26],``
       |    ``["eq", "_S.gender", "male"]]``
       |
       | Age must be greater than 26 and the gender must be male.

   * - ``or``
     - | *Arguments:* boolean-expression{>=0}
       |
       | Takes at least one boolean expression argument.
         Returns true if any of the arguments evaluate to true.
     - | ``["or",``
       |   ``["eq", "_S.category", "A"],``
       |   ``["eq", "_S.category", "B"]]``
       |
       | The category field must contain "A" or "B".
       
   * - ``not``
     - | *Arguments:* boolean-expression{1}
       |
       | Takes a single boolean expression argument.
         Returns the inverse boolean value.
     - | ``["not",``
       |   ``["or",``
       |      ``["eq", "_S.category", "A"],``
       |      ``["eq", "_S.category", "B"]]]``
       |
       | The category must contain neither "A" nor "B".


A *boolean-expression* is any function that returns a boolean value.

Comparisons
--------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``eq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns *true* if the two
         arguments given are equal.
     - | ``["eq", "_S.age", 42]``
       |
       | The source entity's age field must have the value 42.
       
   * - ``neq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns *false* if the two
         arguments given are equal.
     - | ``["neq", "_S.age", 42]``
       |
       | The source entity's age field must *not* have the value 42.
       
   * - ``gt``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than the second argument.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than 42.
       
   * - ``gte``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than or equal the second argument.
     - | ``["gte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than or equal 42.
       
   * - ``lt``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         the second argument.
     - | ``["lt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than 42.
       
   * - ``lte``
     - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         or equal the second argument.
     - | ``["lte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than or equal 42.
       
   * - ``empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is 0.
     - | ``["empty", "_S.hobbies"]``
       |
       | Returns true of the source entity's ``hobbies`` field is
         empty (has no values).

       
   * - ``not-empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is greater than 0.
     - | ``["not-empty", "_S.hobbies"]``
       |
       | Returns true of the source entity's ``hobbies`` field is not
         empty (has one or more values).


Conditionals
---------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``if``
     - | *Arguments:*
       |   CONDITION(boolean-expression{1}),
       |   THEN(value-expression{1}),
       |   ELSE(value-expression{0\|1})
       |
       | If CONDITION evaluates to *true* then return the result of
         evaluating THEN. If CONDITION evaluates to *false* then return
         the result of evaluating ELSE.
     - | ``["if", ["gt", "_S.age", 42], 1, 2]``
       |
       | Return 1 if the source entity's ``age`` field is greater
         than 43, if not 2 is returned.

   * - ``coalesce``
     - | *Arguments:*
       |   FUNCTION(function-expression{0|1}),
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES that makes the FUNCTION expression
         return a non-null value. The FUNCTION expression argument is optional,
         so if it is not given the first non-null value in VALUES is returned.
     - | ``["coalesce", "_S.tags"]``
       |
       | Returns the first value in the source entity's ``tags``
         field that is not null.
       |
       | ``["coalesce",``
       |     ``["gt", "_.expenses", 1000], "_S.hobbies"]``
       |
       | Returns the first hobby that has expenses greater than 1000.


Nested transformations
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``apply``
     - | *Arguments:*
       |   TRANSFORM_ID(string{1}),
       |   VALUES(value-expression{1})
       |
       | Applies the TRANSFORM_ID transform on the entities in VALUES.
         TRANSFORM_ID must be the id of a transform in the current DTL
         specification.
     - | ``["apply", "order", "_S.orders"]``
       |
       | This will transform the order entities in the source entity's
         ``orders`` field using the ``order`` transform. The output is
         the transformed order entities.


Paths
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``path``
     - | *Arguments:*
       |   PROPERTY_PATH(string{1}),
       |   VALUES(value-expression{1})
       |
       | Traverses the PROPERTY_PATH path for each of the entities in
         VALUES. The result is a list of all the values at the end of
         the traversal. PROPERTY_PATH paths are separated by '``.``'
         (periods). Only properties on the entity can be traversed. If
         you want to traverse to other entities use ``hops`` instead.
     - | ``["path", "age", ["values", {"age": 23}, {"age": 24}]]``
       |
       | Traverses the ``age`` field of the VALUES entities.
         Returns ``[23, 24]``.
       |
       | ``["path", "order_lines.item_name", "_S.orders"]``
       |
       | This will travese from the source entity's orders to the
         order lines and their item names. The output is a list of
         product item names.


Hops
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``hops``
     - | *Arguments:*
       |   HOPS_SPEC(dict{1})
       |
       | ...TODO...
     - |


Strings
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``upper``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the uppercase version of its input strings.
         Non-string values are ignored.
     - | ``["upper", ["values", "a", "b", "c"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["upper", "_S.name"]``
       |
       | Returns an uppercased version of the source entity's name.
       
   * - ``lower``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the lowercase version of its input strings.
         Non-string values are ignored.
     - | ``["lower", ["values", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["lower", "_S.name"]``
       |
       | Returns a lowercased version of the source entity's name.
       
   * - ``length``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the length (number of characters) of its input strings.
         Non-string values are ignored.
     - | ``["length", ["values", "", "a", "bb", "ccc"]]``
       |
       | Returns ``[0, 1, 2, 3]``.
       |
       | ``["length", "_S.name"]``
       |
       | Returns the length of the source entity's name.
       
   * - ``concat``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns a concatenated string of its input strings.
         Non-string values are ignored.
     - | ``["concat", ["values", "a", "b", "c"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["concat", "_S.tags"]``
       |
       | Returns a concatenated version of the source entity's tags.


Values / collections
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``first``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["first", ["values", "a", "b", "c"]]``
       |
       | Returns ``"A"``.
       |
       | ``["first", "_S.tags"]``
       |
       | Returns the first tag in the source entity's ``tags`` field.
       
   * - ``values``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Constructs a list of the values in VALUES.
     - | ``["values"]``
       |
       | Returns ``[]``.
       |
       | ``["values", "a", "b", "c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["values", "a", ["values", "b"], "c"]``
       |
       | Returns ``["a", ["b"], "c"]``.
       
   * - ``flatten``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Flattens its input values in VALUES. Note that it does *not* do so
         recursively. Constructs a new list.
     - | ``["flatten", ["values", 1, 2], ["values", 3, 4]]``
       |
       | Returns ``[1, 2, 3, 4]``.
       |
       | ``["flatten", ["values", 1, 2], ["values", 3, ["values", 4]]]``
       |
       | Returns ``[1, 2, 3, [4]]``.
       |
       | ``["flatten", ["values", 1, 2], ["values", 3, ["values", 4]], 5]``
       |
       | Returns ``[1, 2, 3, [4], 5]``.
       
   * - ``filter``
     - | *Arguments:*
       |   FILTER(boolean-expression(1}
       |   VALUES(value-expression{1})
       |
       | Filters out the the values in VALUES for which the FILTER expression
         does *not* evaluate to *true*.
     - | ``["filter", ["gt", "_.age", 42],``
       |     ``["values", {"age": 30}, {"age": 50}, {"age": 40}]]``
       |
       | Returns ``[{"age": 50}]``.
       |
       | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the order entities that have an amount of more than 100.
       
   * - ``min``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns the minimum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the minimal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.
     - | ``["min", ["values", 4, 2, 5, 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the lowest amount.
       
   * - ``max``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns the maximum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the maximal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.
     - | ``["max", ["values", 4, 2, 5, 3]]``
       |
       | Returns ``5``.
       |
       | ``["max", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the highest amount.

   * - ``count``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the number of elements in VALUES.
     - | ``["count", ["values", 2, 4, 6]]``
       |
       | Returns ``3``.
       |
       | ``["count", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the the number of order entities that have an amount of
         more than 100.
       
   * - ``distinct``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns a list of distinct values in VALUES, i.e. it returns a list
         where duplicates have been removed from VALUES. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used to check for duplicates. Note that even though FUNCTION is
         given it is the value in VALUES that is returned.
     - | ``["distinct", ["values", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[4, 2, 5, 3]``.
       |
       | ``["distinct", "_S.tags"]]``
       |
       | Returns a deduplicated list of tags.
       |
       | ``["distinct", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns a list of order lines, but only one per unique EAN, i.e. product
         number.
       
   * - ``sorted``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns a list of sorted values in VALUES. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that.
     - | ``["sorted", ["values", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[2, 3, 4, 4, 5]``.
       |
       | ``["sorted", ["values", {"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 20}, {"age": 30}, {"age": 50}]``.
       |
       | ``["sorted", "_S.tags"]]``
       |
       | Returns a sorted list of tags.
       
   * - ``map``
     - | *Arguments:*
       |   FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each value in VALUES apply the FUNCTION function and construct a new
         list of the return values.
     - | ``["map", ["lower", "_."], ["values", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["map", ["distinct", "_."],``
       |   ``["values", ["values", "A", "A"], ["values", "B", "C"]]]``
       |
       | Returns ``[["A"], ["B", "C"]]``.


Sets
----------------------

.. list-table:: 
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples
       
   * - ``union``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the union of the two sets SET1 and SET2, i.e. the elements that
         are either in SET1 or in SET2. The two arguments do not have to be real
         sets, but will be coerced into sets before applying the union operator.
     - | ``["union", ["values", "A", "B"], ["values", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union", "A", ["values", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       
   * - ``intersection``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the intersection of the two sets SET1 and SET2, i.e. the elements
         that are in both SET1 and SET2. The two arguments do not have to be real sets,
         but will be coerced into sets before applying the intersection operator.
     - | ``["intersection", ["values", "A", "B"], ["values", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "B", ["values", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "A", ["values", "B", "C"]]``
       |
       | Returns ``[]``.
       
   * - ``difference``
     - | *Arguments:*
       |   SET1(value-expression{1})
       |   SET2(value-expression{1})
       |
       | Returns the difference of the two sets SET1 and SET2, i.e. the elements
         that are in SET1, but not in SET2. The two arguments do not have to be real
         sets, but will be coerced into sets before applying the difference operator.
     - | ``["difference", ["values", "A", "B"], ["values", "B"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference", "A", ["values", "B", "C"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference",``
       |   ``["values", "A", "B", "C", "D"], ["values", "A", "B", "E"]]``
       |
       | Returns ``["C", "D"]``.
