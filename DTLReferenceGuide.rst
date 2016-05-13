.. _DTLReferenceGuide:

===================
DTL Reference Guide
===================

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

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

  ["add", "name", ["concat", ["list", "_S.firstname", " ", "_S.lastname"]]]

Input Streams
-------------

For a DTL processor to produce new entities it must be supplied a stream of source entities. DTL can only be applied to entities being sourced from a datahub dataset. When defining a DTL transform it is possible to process entities from many streams.

A DTL script must specify which datasets should be used as a source. This can be a list of datasets.

::

  {
    "datasets": ["people"]
  }


Annotated Example
=================

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
        "rules": {
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

2. | There are two named ``rules`` specified in the DTL document:
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

- When the DTL of a pipe is modified, the pipe's "last-seen" value must be
  cleared in order to reprocess already seen entities with the new DTL.
  This can be done by setting the "last-seen" value to an empty string with the
  `update-last-seen <./api.html#api-reference-pump-update-last-seen>`_ operation in the SESAM API.


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
       you can apply nested transform rules, where each of the values
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

1. **Property path strings**: ``"_S.orders.amount"``, which will start
   from the given variable, in this case the source entity ``_S``, and
   then traverse to the ``orders`` property and then to the ``amount``
   property. The end result is a list of amounts. Note that property
   path strings function can only access property on the entity it
   operates on, including nested entities.

   One can also refer to the content of the variables themselves,
   e.g. ``_S.`` would refer to the source entity itself (note the dot
   after the variable name). ``_T.`` refers to the target entity, and
   ``_.`` refers to the current value.

2. **The "path" function**: ``["path", "placed_by", ["sorted",
   "_.amount", "_S.orders"]]``, which will first evaluate the
   rightmost expression. Then it will traverse the path given in the
   first argument for each of them and return the end result. The
   first argument is an expression that resolve to either a single
   string or a list of strings. Note that the ``path`` function can
   only access property on the dictionary/entity it operates on,
   including nested entities.

.. _hops_function:

3. **The "hops" function**:

   ::

       ["hops", {
           "datasets": ["orders o"],
           "where": [
             ["eq", "_S._id", "o.cust_id"],
             ["eq", "o.type", "BILLING"]
           ]
       }]

   The ``hops`` function can be used to perform joins across two or
   more datasets, so if you want to navigate beyond the current entity
   use ``hops``. This particular example will join the source entity
   with entities from the ``orders`` dataset using the ``["eq",
   "_S._id", "o.cust_id"]`` join expression and then filter the orders
   by ``["eq", "o.type", "BILLING"]``. Note that only ``eq`` functions
   will be treated as join expressions. All other function are treated
   as filter expressions. For an ``eq`` to be a join expression it
   will have to refer to variables from two different datasets.


Dependency Tracking
===================

TODO: Explain how this works.


Argument types
==============

In the function tables below you'll see argument lists like this
``CONDITION(boolean-expression{1}), THEN(transforms{1}), ELSE(transforms{0|1})``.

``CONDITION``, ``THEN`` and ``ELSE`` are logical names that have no
meaning other than so that we can refer to them by name. Inside the
parenthesis is the type of argument, i.e. ``boolean-expression`` and
``transforms``. The numbers inside the curly braces is the cardinality
of the argument. Here are some cardinalites that you'll come across:

#. ``{0|1}``: zero or one, i.e. optional.

#. ``{1}``: exactly one

#. ``{2}``: exactly two

#. ``{>=0}``: zero or more

#. ``{>=1}``: one or more

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Argument type
     - Description
     - Examples

   * - ``boolean-expression``
     - | Refers to an expression that returns a single "boolean" value. Note that
         ``false``, ``null`` and ``[]`` evaluate to false. All other values
         evaluate to true.
     - | ``["eq", "_S.type", "person"]``

   * - ``value-expression``
     - | Refers to an expression that returns null, a single value or a
         list of values.
     - | ``["list", 1, 2, 3]``

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


.. _merge_union_function:
.. _merge_function:

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

   * - ``comment``
     - | *Arguments:*
       |   COMMENTS(value-expression{>=0})
       |
       | A transform that does nothing except hold comments. Useful for
         documenting the transforms, or just disabling transforms inside. Any
         expressions inside the comment will not be evaluated.
     - | ``["comment", "This is a comment"]``
       |
       | A single line comment.
       |
       | ``["comment",``
       |      ``"First line",``
       |      ``"Second line",``
       |      ``"Third line"]``
       |
       | A comment that spans multiple lines.

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
       | ``["merge", ["list", {"a": 1}, {"a": 2, "b": 3}]]``
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
     - | ``["merge-union", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
         Merge the property values if the property already exists.
       |
       | ``["merge-union", ["list", {"a": 1}, {"a": 2, "b": 3}]]``
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
-------

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
     - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns true if any of the arguments evaluate to true.
     - | ``["or",``
       |   ``["eq", "_S.category", "A"],``
       |   ``["eq", "_S.category", "B"]]``
       |
       | The category field must contain "A" or "B".

   * - ``not``
     - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns the inverse boolean value. It behaves like ``and``,
         but returns the inverse.
     - | ``["not",``
       |   ``["or",``
       |      ``["eq", "_S.category", "A"],``
       |      ``["eq", "_S.category", "B"]]]``
       |
       | The category must contain neither "A" nor "B".

   * - ``all``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | If FUNCTION is specified, then the function is evaluated for each value in
         VALUES. Returns true if all arguments evaluate to true. 
     - | ``["all",``
       |    ``["list", 1, 2, 3]]``
       |
       | Returns true because all arguments evaluate to true.
       |
       | ``["all",``
       |    ``["gt", 2, "_."],``
       |    ``["list", 4, 5, 6]]``
       |
       | Returns true because all arguments are greater than 2.
       |
       | ``["all",``
       |    ``["lt", 2, "_."],``
       |    ``["list", 1, 3, 5]]``
       |
       | Returns false because not all arguments are less than 2.

   * - ``any``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | If FUNCTION is specified, then the function is evaluated for each value in
         VALUES. Returns true if at least one argument evaluates to true. 
     - | ``["any",``
       |    ``["list", 1, 2, 3]]``
       |
       | Returns true because all arguments evaluate to true.
       |
       | ``["any",``
       |    ``["gt", 5, "_."]]``
       |    ``["list", 4, 6, 8]]``
       |
       | Returns true because two of the arguments are greater than 5.
       |
       | ``["any",``
       |    ``["lt", 2, "_."],``
       |    ``["list", 6, 7, 8]]``
       |
       | Returns false because none of the arguments are less than 2.


Comparisons
-----------

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
------------

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


Data Types
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``uri``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to URIs. Only strings in VALUES will be
         cast to URIs. Note that *no* URI escaping is done on the strings.
     - | ``["uri", "http://www.bouvet.no/"]``
       |
       | Returns one URI.
       |
       | ``["uri", ["list", "http://www.bouvet.no/", ""http://www.sesam.io/", 12345]]``
       |
       | Returns a list of two URIs. The number is silently ignored because it is not a string.

   * - ``is-uri``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a URI literal or if it is a list, that the first element
       | in the list is a URI
       |
     - | ``["is-uri", ["uri", "foo:bar"]]``
       |
       | Returns true.
       |
       | ``["is-uri", "foo:bar"]``
       |
       | Returns false.
       |
       | ``["is-uri", ["list", ["uri", "foo:bar"], 12345]]``
       |
       | Returns true
       |
       | ``["is-uri", ["list", 1, ["uri", "foo:bar"]]]``
       |
       | Returns false

   * - ``string``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to strings.
     - | ``["string", 1]``
       |
       | Returns one string: "1".
       |
       | ``["string", ["1", "~rhttp://www.bouvet.no/", 124.4, 12345]]``
       |
       | Returns a list of strings.

   * - ``is-string``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a string literal or if it is a list, that the first element
       | in the list is a string
       |
     - | ``["is-string", "foo:bar"]``
       |
       | Returns true.
       |
       | ``["is-string", 1]``
       |
       | Returns false.
       |
       | ``["is-string", ["list", "foo:bar", 12345]]``
       |
       | Returns true
       |
       | ``["is-string", ["list", 1, "foo:bar"]]``
       |
       | Returns false

   * - ``integer``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all input values to integers. If no default value expression is given, values that don't parse
       | as integers will be silently ignored. If not, the evaluated value from the default expression will be used
       | as a replacement value.
       |
     - | ``["integer", "1"]``
       |
       | Returns one integer: 1.
       |
       | ``["integer", ["list", "1", "~rhttp://www.bouvet.no/", 124.4, 12345]]``
       |
       | Returns a list of integers: [1, 124, 12345]. The URI value is ignored.
       |
       | ``["integer", ["integer", 0], ["list", "1", "~rhttp://www.bouvet.no/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, 0, 0, 12345]. The URI value and the string value are replaced with the
       | literal value 0
       |
       | ``["integer", ["string", "n/a"], ["list", "1", "~rhttp://www.bouvet.no/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "n/a", "n/a", 12345]. The URI value and the string value are replaced with the
       | literal value "n/a"
       |
       | ``["integer", ["string", "_."], ["list", "1", "~rhttp://www.bouvet.no/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "http://www.bouvet.no/", "10^2", 12345]. The URI value and the string float value
       | are replaced with the their respective string casts.

   * - ``is-integer``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is an integer literal or if it is a list, that the first element
       | in the list is an integer
       |
     - | ``["is-integer", 1]``
       |
       | Returns true.
       |
       | ``["is-integer", "1"]``
       |
       | Returns false.
       |
       | ``["is-integer", ["list", 1, "12345"]]``
       |
       | Returns true
       |
       | ``["is-integer", ["list", "1", 2]]``
       |
       | Returns false
       |
       | ``["is-integer", ["list", ["integer", "1"], 2]]``
       |
       | Returns true

   * - ``now``
     - | *Arguments:*
       |   NONE(value-expression{0})
       |
       | Returns the current time as a datetime value.
       |
     - | ``["now"]``
       |
       | Returns the current time as a datetime value, e.g. "~t2016-05-13T14:32:00.431Z".

   * - ``datetime``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all input values to datetime values. If no default value expression is given, values that don't parse
       | as datetime values will be silently ignored. If not, the evaluated value from the default expression will be used
       | as a replacement value.
       |
     - | ``["datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z".
       |
       | ``["datetime", 1438076760123450000]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z". Note that integer values are treated as nanoseconds since epoch.
       |
       | ``["datetime", ["list", ["now"], ["now"], "hello"]]``
       |
       | Returns a list of two datetime values which both are the current time: [1, 124, 12345]. The "hello" string is ignored.
       |
       | ``["datetime", ["now"], "hello"]``
       |
       | Returns the current time as a datetime value, e.g. "~t2016-05-13T14:32:00.431Z". Note that this was created by the function argument.

   * - ``is-datetime``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a datetime value or if it is a list, that the first element
       | in the list is a datetime value.
       |
     - | ``["is-datetime", ["now"]]``
       |
       | Returns true.
       |
       | ``["is-datetime", ["datetime", "2015-07-28T09:46:00.12345Z"]]``
       |
       | Returns true.
       |
       | ``["is-datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns false
       |
       | ``["is-datetime", ["list", "1", 2]]``
       |
       | Returns false

   * - ``boolean``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all input values to booleans. If no default value expression is given, values that don't parse
       | as boolean values will be silently ignored. If not, the evaluated value from the default expression will be used
       | as a replacement value. String literals are case insensitive, and the supported values are "true" and "false".
       | null values are evaluated as false.
       |
     - | ``["boolean", "false"]``
       |
       | Returns one boolean: false.
       |
       | ``["boolean", ["list", "true", "~rhttp://www.bouvet.no/", "True", false, 1234]]``
       |
       | Returns a list of booleans: [true, true, false]. The URI and integer values are ignored.
       |
       | ``["boolean", ["boolean", false], ["list", "true", "~rhttp://www.bouvet.no/", "124.4", "FALSE"]]``
       |
       | Returns a list of booleans: [true, false, false, false]. The URI value and the string value are replaced with the
       | literal value: false
       |
       | ``["boolean", ["string", "n/a"], ["list", "true", "~rhttp://www.bouvet.no/", "124.4"]]``
       |
       | Returns a list of booleans: [true, "n/a", "n/a"]. The URI value and the string value are replaced with the
       | literal value "n/a"
       |
       | ``["boolean", ["string", "_."], ["list", "true", "~rhttp://www.bouvet.no/", "False"]]``
       |
       | Returns a list of booleans: [true, "http://www.bouvet.no/", false]. The URI value is replaced with its string cast.

   * - ``is-boolean``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a boolean literal or if it is a list, that the first element
       | in the list is a boolean
       |
     - | ``["is-boolean", false]``
       |
       | Returns true.
       |
       | ``["is-boolean", "True"]``
       |
       | Returns false.
       |
       | ``["is-boolean", ["list", true, "12345"]]``
       |
       | Returns true
       |
       | ``["is-boolean", ["list", "True", 2]]``
       |
       | Returns false
       |
       | ``["is-boolean", ["list", ["boolean", "FALSE"], 1234]]``
       |
       | Returns true

   * - ``float``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all input values to floats. If no default value expression is given, values that don't parse
       | as float values will be silently ignored. If not, the evaluated value from the default expression will be used
       | as a replacement value.
       |
     - | ``["float", "1.0"]``
       |
       | Returns one float: 1.0
       |
       | ``["float", ["list", "1.0", "~rhttp://www.bouvet.no/", 2.2, "3.3", "one"]]``
       |
       | Returns a list of floats: [1.0, 2.2, 3.3]. The URI and float string value are ignored.
       |
       | ``["float", ["boolean", false], ["list", "1.0", "~rhttp://www.bouvet.no/", "124.4", "FALSE"]]``
       |
       | Returns a list of floats: [1.0, false, 124.4, false]. The URI value and the string value are replaced with the
       | literal value: false
       |
       | ``["float", ["string", "n/a"], ["list", "1.0", "~rhttp://www.bouvet.no/", "124.4"]]``
       |
       | Returns a list of floats: [1.0, "n/a", 124.4]. The URI value is replaced with the
       | literal value "n/a"
       |
       | ``["float", ["string", "_."], ["list", "1.0", "~rhttp://www.bouvet.no/", "2.5"]]``
       |
       | Returns a list of floats: [1.0, "http://www.bouvet.no/", 2.5]. The URI value is replaced with its string cast.

   * - ``is-float``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a float literal or if it is a list, that the first element
       | in the list is a float
       |
     - | ``["is-float", 1.0]``
       |
       | Returns true.
       |
       | ``["is-float", 1]``
       |
       | Returns false.
       |
       | ``["is-float", ["list", 1.0, "12345"]]``
       |
       | Returns true
       |
       | ``["is-float", ["list", "1.0", 2.0]]``
       |
       | Returns false
       |
       | ``["is-float", ["list", ["float", "-1.0"], 1234]]``
       |
       | Returns true

   * - ``decimal``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all input values to decimals (a fractional number with unlimited precision). If no default value
       | expression is given, values that don't parse as decimal values will be silently ignored. If not, the evaluated
       | value from the default expression will be used as a replacement value.
       |
     - | ``decimal`` has the exact same usage pattern as ``float``


   * - ``is-decimal``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a decimal literal or if it is a list, that the first element
       | in the list is a decimal
       |
     - | ``is-decimal`` has the exact same usage pattern as ``is-float``

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
       |   RULE_ID(string{1}),
       |   VALUES(value-expression{1})
       |
       | Applies the RULE_ID transform rule on the entities in VALUES.
         RULE_ID must be the id of a transform rule in the current DTL
         specification.
     - | ``["apply", "order", "_S.orders"]``
       |
       | This will transform the order entities in the source entity's
         ``orders`` field using the ``order`` transform rules. The output is
         the transformed order entities.


Paths
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``path``
     - | *Arguments:*
       |   PROPERTY_PATH(value-expression{1}),
       |   VALUES(value-expression{1})
       |
       | Traverses the PROPERTY_PATH path for each of the entities in
         VALUES. The result is a list of all the values at the end of
         the traversal. PROPERTY_PATH is an expression that should resolve
         to a string or a list of strings. Those strings are treated as
         literals, i.e. property names, so no variables can be used. Only
         properties on the entity can be traversed. If you want to traverse
         to other entities use the ``hops`` function instead.
     - | ``["path", "age", ["list", {"age": 23}, {"age": 24}]]``
       |
       | Traverses the ``age`` field of the VALUES entities.
         Returns ``[23, 24]``.
       |
       | ``["path", ["list", "order_lines", "item_name"], "_S.orders"]``
       |
       | This will traverse from the source entity's orders to the
         order lines and then return their item names. The output is a
         list of product item names.


Hops
----

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
       | The HOPS_SPEC is a dictionary that takes the following keys:

       1. ``datasets``: A list of strings with the dataset id
          whitespace separated by the dataset alias. The database
          aliases can be referenced in the ``where`` clause.

       2. ``where``: An expression or a list of expressions. If it is
          a list, then the expressions in the list will be wrapped
          with the ``and`` function. The expressions are then
          evaluated to perform the joins.

       3. ``return``: OPTIONAL. A string, or an expression, or not
          specified. If it is a string, then it should refer to a
          comma separated list of dataset aliases. In that case all
          the values of those aliases will be returned. If it is an
          expression then the expression is evaluated on the hops
          result and its result is returned. If not specified, then it
          will return the last dataset alias in the list. This is the
          default.

       4. ``track-dependencies``: OPTIONAL. A boolean. The default is
          true. Can be used to disable dependency tracking for this
          particular ``hops`` function.

       | The join criteria are described by using the
         ``eq`` function. All dataset aliases defined in the
         ``datasets`` key have to be joined and all must by navigable
         from the source entity. If that is not the case, then an error
         will be raised.
       | The ``hops`` function produces a table inside, one column per
         dataset alias. This table is the projected down into a list
         of values by the ``return`` clause that is then returned by
         the function.

     - ::

          ["hops", {
            "datasets": ["Address a", "Country c"],
            "return": "a",
            "where": [
              ["or",
                 ["eq", "a.type", "SHIPPING"],
                 ["eq", "a.type", "BILLING"]],
              ["eq", "_S.address", "a._id"],
              ["eq", "c._id", "a.country"]
            ]}]

       | Join the source entity's ``address`` property with the
         ``Address``'s ``_id`` property, and then the ``Address``'s
         ``country`` property with``Country``'s ``_id`` property.
         Filter the addresses by type, so that only shipping and
         billing addresses are included in the result. Return the
         addresses found.



Entity lookups
--------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``reference``
     - | *Arguments:*
       |   DATASET_ID(string{1})
       |   ENTITY_IDS(value-expression{})
       |
       | Returns a URI that can be used to reference entities in the given
         dataset. The DATASET_ID and ENTITY_IDS parts will be URI path
         encoded. URIs of this type can be resolved using the ``lookup`` function.
     - | ``["reference", "foo", "bar"]``
       |
       | Returns ``"~rsesam:foo/bar"`` (which is a value of the URI datatype)).
       |
       | ``["reference", "foo", ["list", "a", "b"]]``
       |
       | Returns ``["~rsesam:foo/a", "~rsesam:foo/b"]``.

   * - ``lookup``
     - | *Arguments:*
       |   DATASET_IDS(value-expression{0|1})
       |   ENTITY_REFERENCES(value-expression{1})
       |
       | Returns an entity or a list of entities by resolving the strings or URIs in
         ENTITY_REFERENCES. The URIs will be resolved by looking up entities by
         id in the given datasets. Relative references will be resolved in the
         current dataset or in the DATASET_IDS datasets if specified. The returned
         entities have an extra ``_dataset`` property containing the id of the dataset
         where they came from.
     - | ``["lookup", "~rsesam:A/foo"]``
       |
       | Looks up the ``foo`` entity in the ``A`` dataset.
       |
       | ``["lookup", "A", ["list", "foo", "sesam:B/bar"]]``
       |
       | Looks up the ``foo`` entity in the ``A`` dataset and the ``bar``
         entity in the ``B`` dataset.
       |
       | ``["lookup", "bar"]``
       |
       | Looks up the ``bar`` entity in the current dataset.
       |
       | ``["lookup",``
       |   ``["list", "A", "B"],``
       |   ``["list", "bar", "baz", "~rsesam:C/foo", "~rsesam:D/quux"]``
       |
       | Looks up the ``bar`` and ``baz`` entities in the ``A`` and ``B`` datasets.
         ``foo`` is looked up in the ``C`` dataset and ``quux`` in the ``D``
         dataset because they are explicit entity references.

URIs
----

.. _curie_function:
.. _uri_expand_function:

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples


   * - ``curie``
     - | *Arguments:*
       |   PREFIX(string{1}),
       |   VALUES(value-expression{1})
       |
     - | Constructs new curies as URI objects based on a the PREFIX and VALUES arguments
       | ``["curie", "foo", "bar"]``
       |
       | This will produce a URI object with the value "~rfoo:bar"
       | ``["curie", "foo", ["list", "bar", "zoo"]]``
       |
       | This will produce a list of two URI objects with the values ["~rfoo:bar", "~rfoo:zoo"]

   * - ``uri-expand``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   ENTITIES(value-expression{1})
       |
     - | Runs the given entities through the prefixing rules and the
         prefix expansion mapping defined in the node metadata RDF registry. The given entities must have a
         ``_dataset`` property containing the id of the dataset to which
         they belong *or* the key to look up the prefixes must be computed by the (optional) FUNCTION argument. The
         result of the FUNCTION argument will override any ``_dataset`` property on the entity. The id given or
         computed will be used to locate the prefix rules and prefix expansion mapping within the node RDF registry.
         Note that the result of FUNCTION must be a single string value.

       | The main purpose of this function is to prepare entities for
         translation into RDF form. See the :doc:`RDF support <rdf-support>`
         document for more information about how this works.

       | Example node metadata:

         ::

            {
                "rdf": {
                  "people": {
                     "prefixes": {
                       "p": "http://example.org/people/"
                     },
                     "prefix_rules": {
                       "id": "p",
                       "properties": [
                          "p", ["name"],
                          "c", ["Employer"],
                          "_", ["**"]
                       ]
                     }
                  }
                }
            }

       | Example input entity:

         ::

            {
              "_id": "john_doe",
              "_dataset": "people",
              "name": "John Doe",
              "employer": "Example org Ltd.",
              "born": "1973-01-21"
            }

       | Given the above configuration you should expect the following URI-expanded
         entity in the result:

         ::

            {
              "_id": "<http://example.org/people/john_doe>",
              "_dataset": "people",
              "<http://example.org/people/name>": "John Doe",
              "<http://example.org/company/employer>": "Example org Ltd.",
              "<http://example.org/born>": "1973-01-21"
            }

       | ``["uri-expand", {"_id": "mary", "_dataset": "people", "name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity.
       |
       | ``["uri-expand", ["lookup", ["list", "~rsesam:A/foo"], "bar"]]``
       |
       | Looks up the ``foo`` entity in the ``A`` dataset and ``bar`` in the current
         dataset, then URI expands them.
       | ``["uri-expand", ["list", {"_id": "mary", "name": "Mary Jones"}]]``
       |
       | Returns an empty list because the ``mary`` entity is missing the ``_dataset``
         property.
       | ``["uri-expand", ["string", "people"], {"_id": "mary", "_dataset": "employees", "name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity using the prefixes registered by the "people" key
         in the node RDF registry (i.e. the ``_dataset`` value of "employees" is overriden by the computed value)

       | ``["uri-expand", ["string", "_.type"], {"_id": "mary", "_dataset": "employees", "type": "person", "name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity using the prefixes registered by the "person" key
         in the node RDF registry. The ``_dataset`` value of "employees" is overriden by the computed value (based on
         the contents of the entity's ``type`` property in this example).

Strings
-------

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
     - | ``["upper", ["list", "a", "b", "c"]]``
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
     - | ``["lower", ["list", "A", "B", "C"]]``
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
     - | ``["length", ["list", "", "a", "bb", "ccc"]]``
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
     - | ``["concat", ["list", "a", "b", "c"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["concat", "_S.tags"]``
       |
       | Returns a concatenated version of the source entity's tags.

   * - ``join``
     - | *Arguments:*
       |   SEPARATOR(string{1})
       |   VALUES(value-expression{1})
       |
       | Returns a string created by joining its input strings by SEPARATOR.
         Non-string values are ignored.
     - | ``["join", "-", ["list", "a", "b", 123, "c"]]``
       |
       | Returns ``"a-b-c"``.
       |
       | ``["join", "-", "_S.tags"]``
       |
       | Returns a joined string of the source entity's tags separated by dashes.

   * - ``split``
     - | *Arguments:*
       |   SEPARATOR(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a list of strings created by splitting its input strings by SEPARATOR.
         Non-string values are ignored.
     - | ``["split", "-", "a-b-c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["split", "-", ["list", "a-b", "c-d", "e"]]``
       |
       | Returns ``["a", "b", "c", "d", "e"]``.
       |
       | ``["split", "-", "_S.uuid"]``
       |
       | Returns a list of strings of the source entity's tags separated by dashes.

   * - ``strip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from both sides. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["strip", [" ab ", "cd ", "ef"]]``
       |
       | Returns ``["ab", "cd", "ef"]``.
       |
       | ``["strip", "  abc"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["strip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed.
       |
       | ``["strip", "x", ["123xxx", "xx456xx"]]``
       |
       | Returns ``["123", "456"]``.

   * - ``lstrip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the left side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["lstrip", [" ab ", "cd ", "ef"]]``
       |
       | Returns ``["ab ", "cd ", "ef"]``.
       |
       | ``["lstrip", "  abc"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["lstrip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed
         from the left.
       |
       | ``["lstrip", "x", ["123xxx", "xx456xx"]]``
       |
       | Returns ``["123xxx", "456xx"]``.

   * - ``rstrip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the right side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["rstrip", [" ab ", "cd ", "ef"]]``
       |
       | Returns ``[" ab", "cd", "ef"]``.
       |
       | ``["rstrip", "  abc"]]``
       |
       | Returns ``"  abc"``.
       |
       | ``["rstrip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed
         from the right.
       |
       | ``["rstrip", "x", ["123xxx", "xx456xx"]]``
       |
       | Returns ``["123", "xx456"]``.

   * - ``replace``
     - | *Arguments:*
       |   OLD_STRING(string{1})
       |   NEW_STRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Replaces occurrences of OLD_STRING with NEW_STRING in VALUES. Non-string values
         are ignored.
     - | ``["replace", "http://", "https://", "http://www.sesam.io/"]``
       |
       | Returns ``"https://www.sesam.io/"``.
       |
       | ``["replace", ":", ".", "_S.date"]]``
       |
       | Returns a date string where the colon has been replaced by a period.

   * - ``matches``
     - | *Arguments:*
       |   PATTERN(string{1})
       |   VALUES(value-expression{1})
       |
       | Returns true if all the values in VALUES match the pattern in PATTERN. The '*' and '?'
         wildcard characters can be used. Non-string values are not matched and will cause the
         function to return false. If PATTERN contains multiple string values then only the
         first one is used.
     - | ``["matches", "a*p*a", ["list", "alpha", alpaca"]``
       |
       | Returns ``true``.
       |
       | ``["matches", "*_sport", ".", "_S.tags"]]``
       |
       | Returns true if all the tags that have a "_sport" suffix.


Values / collections
--------------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``list``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Constructs a list of the values in VALUES.
     - | ``["list"]``
       |
       | Returns ``[]``.
       |
       | ``["list", "a", "b", "c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["list", "a", ["list", "b"], "c"]``
       |
       | Returns ``["a", ["b"], "c"]``.

   * - ``is-list``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a list
       |
     - | ``["is-list", ["list", "foo:bar"]]``
       |
       | Returns true.
       |
       | ``["is-list", "foo:bar"]``
       |
       | Returns false.
       |
       | ``["is-list", ["list", ["uri", "foo:bar"], 12345]]``
       |
       | Returns true
       |
       | ``["is-list", ["dict", "1", 2]]``
       |
       | Returns false
       |
       | ``["is-list", ["items", ["dict", "1", 2]]]``
       |
       | Returns true

   * - ``first``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["first", ["list", "a", "b", "c"]]``
       |
       | Returns ``"a"``.
       |
       | ``["first", "_S.tags"]``
       |
       | Returns the first tag in the source entity's ``tags`` field.

   * - ``last``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the last value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["last", ["list", "a", "b", "c"]]``
       |
       | Returns ``"c"``.
       |
       | ``["last", "_S.tags"]``
       |
       | Returns the last tag in the source entity's ``tags`` field.

   * - ``in``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |   ITEMS(value-expression{1})
       |
       | Boolean function that returns true if VALUES exists in ITEMS. If VALUES is a sequence
         of values, then all VALUES must exist in ITEMS. ITEMS must be a list, If VALUES or ITEMS is empty, then
         false is returned.
     - | ``["in", "a", ["list", "a", "b", "c"]]``
       |
       | Returns true.
       |
       | ``["in", "d", ["list", "a", "b", "c"]]``
       |
       | Returns false.
       |
       | ``["in", ["list", "a", "c"], ["list", "a", "b", "c"]]``
       |
       | Returns true.
       |
       | ``["in", ["list", "a", "c", "d"], ["list", "a", "b", "c"]]``
       |
       | Returns false.


   * - ``nth``
     - | *Arguments:*
       |   INDEX(value-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns the nth value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned only if INDEX is 0. If VALUES is
         empty or the INDEX is out of bounds, then null is returned.
         Note that INDEX is zero-based.

     - | ``["nth", 1, ["list", "a", "b", "c"]]``
       |
       | Returns ``"b"``.
       |
       | ``["nth", 5, ["list", "a", "b", "c"]]``
       |
       | Returns ``null``.
       |
       | ``["nth", 1, "_S.tags"]``
       |
       | Returns the second tag in the source entity's ``tags`` field.

   * - ``flatten``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Flattens its input values in VALUES. Note that it does *not* do so
         recursively. Constructs a new list.
     - | ``["flatten", ["list", 1, 2, ["list", 3, 4]]]``
       |
       | Returns ``[1, 2, 3, 4]``.
       |
       | ``["flatten", ["list", ["list", 1, 2], ["list", 3, ["list", 4], 5]]]``
       |
       | Returns ``[1, 2, 3, [4], 5]``.
       |
       | ``["flatten", ["list", "_S.sisters", "_S.brothers"]]``
       |
       | Returns a list that contains the sisters and brothers.

   * - ``filter``
     - | *Arguments:*
       |   FILTER(boolean-expression(1}
       |   VALUES(value-expression{1})
       |
       | Filters out the the values in VALUES for which the FILTER expression
         does *not* evaluate to *true*.
     - | ``["filter", ["gt", "_.age", 42],``
       |     ``["list", {"age": 30}, {"age": 50}, {"age": 40}]]``
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
     - | ``["min", ["list", 4, 2, 5, 3]]``
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
     - | ``["max", ["list", 4, 2, 5, 3]]``
       |
       | Returns ``5``.
       |
       | ``["max", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the highest amount.

   * - ``sum``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the sum of the numeric values in VALUES. Any non-numeric values are ignored.
     - | ``["sum", ["list", 2, 4, 6]]``
       |
       | Returns ``12``.
       |
       | ``["sum", "_S.amounts"]]``
       |
       | Returns the sum of the amounts.

   * - ``count``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the number of elements in VALUES.
     - | ``["count", ["list", 2, 4, 6]]``
       |
       | Returns ``3``.
       |
       | ``["count", "_S.orders"]]``
       |
       | Returns the the number of orders.

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
     - | ``["distinct", ["list", 4, 2, 5, 4, 3]]``
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
       | Returns VALUES sorted in ascending order. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that. If VALUES is not
         a list, then VALUES is returned.
     - | ``["sorted", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[2, 3, 4, 4, 5]``.
       |
       | ``["sorted", "_.age", ["list", {"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 20}, {"age": 30}, {"age": 50}]``.
       |
       | ``["sorted", "_S.tags"]]``
       |
       | Returns the tags in ascending order.

   * - ``sorted-descending``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns VALUES sorted in descending order. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that. If VALUES is not
         a list, then VALUES is returned.
     - | ``["sorted-descending", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[5, 4, 4, 3, 2]``.
       |
       | ``["sorted-descending", "_.age", ["list", {"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 50}, {"age": 30}, {"age": 20}]``.
       |
       | ``["sorted-descending", "_S.tags"]]``
       |
       | Returns the tags in descending order.

   * - ``reversed``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns VALUES in reversed order.
     - | ``["reversed", ["list", 1, 3, 2]]``
       |
       | Returns ``[2, 3, 1]``.
       |
       | ``["reversed", ["sorted", "_S.tags"]]``
       |
       | Returns list of tags sorted in descending order.

   * - ``map``
     - | *Arguments:*
       |   FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each value in VALUES apply the FUNCTION function and construct a new
         list of the return values.
     - | ``["map", ["lower", "_."], ["list", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["map", ["distinct", "_."],``
       |   ``["list", ["list", "A", "A"], ["list", "B", "C"]]]``
       |
       | Returns ``[["A"], ["B", "C"]]``.

   * - ``group-by``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Groups the values in VALUES by the result of executing the FUNCTION function
         on them. Returns a dictionary, where the key is the
         group key and the value is the list of values in VALUES that were
         grouped under that key.
     - | ``["group-by", ["length", "_.], ["list", "phi", "alpha", "rho"]]``
       |
       | Returns ``{3: ["phi", "rho"], 5: ["alpha"]}``.
       |
       | ``["group-by", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns order lines grouped by EAN, i.e. product number.
       |
       | ``["group-by", "_.gender", "_S.people"]]``
       |
       | Returns a dictionary of people grouped by their gender.


Sets
----

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
     - | ``["union",``
       |     ``["list", "A", "B"], ["list", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union", "A", ["list", "B", "C"]]``
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
     - | ``["intersection",``
       |     ``["list", "A", "B"], ["list", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "B", ["list", "B", "C"]]``
       |
       | Returns ``["B"]``.
       |
       | ``["intersection", "A", ["list", "B", "C"]]``
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
     - | ``["difference",``
       |    ``["list", "A", "B"], ["list", "B"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference", "A", ["list", "B", "C"]]``
       |
       | Returns ``["A"]``.
       |
       | ``["difference",``
       |   ``["list", "A", "B", "C", "D"],``
       |   ``["list", "A", "B", "E"]]``
       |
       | Returns ``["C", "D"]``.


Dictionaries / Entities
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``items``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a single list of key+value tuples.
         For each key+value pair in the dictionaries one pair is added to the output
         list. Non-dictionary values are ignored. Note that entities are dictionaries,
         so you can use this function with them.
     - | ``["items",``
       |     ``["list", {"A": 1, "B": 2}, {"C": 3}]]``
       |
       | Returns ``[["A", 1], ["B", 2], ["C", 3]]``.
       |
       | ``["items", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``[["A": 1]]``.

   * - ``dict``
     - | *Arguments:*
       |   ITEMS(value-expression{1})
       |
       | Takes a list of key+value pair tuples and returns a single dictionary with
         those tuples as keys and values. Note that the last key in the tuple list
         wins. Values are not two-element tuples are ignored.
     - | ``["dict",``
       |     ``["list",``
       |         ``["list", "A", 1],``
       |         ``["list", "B", 2],``
       |         ``["list", "C", 3]]]``
       |
       | Returns ``{"A": 1, "B": 2, "C": 3}``.
       |
       | ``["dict", ["list", "X", 123, ["A", 1]]``
       |
       | Returns ``{"A": 1}``.

   * - ``is-dict``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a dictionary or if it is a list, that the first element
       | in the list is a dictionary
       |
     - | ``["is-dict", ["dict", "1", 2]]``
       |
       | Returns true.
       |
       | ``["is-dict", "foo:bar"]``
       |
       | Returns false

   * - ``keys``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a single list of keys.
         For each key+value pair in the dictionaries one key is added to the output
         list. Non-dict values are ignored.
     - | ``["keys",``
       |     ``["list", {"A": 1, "B": 2}, {"A": 1, "C": 3}]]``
       |
       | Returns ``["A", "B", "A", "C"]``.
       |
       | ``["keys", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``["A"]``.

   * - ``values``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a single list of values.
         For each key+value pair in the dictionaries one value is added to the output
         list. Non-dict values are ignored.
     - | ``["values",``
       |     ``["list", {"A": 1, "B": 2}, {"A": 1, "C": 3}]]``
       |
       | Returns ``[1, 2, 1, 3]``.
       |
       | ``["values", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``[1]``.


Math
----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

   * - ``plus``
     - | *Arguments:*
       |   INCREMENT(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and increments them by INCREMENT. Non-numeric
         values are ignored.
     - | ``["plus", 10, ["list", 1, 2, 3]]``
       |
       | Returns ``[11, 12, 13]``.
       |
       | ``["plus", 10, 10]``
       |
       | Returns ``20``.

   * - ``minus``
     - | *Arguments:*
       |   DECREMENT(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and decrements them by DECREMENT. Non-numeric
         values are ignored.
     - | ``["minus", 1, ["list", 1, 2, 3]]``
       |
       | Returns ``[0, 1, 2]``.
       |
       | ``["minus", 10, 12]``
       |
       | Returns ``2``.

   * - ``divide``
     - | *Arguments:*
       |   DIVISOR(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and divides them by DIVISOR. Non-numeric
         values are ignored.
     - | ``["divide", 2, ["list", 2, 4, 6]]``
       |
       | Returns ``[1, 2, 3]``.
       |
       | ``["divide", 10, 20]``
       |
       | Returns ``2``.
       |
       | ``["divide", 2, 3]``
       |
       | Returns ``1.5``.

   * - ``multiply``
     - | *Arguments:*
       |   MULTIPLIER(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and multiplies them by MULTIPLIER. Non-numeric
         values are ignored.
     - | ``["multiply", 2, ["list", 2, 4, 6]]``
       |
       | Returns ``[4, 8, 12]``.
       |
       | ``["multiply", 10, 20]``
       |
       | Returns ``200``.
       |
       | ``["multiply", 2.3, 2]``
       |
       | Returns ``4.6``.

   * - ``mod``
     - | *Arguments:*
       |   DIVISOR(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and finds the remainder of dividing them
         by DIVISOR. Non-numeric values are ignored.
     - | ``["mod", 2, ["list", 2, 5, 6]]``
       |
       | Returns ``[0, 1, 0]``.
       |
       | ``["mod", 3, 5]``
       |
       | Returns ``2``.
