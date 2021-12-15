.. _DTLReferenceGuide:

=====================
 DTL Reference Guide
=====================

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

The Data Transformation Language (DTL) has been created as a means to allow developers to clearly describe transformations that should be performed on streams of data in order to create new datasets.

Core Concepts
-------------

DTL allows developers to describe a data transform. The DTL processor applies the transform to a stream of entities. For each entity in the stream the same transform is applied. The result of processing is a stream of new entities.

A DTL transform describes how to construct new entities from the source entity. A transform can also perform hops that range across datasets in the datahub. These hops must start from the source entity.

DTL consists of 'functions' that can pick and transform data and 'hops' that can traverse the data in the datahub. In combination these offer a powerful way to construct new data entities from existing data. DTL functions are composable and thus allowing complex computation to be expressed.

Syntax
------

DTL uses a JSON syntax to describe the transforms to perform. In general DTL uses functions over keywords and as such there are just a few terms that are baked into the language.

An example using the 'add' transform:

  ["add", "name", "_S.firstname"]

And composing functions:

  ["add", "name", ["concat", ["upper", "_S.lastname"], ", ", "_S.firstname"]]


Annotated Example
=================

Lets say that we have two datasets ``person`` and ``orders``, and that
we want to transform the *persons* by joining in their *orders* and
apply a few other transform functions. In this section you'll find a
complete DTL transform that takes entities from the ``person`` dataset,
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

A pipe with the ``dtl`` transform below lets us transform persons into
persons with orders:

::

    {
      "_id": "person-with-orders",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "person"
      },
      "transform": {
        "type": "dtl",
        "rules": {
            "default": [
                ["copy", "_id"],
                ["add", "type", "customer"],
                ["add", "name", ["upper", "_S.name"]],
                ["add", "orders",
                  ["sorted", "_.amount", ["apply-hops", "order", {
                    "datasets": ["orders o"],
                    "where": [
                      ["eq", "_S._id", "o.cust_id"]
                    ]
                }]]],
                ["add", "order_count", ["count", "_T.orders"]],
                ["filter", ["gt", "_T.order_count", 10]]
            ],
            "order": [
                ["copy", "_id"],
                ["add", "amount", "_S.amount"]
            ]
        }
      },
      "sink": {
          "type": "dataset",
          "dataset": "person-with-orders"
      }
    }

Explanation:

1. | The ``dtl`` transform will receive source entities from the
     ``person`` dataset. It will transform them and they'll be written
     to the ``person-with-orders`` dataset.

2. | There are two named ``rules`` specified in the DTL transform:
     ``default`` and ``order``. The ``default`` rule is mandatory and
     is the one that is applied to the entities in the ``person``
     dataset.

3. | ``["copy", "_id"]`` copies the ``_id`` property from the source
     entity to the target entity.

4. | ``["add", "type", "customer"]`` adds the ``type`` property to the target
     entity with the literal value ``"customer"``.

5. | ``["add", "name", ["upper", "_S.name"]]`` add the ``name``
     property to the target entity by uppercasing the name in the source
     entity.

   ::

       ["add", "orders",
         ["sorted", "_.amount", ["apply-hops", "order", {
           "datasets": ["orders o"],
           "where": [
             ["eq", "_S._id", "o.cust_id"]
           ]
       }]]]

6. | The expression above adds the ``orders`` property to the target
     entity. It does this by joining the source entity's ``_id``
     property with the ``cust_id`` property of entities in the
     ``orders`` dataset. The join is done by the ``apply-hops`` function,
     which takes a hops specification that contains list of ``datasets``,
     assigns aliases to them, which then get exposed as variables that
     you can use in expressions in the ``where`` clause. The result of
     the join is a list of orders:

   ::

    [{
      "_id": "100",
      "amount": 320,
      "order_lines": [...],
      "cust_id": "1"
    },
    {
      "_id": "200",
      "amount": 500
      "order_lines": [...],
      "cust_id": "1"
    }]

   | Next, the ``order`` transform is then applied. The result of this
     is a list of orders with two properties: ``_id`` and ``amount``:

   ::

    [{
      "_id": "100",
      "amount": 320
    },
    {
      "_id": "200",
      "amount": 500
    }]

   | The order entities are then ``sorted`` by their ``amount``
     property before being assigned to the ``orders`` property on the
     target entity:

   ::

    [{
      "_id": "100",
      "amount": 320
    },
    {
      "_id": "200",
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

- the hops function is deterministic but not sorted (it produces deterministic order
  based on the ``_id`` property of the entities within each dataset it processes).
  You must apply the ``sorted`` function to the result of a hops join to achieve a
  particular order.

- The filter function can be used to stop transformation of individual
  entities, effectively filtering them out of the output stream.

- When the DTL of a pipe is modified, the pipe's "last-seen" value must be
  cleared in order to reprocess already seen entities with the new DTL.
  This can be done by setting the "last-seen" value to an empty string with the
  `update-last-seen <./api.html#api-reference-pump-update-last-seen>`_ operation in the SESAM API.


.. _variables:

Variables
=========

There are four built-in variables in the Data Transformation
Language. These are ``_S``, ``_T``, ``_P``, ``_B`` and ``_``. They refer to
the source entity, the target entity, the parent context, bound endpoint variables and the
current value respectively. ``_S`` and ``_T`` appear in pairs inside
each applied transform. ``_P`` appears inside the ``apply`` function
and refers to the parent context. ``_`` is used to refer to the
current value in functional expressions. The ``_B`` variable is used by the :ref:`HTTP endpoint sinks <http_endpoint_sink>` to hold variables
defined by URL parameters (i.e. a URL variable ``foo`` given to the endpoint API on the form
``http://my_host:port/api/publishers/my_endpoint?foo=bar`` will be reflected in the ``_B`` map as a key ``foo`` with
the value ``bar``). It is useful for parameterizing the transform on an endpoint sink.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Variable
     - Description
     - Examples

       .. _s_variable:

   * - ``_S``
     - Refers to the source entity. This is the entity on which the
       DTL transform operate. Note that with the ``apply`` function
       you can apply nested transform rules, where each of the values
       given to ``apply`` is made a source entity for that nested
       transform.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater than 42.

       .. _t_variable:

   * - ``_T``
     - Refers to the target entity. This is the entity that is the
       primary target entity of transforming the source entity. Note
       that the ``create`` transform can be used to emit entities
       in addition to just the target entity.
     - | ``["gt", ["length", "_T.length"], 100]``
       |
       | The target entity's ``description`` field must have a length of
         more than 100 characters.

       .. _p_variable:

   * - ``_P``
     - A dict that contains the source entity and the
       target entity of the parent context. If the parent context also has
       a parent context, then that will also be available. The dict always
       contains the ``_S`` and ``_T`` variables, while the ``_P`` property is
       optional.  ``_P`` does not contain the ``_R`` variable. Note that
       the ``_P`` appears only inside the ``apply`` function.

     - | ``["gt", "_P._S.age", 18]``
       |
       | The parent source entity's ``age`` field must be greater than 18.
       |
       | ``["lt", ["length", "_P._P._T.description"], 100]``
       |
       | The grandparent target entity's ``description`` field must have a
         length of less than 100 characters.

       .. _r_variable:

   * - ``_R``
     - A dict that contains the source entity and the
       target entity of the root context. The root context is the outermost
       context, which in practice is the context of the ``default`` rule. The
       dict contains the ``_S`` and ``_T`` variables.

     - | ``["lt", "_R._S.age", 18]``
       |
       | The root source entity's ``age`` field must be less than 18.
       |
       | ``["lt", ["length", "_R._T.description"], 50]``
       |
       | The root target entity's ``description`` field must have a
         length of less than 50 characters.

       .. _underscore_variable:

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


.. _path_expressions_and_hops:

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
   e.g. ``"_S."`` would refer to the source entity itself (note the dot
   after the variable name). ``"_T."`` refers to the target entity, and
   ``"_."`` refers to the current value.

   You can have periods in path elements if you quote them. Example:
   ``"_S.foo.'john.doe''s'.bar"`` is equivalent to
   ``["path", ["list", "foo", "john.doe's", "bar"], , "_S."]``. A quoted path
   element must begin and end with a single quote. Single quotes can
   be escaped with ``''``.

2. **The "path" function**: ``["path", "placed_by", ["sorted",
   "_.amount", "_S.orders"]]``, which will first evaluate the
   rightmost expression. Then it will traverse the path given in the
   first argument for each of them and return the end result. The
   first argument is an expression that resolve to either a single
   string or a list of strings. Note that the ``path`` function can
   only access property on the dictionary/entity it operates on,
   including nested ones.

3. **The "hops" function**:

   ::

       ["hops", {
           "datasets": ["orders o"],
           "where": [
             ["eq", "_S._id", "o.cust_id"],
             ["eq", "o.type", "BILLING"]
           ]
       }]

   The ``hops`` function can be used to perform :ref:`joins <joins>` across two or
   more datasets, so if you want to navigate beyond the current entity
   use ``hops``. This particular example will join the source entity
   with entities from the ``orders`` dataset using the ``["eq",
   "_S._id", "o.cust_id"]`` join expression and then filter the orders
   by ``["eq", "o.type", "BILLING"]``. Note that only ``eq`` functions
   will be treated as join expressions. All other function are treated
   as filter expressions. For an ``eq`` to be a join expression it
   will have to refer to variables from two different datasets.

.. _joins:

How joins work
==============

Given two entities ``A`` and ``B`` bound to the dataset aliases ``a``
and ``b`` in the expressions below:

::

   {
     "_id": "A",
     "value": 1,
     "values": [1, 2, 4, 5]
   }

::

   {
     "_id": "B",
     "value": 1,
     "values": [1, 3, 4, 6]
   }

There are four different kinds of joins:

1. One-to-one join: ``["eq", "a.value", "b.value"]``

2. One-to-many: ``["eq", "a.value", "b.values"]``

3. Many-to-one: ``["eq", "a.values", "b.value"]``

4. Many-to-many: ``["eq", "a.values", "b.values"]``

The rule for joins is very simple: *if any of the values overlap,
then the join succeeds*.

All of the four joins given above succeed for the two entities because
they all have overlapping values, i.e. the values ``1`` and ``4``.

Join expressions that contain functional expressions work the same
way, e.g. ``["eq", ["+", "a.value", 2], "b.values"]`` succeeds as ``3``
is a value shared by both.

If you need to do joins with composite keys then the :ref:`tuples
<tuples_dtl_function>` DTL function is useful. Using composite keys is
almost always a better choice than having multiple individual joins as
the former will have better precision.

.. NOTE::

   ``null`` values and deleted entities are not indexed, so they are
   not traversed by joins.

.. NOTE::

   It is only ``eq`` functions that reference a single dataset alias
   in both left and right arguments that are considered join
   functions.

   There must be exactly one unique dataset alias reference
   in each ``eq`` argument.

.. _namespace_aware_functions:

Namespaces
==========

The following functions are namespace aware: :ref:`add
<dtl_transform-add>`, :ref:`default <dtl_transform-default>`,
:ref:`make-ni <dtl_transform-make-ni>`, :ref:`remove
<dtl_transform-remove>`, :ref:`copy <dtl_transform-copy>`,
:ref:`rename <dtl_transform-rename>` and :ref:`path
<path_dtl_function>`. This means they behave slightly differently when
:ref:`namespaced identifiers <namespaces>` is enabled.

- Function arguments that are of type ``wildcard-string`` will make
  pattern matching aware of the boundary between the namespace and the
  identifier parts of namespaced identifiers.

- Function arguments that reference unqualified properties,
  i.e. properties with only the identifier part, will in general match
  that property in all namespaces.

See the individual functions for more details.

.. _ni_escape_syntax:

NI escape syntax
----------------

``"foo:bar"`` is an example of a fully qualified namespaced
identifier. ``"bar"`` is an unqualified one and consists of only the
identifier part.

There exists two special escape prefixes, ``":"`` and ``"::"``.

- If you want to make sure that the value is to be interpreted as-is
  then use the ``"::"`` prefix, e.g. ``"::bar"``. ``"::foo:bar"`` is
  equivalent to ``"foo:bar"``.

- If you want the value to be relative to the current namespace,
  i.e. identity or property namespace depending on the context, then use
  the ``":"`` prefix, e.g. ``":bar"``. If the current property namespace
  is ``"foo"`` then ``":bar"`` is equivalent to ``"foo:bar"``.

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

   * - ``integer-expression``
     - | Refers to an expression that returns a single "integer" value.
     - | ``["+", 1, 2]``

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
     - | ``["add", "type", "person"]``
       |
       | or
       |
       | ``[["add", "type", "person"],``
       |  ``["copy", ["list", "name", "age"]]]]``

.. _dtl-transforms:

Transforms
==========

A transform function is a function that has side-effects, typically
modifying the target entity, and has no return value.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _`dtl_transform-if`:

   * - ``if``
     - | *Arguments:*
       |   CONDITION(boolean-expression{1}),
       |   THEN(transforms{1}),
       |   ELSE(transforms{0|1})
       |
       | If CONDITION evaluates to *true* then apply the transforms in THEN,
       | otherwise apply the transforms in ELSE.

       | Note that the THEN and ELSE arguments can either be a single transform
         function or a list of transform functions. The list can be empty.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

          | ``["if", ["gt", "_S.age", 18],``
          |      ``[["add", "type", "adult"],``
          |       ``["add", "is_adult", true]],``
          |      ``["add", "type", "child"]]``

     - | ``["if", ["eq", "_S.type", "person"], [``
       |      ``["add", "type", "person"],``
       |      ``["copy", ["list", "name", "age"]]]]``
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

       .. _dtl_transform-case-eq:
   * - ``case-eq``
     - | *Arguments:*
       |   VALUE(value-expression{1}),
       |   (VALUE_N(value-expression{1},
       |    THEN(transforms{1}))+,
       |   ELSE(transforms{0\|1})
       |
       | Evaluates the first THEN for which VALUE is equal to VALUE_N. If there is no
         match, then ELSE is evaluated. If there is no ELSE, then it is a no-op.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

     - | ``["case-eq", "_S.country",``
       |   ``"NO", ["add", "country", "Norway"],``
       |   ``"SE", ["add", "country", "Sweden"],``
       |   ``["add", "country", "Other"]]``
       |
       | Given then value of ``_S.country``, adds ``{"country": "Norway"}`` if the value is ``"NO"``
         and ``{"country": "Sweden"}`` if the value is ``"SE"``, otherwise ``{"country": "Other"}`` is added.
       |
       | ``["case-eq", "_S.dialing_code",``
       |   ``45, ["add", "country_code", "DK"],``
       |   ``46, ["add", "country_code", "SE"],``
       |   ``47, ["add", "country_code", "NO"]]``
       |
       | Given the value of ``_S.dialing_code``, adds ``{"country": "DK"}`` if the value is
         ``45`` and ``{"country": "SE"}`` if the value  is ``46`` and ``{"country": "NO"}`` if the value is ``47``,
         otherwise it is a no-op.

       .. _dtl_transform-case:
   * - ``case``
     - | *Arguments:*
       |   (VALUE(value-expression{1},
       |    THEN(transforms{1}))+,
       |   ELSE(transforms{0\|1})
       |
       | Evaluates the first THEN for which VALUE is true. If there is no
         match, then ELSE is evaluated. If there is no ELSE, then it is a no-op.

       .. NOTE::

          If you need to specify multiple transforms then wrap them in a list.

     - | ``["case",``
       |   ``["gte", "_S.age", 18], ["add", "group", "adult"]],``
       |   ``["gte", "_S.age", 13], ["add", "group", "teenager"],``
       |   ``["gte", "_S.age", 2], ["add", "group", "toddler"],``
       |   ``["lt", "_S.age", 2], ["add", "group", "baby"],``
       |   ``["add", "group", "unknown"]]``
       |
       | Adds ``{"group": "adult"}`` if the value of ``_S.age`` is greater than or equal to ``18``,
       | or ``{"group": "teenager"}`` if the value of ``_S.age`` is greater than or equal to ``13``,
       | or ``{"group": "toddler"}`` if the value of ``_S.age`` is less than ``2``,
       | otherwise ``{"group": "unknown"}``.

       .. _`dtl_transform-comment`:

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

       .. _`dtl_transform-filter`:

   * - ``filter``
     - | *Arguments:*
       |   UNLESS_CONDITION(boolean-expression{0|1})
       |
       | If the evaluation of the UNLESS_CONDITION expression returns false, then stop
         applying transformations. In this case *no* target entity is emitted
         for the source entity. Note that any entities already emitted by
         ``create`` will not be stopped. If you want then make sure that you don't
         create them before the ``filter``.
       |
       | If the UNLESS_CONDITION argument is not given then the filter evaluates to
         false.

       .. NOTE::

          If used with a ``dataset`` sink then the ``filter`` function
          will set the ``_filtered`` property to ``true`` and emit the
          entity.

          The reason for this is so that the ``dataset`` sink can
          detect deleted entities even on incremental syncs, not just
          on full syncs. Entities with the ``_filtered`` property set to
          ``true`` will thus be deleted from the dataset if the entity
          already exists and it is not already deleted.

          The rationale for this behaviour is so that entities that
          have previous versions get deleted in the resulting dataset
          when they no longer pass the filter.

          If you have more than one transform then you may want to be
          careful about how you process ``_filtered`` entities in
          subsequent transforms.

          If you would like to control how deletions happen, then you
          should not use the ``filter`` function, but instead set the
          ``_deleted`` property.

     - | ``["filter", ["gt", "_S.age", 42]]``
       |
       | Continue processing only if the source entity's age is greater than 42.
       |
       | ``["filter", ["eq", "_S.type", "person"]]``
       |
       | Continue processing only if the source entity's type is ``person``.
       |
       | ``["filter"]``
       |
       | Stop processing.
       |

       .. _`dtl_transform-discard`:

   * - ``discard``
     - | *Arguments:*
       |   UNLESS_CONDITION(boolean-expression{0|1})
       |
       | This transform is almost identical to ``filter``, but will drop the target
         entity on the floor. Use it with care as the discarded entity will not be
         deleted in the sink.
       |
       | If the evaluation of the UNLESS_CONDITION expression returns false, then stop
         applying transformations. In this case *no* target entity is emitted
         for the source entity. Note that any entities already emitted by
         ``create`` will not be stopped. If you want then make sure that you don't
         create them before the ``discard``.
       |
       | If the UNLESS_CONDITION argument is not given then the target entity will be discarded.

       .. WARNING::

          Only use this transform when you know that you've never sent an entity
          with the same ``_id`` to the sink before. The reason is that that the entity will
          then not be deleted in the sink. If you want it to be deleted then use the
          ``filter`` transform instead.

     - | ``["discard", ["gt", "_S.age", 42]]``
       |
       | Discard the target entity unless the source entity's age is greater than 42.
       |
       | ``["discard", ["eq", "_S.type", "person"]]``
       |
       | Discard the target entity unless the source entity's type is ``person``.
       |
       | ``["discard"]``
       |
       | Discard the target entity unconditionally.
       |

       .. _`dtl_transform-add`:

   * - ``add``
     - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field(s) to the target entity with the values returned
         by evaluating the VALUES expression.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.

     - | ``["add", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity.
       |
       | ``["add", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity. The value is
         the uppercased version of the source entity's ``name`` property.
       |
       | ``["add",``
       |   ``["concat", "x-", "_S.key"], "_S.value"]``
       |
       | Adds the property returned by the ``concat`` function and assigns it the
         value returned by ``_S.value``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:* ``{}``
       |
       | ``["add", "age", 26]``
       |
       | Result: ``{"bar:age": 26}``. Adds the ``bar:age`` property with the value
         26 to the target entity.
       |
       | ``["add", "person:age", 26]``
       |
       | Result: ``{"person:age": 26}``. Adds the ``person:age`` property with the
         value 26 to the target entity.
       |
       | ``["add", "::age", 26]``
       |
       | Result: ``{"age": 26}``. Adds the ``age`` property with the value 26 to
         the target entity. Note
         that if the PROPERTY arguments starts with ``::`` it will be interpreted
         to mean add what ever is after the double colons. See
         :ref:`NI escape syntax <ni_escape_syntax>` for more details.
       |
       | ``["add", ":age", 26]``
       |
       | Result: ``{"bar:age": 26}``. Adds the ``bar:age`` property with the value
         26 to the target entity.
         Note that this example uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to reference the current namespace.

       .. _`dtl_transform-default`:

   * - ``default``
     - | *Arguments:*
       |   PROPERTY(string{1})
       |   VALUES(value-expression{1})
       |
       | Adds the PROPERTY field(s) to the target entity with the values returned
         by evaluating the VALUES expression, unless the property already exists.
         ``default`` behaves exactly like ``add``, except that it does not add
         the property if the property already exists on the target entity. If
         the property exists it does nothing.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.
     - | ``["default", "age", 26]``
       |
       | Adds the ``age`` property with the value 26 to the target entity, if
         the property does not exists.
       |
       | ``["default", "upper_name", ["upper", "_S.name"]]``
       |
       | Adds the ``upper_name`` property to the target entity, if
         the property does not exists.. The value is
         the uppercased version of the source entity's ``name`` property.
       |
       | ``["default",``
       |   ``["concat", "x-", "_S.key"], "_S.value"]``
       |
       | Adds the property returned by the ``concat`` function and assigns it the
         value returned by ``_S.value``, if the property does not exists..
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:* ``{}``
       |
       | ``["default", "age", 26]``
       |
       | Result: ``{"bar:age": 26}``. If the target entity does not already have
         the ``bar:age`` property, then
         the ``bar:age`` property with the value 26 is added to the target entity.
       |
       | ``["default", "person:age", 26]``
       |
       | Result: ``{"person:age": 26}``. If the target entity does not already have
         the ``person:age`` property, then
         the ``person:age`` property with the value 26 is added to the target entity.
       |
       | ``["default", "::age", 26]``
       |
       | Result: ``{"age": 26}``. If the target entity does not already have the
         ``age`` property, then
       | the ``age`` property with the value 26 is added to the target entity. Note
         that if the PROPERTY arguments starts with ``::`` it will be interpreted
         to mean add what ever is after the double colons. See
         :ref:`NI escape syntax <ni_escape_syntax>` for more details.
       |
       | ``["default", ":age", 26]``
       |
       | Result: ``{"bar:age": 26}``. If the target entity does not already have the
         ``bar:age`` property, then
         the ``bar:age`` property with the value 26 is added to the target entity.
         Note that this example uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to reference the current namespace.

       .. _`dtl_transform-make-ni`:

   * - ``make-ni``
     - | *Arguments:*
       |   NAMESPACE(string{1})
       |   FROM_PROPERTY(string{1})
       |   TO_PROPERTY(string{0|1})
       |
       | Adds the FROM_PROPERTY field to the target entity's TO_PROPERTY with
         string values made into namespaced identifiers in the NAMESPACE namespace.
         If none of the values can be made into namespaced identifiers then nothing is added. If
         TO_PROPERTY is omitted then it defaults to FROM_PROPERTY + ``-ni``.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         If namespaced identifiers are enabled,
         then the property will be prefixed by the current
         namespace. If the property is ``_id`` then the string values
         will be prefixed by the identity namespace. All other
         properties will have their name prefixed by the property
         namespace.
     - | ``["make-ni", "soccer", "referee", "ref"]``
       |
       | If the source entity has ``{"referee": "john.doe"}`` then adds the ``ref``
         property with the value ``~:soccer:john.doe`` to the target entity.
       |
       | ``["make-ni", "hockey", "players"]``
       |
       | Adds the ``players-ni`` property to the target entity, if
         any namespaced identifiers were created.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"referee": "john.doe",``
       |  ``"x:referee": "john.c.doe"}``
       |
       | ``["make-ni", "soccer", "referee"]``
       |
       | Result:
       | ``{ "referee-ni": "~:soccer:john.doe"``
       |   ``"x:referee-ni": "~:soccer:john.c.doe" }``.
       | Copies all ``referee`` properties in all namespaces from the source entity
         to the target entity. Note that the target properties are suffixed by ``-ni``.
         The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "referee", "ref"]``
       |
       | Result:
       | ``{ "ref": "~:soccer:john.doe"``
       |   ``"x:ref": "~:soccer:john.c.doe" }``.
       | Copies all ``referee`` properties in all namespaces from the source entity
         to the target entity. Note that the target properties are *not* suffixed by
         ``-ni``. The properties keep their namespaces, but the identifier
         part is replaced by ``ref``. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee"]``
       |
       | Result:
       | ``{ "x:referee-ni": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``x:referee-ni`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee", "ref"]``
       |
       | Result:
       | ``{ "x:ref": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``x:ref`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.
       |
       | ``["make-ni", "soccer", "x:referee", "y:ref"]``
       |
       | Result:
       | ``{ "y:ref": "~:soccer:john.c.doe" }``.
       | Copies the ``x:referee`` property as ``y:ref`` from the source entity
         to the target entity. The values are converted into
         NIs by adding the ``soccer`` namespace. Any non-string values are ignored.

       .. _`dtl_transform-remove`:

   * - ``remove``
     - | *Arguments:*
       |   PROPERTY(wildcard-string{1})
       |
       | Removes the PROPERTY field from the target entity. The PROPERTY can
         be pattern with ``*`` and ``?`` characters in it. The pattern must match
         the full property names.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         The pattern in PROPERTY is namespace aware, so the last colon in the pattern
         is considered to be the separator between the namespace and the identifier.
     - | ``["remove", "age"]``
       |
       | Removes the ``age`` property from the target entity.
       |
       | ``["remove", "temp_*"]``
       |
       | Removes all properties matching the ``temp_*`` wildcard pattern from
         the target entity.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Target entity:*
       | ``{"age": 36,``
       |  ``"x:age": 36}``
       |  ``"y:age": 36}``
       |
       | ``["remove", "age"]``
       |
       | Result: ``{}``.
       | Removes the ``age`` property in all namespaces from the target entity.
       |
       | ``["remove", "x*:age"]``
       |
       | Result: ``{"age": 36, "y:age": 36}``.
       | Removes the ``age`` property in all namespaces starting with ``x``
         from the target entity.
       |
       | ``["remove", "x:age"]``
       |
       | Result: ``{"age": 36, "y:age": 36}``.
       | Removes the ``x:age`` property from the target entity.

       .. _`dtl_transform-copy`:

   * - ``copy``
     - | *Arguments:*
       |   INCLUDE_PROPERTIES(wildcard-string-list{1})
       |   EXCLUDE_PROPERTIES(wildcard-string-list{1})
       |
       | Copies properties in INCLUDE_PROPERTIES from the source entity to the
         target entity. Any properties matching any of the EXCLUDE_PROPERTIES
         patterns are not included. INCLUDE_PROPERTIES and EXCLUDE_PROPERTIES
         can be a single string or a list of strings, where the strings are
         patterns. ``*`` and ``?`` are valid pattern characters.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         The pattern in PROPERTY is namespace aware, so the last colon in the pattern
         is considered to be the separator between the namespace and the identifier.
     - | ``["copy", "age"]``
       |
       | Copies the ``age`` property from the source entity to the target entity.
       |
       | ``["copy", "a*", "ab*"]``
       |
       | Copies all properties starting with ``a`` from the source entity to the
         target entity, but not those starting with ``ab``.
       |
       | ``["copy",``
       |   ``["list", "a*", "b*"],``
       |   ``["list", "ab*", "ba*"]]``
       |
       | Copies all properties starting with ``a`` or ``b`` from the source entity
         to the target entity, but not those starting with ``ab`` or ``ba``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"age": 36,``
       |  ``"x:age": 36}``
       |  ``"xyz:age": 36}``
       |
       | ``["copy", "age"]``
       |
       | Result:
       | ``{ "age": 36.``
       |   ``"x:age": 36,``.
       |   ``"xyz:age": 36}``.
       | Copies the ``age`` property in all namespaces to the target entity.
       |
       | ``["copy", "x*:*e", "*y*:*e"]``
       |
       | Result: ``{ "x:age": 36 }``.
       | Copies the properties ending with ``e`` in all namespaces starting with ``x``,
         except those in a namespace that contains the character ``y``,
         to the target entity.

       .. _`dtl_transform-rename`:

   * - ``rename``
     - | *Arguments:*
       |   PROPERTY1(string{1})
       |   PROPERTY2(string{1})
       |
       | Copies the PROPERTY1 field from the source entity to the PROPERTY2 field
         on the target entity. This is effectively a way to copy and rename
         properties from the source entity to the target entity. No wildcard
         patterns are supported.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         If namespaced identifiers are enabled,
         then the renaming makes sure that any namespaces on the target entity either
         keep their original namespaces or all values are collected into a single
         property on the target.
     - | ``["rename", "age", "current_age"]``
       |
       | Copies the ``age`` field from the source entity and adds it as
         ``current_age`` on the target entity.
       |
       | ``["rename",``
       |   ``["concat", "in-", "_S.key"],``
       |   ``["concat", "out-", "_S.key"]]``
       |
       | Copies the value of the property returned by the first ``concat`` function
         and assigns it to the property returned by the second ``concat`` function.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | *Source entity:*
       | ``{"a": 1,``
       |  ``"x:a": 2}``
       |  ``"xyz:a": 3}``
       |
       | ``["rename", "a", "b"]``
       |
       | Result:
       | ``{ "b": 1.``
       |   ``"x:b": 2,``.
       |   ``"xyz:b": 3}``.
       | Renames the ``a`` property in all namespaces to ``b`` in the same namespace.
         In practice this renames the identifier part of the namespaced identifiers
         from ``a`` to ``b``. If PROPERTY2 only contains the identifier part of
         namespaced identifier, then the identifier part of PROPERTY1 will be renamed to this.
       |
       | ``["rename", "a", "z:b"]``
       |
       | Result:
       | ``{"z:b": [1, 2, 3]}``.
       | Collects all the values in the ``a`` property in all namespaces into
         the ``z:b`` property. If PROPERTY2 contains a fully qualified namespaced
         identifier then all values in PROPERTY1 will be collected into this property.
       |
       | ``["rename", "x:a", "x:b"]``
       |
       | Result:
       | ``{"x:b": 2}``.
       | Renames the ``x:a`` property to ``x:b``.

       .. _`dtl_transform-merge`:

   * - ``merge``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity. If the property already exists, it will be overwritten. This means that
         properties from later value entities win over earlier  ones.
     - | ``["merge", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
       |
       | ``["merge", ["list", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=2`` and ``b=3`` to the target entity. Note that
         ``a=1`` is not added because it gets overwritten with ``a=2`` later.

       .. _`dtl_transform-merge-union`:

   * - ``merge-union``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES copy all the properties of the value onto the
         target entity. If the property already exists on the target entity, add
         the new values as a list of values.
     - | ``["merge-union", "_S.orders"]``
       |
       | Copies the properties of the entities in ``_S.orders`` to the target.
         Merge the property values if the property already exists.
       |
       | ``["merge-union",``
       |   ``["list", {"a": 1}, {"a": 2, "b": 3}]]``
       |
       | Add the properties ``a=[1, 2]`` and ``b=3`` to the target entity.

       .. _dtl_transform-create:
   * - ``create``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES emit them as new entities to the DTLs output
         pipeline.

       | Note that these new entities *must* have an ``_id`` string property.
         Values that are not entities will be ignored.

     - | ``["create", "_S.orders"]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities.
       |
       | ``["create", ["apply", "order", "_S.orders"]]``
       |
       | Emit the orders in the source entity's ``orders`` field as new entities,
         but apply the ``order`` transform to them first.

       .. _dtl_transform-create-child:

   * - ``create-child``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | For each entity in VALUES add it to the ``$children`` property on the
         target entity. Note that the entities *must* have an ``_id`` string property.
         Values that are not entities will be ignored.
       |
       | This function is almost equivalent to:
       |
       | ``["add", "$children",``
       |   ``["union", "_T.$children", ...]]``
       |
       | Note that the ``$children`` property is special. This function should
         really only be used when writing into a ``dataset`` sink.
       |
       | If an entity with a ``$children`` property is written to the ``dataset``
         sink then it will compare it against the value of the ``$children``
         property in the previous version of the entity. It will detect deleted
         entities and add them to the property before storing the entity.
       |
       | Note also that there is an :ref:`emit_children <emit_children_transform>`
         transform that can be used to expand the ``$children`` entities into
         standalone entities.

     - | ``["create-child", "_S.orders"]``
       |
       | Adds the orders in the source entity's ``orders`` field to the "$children" property
         on the target entity.


Expression language
===================

An expression language function is a function that has no side-effects
and returns a single value or a list of values.

Boolean logic
-------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _and_dtl_function:
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

       .. _or_dtl_function:
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

       .. _not_dtl_function:
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

       .. _all_dtl_function:
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
       |    ``["gt", "_.", 2],``
       |    ``["list", 4, 5, 6]]``
       |
       | Returns true because all arguments are greater than 2.
       |
       | ``["all",``
       |    ``["lt", "_.", 2],``
       |    ``["list", 1, 3, 5]]``
       |
       | Returns false because not all arguments are less than 2.

       .. _any_dtl_function:
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
       |    ``["gt", "_.", 5],``
       |    ``["list", 4, 6, 8]]``
       |
       | Returns true because two of the arguments are greater than 5.
       |
       | ``["any",``
       |    ``["lt", "_.", 2],``
       |    ``["list", 6, 7, 8]]``
       |
       | Returns false because none of the arguments are less than 2.

Booleans
--------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _boolean_dtl_function:
   * - ``boolean``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to booleans. If no default value expression
         is given, values that don't parse as boolean values will be silently
         ignored. If not, the evaluated value from the default expression will
         be used as a replacement value. String literals are case insensitive,
         and the supported values are "true" and "false".
       |
     - | ``["boolean", "false"]``
       |
       | Returns one boolean: false.
       |
       | ``["boolean", null]``
       |
       | Returns ``null``.
       |
       | ``["boolean",``
       |   ``["list", "true", "~rhttp://www.example.org/",``
       |     ``"True", false, 1234]]``
       |
       | Returns a list of booleans: [true, true, false]. The URI and integer
         values are ignored.
       |
       | ``["boolean", ["boolean", false],``
       |   ``["list", "true", "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns a list of booleans: [true, false, false, false]. The URI value
         and the string value are replaced with the literal value: false
       |
       | ``["boolean", ["string", "n/a"],``
       |   ``["list", "true", "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns a list of booleans: [true, "n/a", "n/a"]. The URI value and
         the string value are replaced with the literal value "n/a"
       |
       | ``["boolean", ["string", "_."],``
       |   ``["list", "true", "~rhttp://www.example.org/", "False"]]``
       |
       | Returns a list of booleans: [true, "http://www.example.org/", false].
         The URI value is replaced with its string cast.

       .. _is_boolean_dtl_function:
   * - ``is-boolean``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a boolean literal or if
         it is a list, that the first element in the list is a boolean
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
       | Returns true.
       |
       | ``["is-boolean", ["list", "12345", true]]``
       |
       | Returns false.
       |
       | ``["is-boolean", ["list", ["boolean", "FALSE"], 1234]]``
       |
       | Returns true.


Comparisons
-----------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _eq_dtl_function:
   * - ``eq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         lists and compares those lists. Returns ``true`` if the two
         arguments given are equal.
     - | ``["eq", "_S.age", 42]``
       |
       | Returns ``true`` if the source entity's age field is ``42``.
       |
       | ``["eq", "_S.hobbies", ["list", "soccer", "tennis"]]``
       |
       | Returns ``true`` if the hobbies are exactly equal to ``["soccer", "tennis"]``.

       .. WARNING::

          Note that the ``eq`` function serves a dual purpose. It can
          both be used for :ref:`join expressions <joins>` and it can
          be used for :ref:`equality comparisons
          <eq_dtl_function>`. These two are different in that a join
          uses intersection (similar to the ``intersects`` function) and
          the equality comparison is an exact match. Use the
          :ref:`intersects <intersects_dtl_function>` function if you
          want to check for intersection/overlap instead of an exact
          match.

       .. _neq_dtl_function:
   * - ``neq``
     - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns ``false`` if the two
         arguments given are equal.
     - | ``["neq", "_S.age", 42]``
       |
       | The source entity's age field must *not* have the value 42.

       .. _gt_dtl_function:
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

       .. _gte_dtl_function:
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

       .. _lt_dtl_function:
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

       .. _lte_dtl_function:
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

       .. _is_empty_dtl_function:
   * - ``is-empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is 0.
     - | ``["is-empty", "_S.hobbies"]``
       |
       | Returns true if the source entity's ``hobbies`` field is
         empty (has no values).

       .. _is_not_empty_dtl_function:
   * - ``is-not-empty``
     - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is greater than 0.
     - | ``["is-not-empty", "_S.hobbies"]``
       |
       | Returns true if the source entity's ``hobbies`` field is not
         empty (has one or more values).

       .. _is_changed_dtl_function:
   * - ``is-changed``
     - | *Arguments:*
       |   FUNCTION(function-expression{1}),
       |
       | Returns true if the results of evaluating the FUNCTION expression on the current
         version and the previous version of the source entity are different.
       |
       | If the previous version does not exist then the ``is-changed``
       | function returns ``null``. This means that we don't know if it has changed.
       |
       | If either the current or the previous version of the entity
       | has ``_deleted`` set to ``true`` then the ``is-changed``
       | function returns ``true``.
     - | ``["is-changed", "_.name"]``
       |
       | Returns true if the source entity's ``name`` property changed.
       |
       | ``["is-changed", ["list", "_.height", "_.width"]]``
       |
       | Returns true if the source entity's ``height`` or ``width`` properties changed.
       |
       | ``["is-changed", ["-", "_.end", "_.start"]]``
       |
       | Returns true if the source entity's distance between ``start`` and ``end`` changed.


Conditionals
------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _if_dtl_function:
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
         than 42, if not 2 is returned.

       .. _case_eq_dtl_function:
   * - ``case-eq``
     - | *Arguments:*
       |   VALUE(value-expression{1}),
       |   (VALUE_N(value-expression{1},
       |    THEN(value-expression{1}))+,
       |   ELSE(value-expression{0\|1})
       |
       | Returns the first THEN for which VALUE is equal to VALUE_N. If there is no
         match, then ELSE is returned. If there is no ELSE, then ``null`` is returned.
     - | ``["case-eq", "_S.country",``
       |   ``"NO", "Norway",``
       |   ``"SE", "Sweden",``
       |   ``"Other"]``
       |
       |
       | Given then value of ``_S.country``, returns ``"Norway"`` if the value is ``"NO"``
         and ``"Sweden"`` if the value is ``"SE"``, otherwise ``"Other"`` is returned.
       |
       | ``["case-eq", "_S.dialing_code",``
       |   ``45, "DK",``
       |   ``46, "SE",``
       |   ``47, "NO"]``
       |
       |
       | Given the value of ``_S.dialing_code``, returns ``"DK"`` if the value is
         ``45`` and ``"SE"`` if the value  is ``46`` and ``"NO"`` if the value is ``47``,
         otherwise ``null`` is returned.

       .. _case_dtl_function:
   * - ``case``
     - | *Arguments:*
       |   (VALUE(value-expression{1},
       |    THEN(value-expression{1}))+,
       |   ELSE(value-expression{0\|1})
       |
       | Returns the first THEN for which VALUE is true. If there is no
         match, then ELSE is returned. If there is no ELSE, then ``null`` is returned.
     - | ``["case",``
       |   ``["gte", "_S.age", 18], "adult",``
       |   ``["gte", "_S.age", 13], "teenager",``
       |   ``["gte", "_S.age", 2], "toddler",``
       |   ``["lt", "_S.age", 2], "baby",``
       |   ``"unknown"]``
       |
       | Returns ``"adult"`` if the value of ``_S.age`` is greater than or equal to ``18``,
       | or ``"teenager"`` if the value of ``_S.age`` is greater than or equal to ``13``,
       | or ``"toddler"`` if the value of ``_S.age`` is less than ``2``,
       | otherwise ``"unknown"``.

.. _nulls:

Nulls
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _is_null_dtl_function:
   * - ``is-null``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns ``true`` if value is either ``null``, an
         empty list, or a list where the first element in the list is ``null``.
       |
     - | ``["is-null", null]``
       |
       | Returns ``true``.
       |
       | ``["is-null", 1]``
       |
       | Returns ``false``.
       |
       | ``["is-null", ["list"]]``
       |
       | Returns ``true``.
       |
       | ``["is-null", ["list", null]]``
       |
       | Returns ``true``.
       |
       | ``["is-null", ["list", null, 123]]``
       |
       | Returns ``true``. Note that the function only looks at the first value
         in the list.
       |
       | ``["is-null", ["list", 1, "12345"]]``
       |
       | Returns ``false``.

       .. _is_not_null_dtl_function:
   * - ``is-not-null``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns ``false`` if value is either ``null``, an
         empty list, or a list where the first element in the list is ``null``.
       |
     - | ``["is-not-null", null]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", 1]``
       |
       | Returns ``true``.
       |
       | ``["is-not-null", ["list"]]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", ["list", null]]``
       |
       | Returns ``false``.
       |
       | ``["is-not-null", ["list", null, 123]]``
       |
       | Returns ``false``. Note that the function only looks at the first value
         in the list.
       |
       | ``["is-not-null", ["list", 1, "12345"]]``
       |
       | Returns ``true``.

       .. _if_null_dtl_function:
   * - ``if-null``
     - | *Arguments:*
       |   VALUE(value-expression{1})
       |   FALLBACK-VALUE(value-expression{1})
       |
       | If ``is-null`` is false for VALUE then VALUE is returned, otherwise
         FALLBACK-VALUE is returned.
       |
     - | ``["if-null", null, 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", 1, 2]``
       |
       | Returns ``1``.
       |
       | ``["if-null", ["list", null], 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", ["list", null, 123], 2]``
       |
       | Returns ``2``.
       |
       | ``["if-null", ["list", 1, "12345"], 2]``
       |
       | Returns ``[1, "12345"]``.

       .. _coalesce_dtl_function:
   * - ``coalesce``
     - | *Arguments:*
       |   FUNCTION(function-expression{0|1}),
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES that makes the FUNCTION expression
         return a trueish value. The FUNCTION expression argument is optional,
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

Numbers
-------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _integer_dtl_function:
   * - ``integer``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to integers. If no default value expression
         is given, values that don't parse as integers will be silently ignored.
         If not, the evaluated value from the default expression will be used
         as a replacement value.
       |
       | Values that starts with ``"0x"`` are parsed as hexadecimal values in two's complement
         format.
     - | ``["integer", "1"]``
       |
       | Returns one integer: 1.
       |
       | ``["integer",``
       |   ``["list", "1", "~rhttp://www.example.org/", 124.4, 12345]]``
       |
       | Returns a list of integers: [1, 124, 12345]. The URI value is ignored.
       |
       | ``["integer", ["integer", 0],``
       |    ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, 0, 0, 12345]. The URI value and the
         string value are replaced with the literal value 0
       |
       | ``["integer", ["string", "n/a"],``
       |   ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "n/a", "n/a", 12345]. The URI value
         and the string value are replaced with the literal value "n/a"
       |
       | ``["integer", ["string", "_."],``
       |   ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "http://www.example.org/", "10^2", 12345].
         The URI value and the non-integer string value are replaced with the
         their respective string casts.
       |
       | ``["integer", "0x00ff"]``
       |
       | Returns one integer: 255.
       |
       |
       | ``["integer", "0xff"]``
       |
       | Returns one integer: -1.
       |

       .. _is_integer_dtl_function:
   * - ``is-integer``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is an integer literal or
         if it is a list, that the first element in the list is an integer
       |
     - | ``["is-integer", 1]``
       |
       | Returns ``true``.
       |
       | ``["is-integer", "1"]``
       |
       | Returns ``false``.
       |
       | ``["is-integer", ["list", 1, "12345"]]``
       |
       | Returns ``true``.
       |
       | ``["is-integer", ["list", "1", 2]]``
       |
       | Returns ``false``.
       |
       | ``["is-integer", ["list", ["integer", "1"], 2]]``
       |
       | Returns ``true``.

       .. _decimal_dtl_function:
   * - ``decimal``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to decimals (a fractional number with
         unlimited precision). If no default value expression is given,
         values that don't parse as decimal values will be silently ignored.
         If not, the evaluated value from the default expression will be
         used as a replacement value.
       |
     - | ``["decimal", "1.0"]``
       |
       | Returns one decimal value: 1.0
       |
       | ``["decimal",``
       |   ``["list", "1.0", "~rhttp://www.example.org/", 2.2, "one"]]``
       |
       | Returns a list of decimal values: [1.0, 2.2]. The URI and
         non-decimal string value are ignored.
       |
       | ``["decimal", ["boolean", false],``
       |   ``["list", "1.0", 2.1, "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns [1.0, 2.1, false, 124.4, false]. The URI value and the
         non-decimal string value are replaced with the literal value: false
       |
       | ``["decimal", ["string", "n/a"],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns [1.0, 2.0, "n/a", 124.4]. The URI value is replaced with the
       | literal value "n/a".
       |
       | ``["decimal", ["string", "_."],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "2.5"]]``
       |
       | Returns [1.0, 2.0, "http://www.example.org/", 2.5]. The URI value
         is replaced with its string cast.

       .. _is_decimal_dtl_function:
   * - ``is-decimal``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a decimal literal or
         if it is a list, that the first element in the list is a decimal
       |
     - | ``["is-decimal", 1.0]``
       |
       | Returns false (it is a float literal).
       |
       | ``["is-decimal", ["decimal", "1.23"]]``
       |
       | Returns true.
       |
       | ``["is-decimal", 1]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", 1.0, "12345"]]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", "1.0", 2.0]]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", ["decimal", "-1.0"], 1234]]``
       |
       | Returns true.

       .. _float_dtl_function:
   * - ``float``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to floats (a  IEEE 754 binary 64 format).
         if no default value expression is given,
         values that don't parse as float values will be silently ignored.
         If not, the evaluated value from the default expression will be
         used as a replacement value. Note that if you cast decimals to floats
         you can lose precision.
       |
     - | ``["float", "1.0"]``
       |
       | Returns one float value: 1.0
       |
       | ``["float",``
       |   ``["list", "1.0", "~rhttp://www.example.org/", 2.2, "one"]]``
       |
       | Returns a list of float values: [1.0, 2.2]. The URI and
         non-numeric string value are ignored.
       |
       | ``["float", ["boolean", false],``
       |   ``["list", "1.0", 2.1, "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns [1.0, 2.1, false, 124.4, false]. The URI value and the
         non-numeric string value are replaced with the literal value: false
       |
       | ``["float", ["string", "n/a"],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns [1.0, 2.0, "n/a", 124.4]. The URI value is replaced with the
       | literal value "n/a".
       |
       | ``["float", ["string", "_."],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "2.5"]]``
       |
       | Returns [1.0, 2.0, "http://www.example.org/", 2.5]. The URI value
         is replaced with its string cast.

       .. _is_float_dtl_function:
   * - ``is-float``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a float literal or
         if it is a list, that the first element in the list is a float value
       |
     - | ``["is-float", 1.0]``
       |
       | Returns true.
       |
       | ``["is-float", ["decimal", "1.23"]]``
       |
       | Returns false (it is a decimal literal).
       |
       | ``["is-float", 1]``
       |
       | Returns false.
       |
       | ``["is-float", ["list", 1.0, "12345"]]``
       |
       | Returns true.
       |
       | ``["is-float", ["list", "1.0", 2.0]]``
       |
       | Returns false.
       |
       | ``["is-float", ["list", ["decimal", "-1.0"], 123.4]]``
       |
       | Returns false.

       .. _hex_dtl_function:
   * - ``hex``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to a string containing an hexadecimal representation of the value
         in two's complement format.
       | Values that don't parse as integers will be silently ignored.
     - | ``["hex", 1]``
       |
       | Returns one string: ``"0x01"``.
       |
       | ``["hex", 255]``
       |
       | Returns one string: ``"0x00ff"``.
       |
       | ``["hex", -1]``
       |
       | Returns one string: ``"0xff"``.
       |
       | ``["hex",``
       |   ``["list", 1, "~rhttp://www.example.org/", 124.4, 12345]]``
       |
       | Returns a list of strings: ["0x1", "0x3039"]. The URI value and the float value are ignored.


Date and time
-------------

A general note on timezone conversion functions: Sesam relies on tabulated historical data for daylight
saving information for the various timezones. This data gets corrected or supplemented from time to time which means
that the result of an explicit or implicit timezone conversion operation can change over time.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _now_dtl_function:
   * - ``now``
     - | *Arguments:*
       |   NONE(value-expression{0})
       |
       | Returns the current time as a datetime value.
       |
     - | ``["now"]``
       |
       | Returns the current time as a datetime value, e.g.
         "~t2016-05-13T14:32:00.431Z".

       .. WARNING::

          This function is non-deterministic and will return a
          different value every time it is evaluated. Be aware that if
          the pipe is rewound or reset then it will produce a
          different output. Dependency tracking will also have a
          similar effect as to produce a different value when entities
          are reprocessed.

          *Use this function with care and make sure
          that you are aware of the consequences of reprocessing
          entities.*

       .. _datetime_dtl_function:
   * - ``datetime``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to datetime values. If no default value
         expression is given, values that don't parse as datetime values will
         be silently ignored. If not, the evaluated value from the default
         expression will be used as a replacement value.
       |
     - | ``["datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z".
       |
       | ``["datetime", 1438076760123450000]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z". Note that
         integer values are treated as nanoseconds since "1970-01-01T00:00:00Z".
         Negative integer values are interpreted as nanoseconds before that.
       |
       | ``["datetime", ["list", ["now"], ["now"], "hello"]]``
       |
       | Returns a list of two datetime values which both are the current time.
         The "hello" string is ignored.
       |
       | ``["datetime", ["now"], "hello"]``
       |
       | Returns the current time as a datetime value, e.g.
         "~t2016-05-13T14:32:00.431Z". Note that this was created by the
         function argument.

       .. _datetime_parse_dtl_function:
   * - ``datetime-parse``
     - | *Arguments:*
       |   TIMEZONE_NAME(string{0|1})
       |   FORMATSTRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to datetime values. The values must be strings
         matching the format string given. Any values that don't parse as datetime values will
         be silently ignored.
       |
       | The timezone name defaults to "UTC". The datetime string will be interpreted
         as being in this timezone. Click :ref:`here<supported_timezones>` to
         see the list of supported timezones.
       |
       |
       | The supported formatting tokens are:
       |
       |   %d - day of the month (01 to 31)
       |   %e - day of the month (1 to 31)
       |   %H - hour, using a 24-hour clock (00 to 23)
       |   %I - hour, using a 12-hour clock (01 to 12)
       |   %m - month (01 to 12)
       |   %M - minute
       |   %p - either am or pm according to the given time value
       |   %S - second
       |   %f - microsecond as a decimal number, zero-padded on the left
       |   %y - year without a century (range 00 to 99)
       |   %Y - year including the century
       |   %z - UTC offset in the form +HHMM, -HHMM, +HH:MM or -HH:MM. If present, this token must be the last token in the format string.
       |   %% - a literal % character
       |

       .. NOTE::

          When using ``%y``, then the two digits are converted
          according to the POSIX and ISO C standards; 00-68 are mapped
          to the years 2000-2068 and 69-99 are mapped to the years 1969-1999.
     - | ``["datetime-parse",``
       |   ``"%Y-%m-%dT%H:%M:%S.%fZ",``
       |   ``"2015-07-28T09:46:00.12345Z"]``
       |
       | Returns one datetime value: "~t2015-07-28T09:46:00.12345Z".
       |
       | ``["datetime-parse",``
       |   ``"%Y-%m-%dT%H:%M:%S%z",``
       |   ``"2015-07-28T09:46:00+0200"]``
       |
       | Returns one datetime value: "~t2015-07-28T07:46:00Z".
       |
       | ``["datetime-parse", "%d.%m.%Y", "28.07.2015"]``
       |
       | Returns one datetime value: "~t2015-07-28T00:00:00Z".
       |
       | ``["datetime-parse",``
       |   ``"%d.%m.%Y", ["list", "28.07.2015", "01.01.1970"]``
       |
       | Returns two datetime values: ["~t2015-07-28T00:00:00Z", "~t1970-01-01T00:00:00Z"]
       |
       | ``["datetime-parse", "Europe/Oslo"``
       |   ``"%Y-%m-%dT%H:%M:%S",``
       |   ``"2018-08-18T12:39:01"]``
       |
       | Returns one datetime value: "~t2018-08-08T10:39:01Z".

       .. _datetime_format_dtl_function:
   * - ``datetime-format``
     - | *Arguments:*
       |   TIMEZONE_NAME(string{0|1})
       |   FORMATSTRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input datetime values to strings. The strings will be formattet according to the format string.
         Any values that aren't datetime values will be silently ignored. Note that precision loss is possible since
         ``datetime`` objects internally have nanoseconds precision while the formatted strings will only support
         microseconds (using the seconds fraction token ``%f``).
       |
       | The timezone name defaults to "UTC". The datetime value will be translated to this timezone before it
         is formatted. Click :ref:`here<supported_timezones>` to see the list of supported timezones.

       .. NOTE::

          When using ``%y``, then the years are converted
          according to the POSIX and ISO C standards; the years 2000-2068 are mapped to 00-68
          and the years 1969-1999 are mapped to 69-99. For years outside of that range the
          last two digits are used.
     - | ``["datetime-format", "%Y-%m-%dT%H:%M:%SZ",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one string: "2015-07-28T00:00:00Z".
       |
       | ``["datetime-format",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 12:39:01".
       |
       | ``["datetime-format", "Europe/Oslo",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 14:39:01".
       |
       | ``["datetime-format", "Europe/Oslo",``
       |   ``"%Y-%m-%d %H:%M:%S",``
       |   ``["datetime-parse", "Europe/Oslo",``
       |     ``"%Y-%m-%dT%H:%M:%S",``
       |     ``"2018-08-18T12:39:01"]]``
       |
       | Returns one string: "2018-08-18 12:39:01".
       |
       | See ``datetime-parse`` for the supported tokens in the format string.

       .. _datetime_plus_dtl_function:
   * - ``datetime-plus``
     - | *Arguments:*
       |   DATEPART(string{1})
       |   VALUE(integer{1})
       |   VALUES(value-expression{1})
       |
       | Adds a fixed ``VALUE`` number (positive or negative) of ``DATEPART`` values to the the input values,
       | producing new datetime objects. ``DATEPART`` can be one of the following values:
       |
       |   ``year``
       |   ``month``
       |   ``week``
       |   ``day``
       |   ``hour``
       |   ``minute``
       |   ``second``
       |   ``millisecond``
       |   ``microsecond``
       |   ``nanosecond``
       |

     - | ``["datetime-plus", "day", 1, ["datetime-parse",``
       |   ``"%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one datetime value: ``"~t2015-07-29T00:00:00Z"``.
       |
       | ``["datetime-plus", "hour", -1, ["datetime-parse",``
       |   ``"%Y-%m-%d", "2016-03-01"]]``
       |
       | Returns one datetime value: ``"~t2016-02-29T23:00:00Z"``.
       |
       | ``["datetime-plus", "year", 1,``
       |     ``["list",``
       |         ``["datetime-parse",``
       |           ``"%Y-%m-%d", "1971-01-01"],``
       |         ``["datetime-parse",``
       |           ``"%Y-%m-%d", "1950-06-01"]]``
       |
       | Returns two datetime values: ``["~t1972-01-01T00:00:00Z",``
       |                               ``"~t1951-06-01T00:00:00Z"]``.

       .. _datetime_diff_dtl_function:
   * - ``datetime-diff``
     - | *Arguments:*
       |   DATEPART(string{1})
       |   STARTDATE(value-expression{1})
       |   ENDDATE(value-expression{1})
       |
       | Computes the positive or negative number of ``DATEPART`` values between the end and start date input values
       | ``DATEPART`` can be one of the following values:
       |
       |   ``year``
       |   ``month``
       |   ``week``
       |   ``day``
       |   ``hour``
       |   ``minute``
       |   ``second``
       |   ``millisecond``
       |   ``microsecond``
       |   ``nanosecond``
       |
       | Note that the return values are rounded downwards to the nearest (absolute) integer value, i.e. +-11 months is
       | 0 years and +-8 days is +-1 week.

       |
     - | ``["datetime-diff", "day",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-29"]]``
       |
       | Returns one integer value: -1
       |
       | ``["datetime-diff", "day",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-29"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-07-28"]]``
       |
       | Returns one integer value: 1
       |
       | ``["datetime-diff", "year",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-03-02"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2016-07-29"]]``
       |
       | Returns: -1
       |
       | ``["datetime-diff", "month",``
       |   ``["datetime-parse", "%Y-%m-%d", "2015-03-02"],``
       |   ``["datetime-parse", "%Y-%m-%d", "2016-07-29"]]``
       |
       | Returns: -16

       .. _datetime_shift_dtl_function:
   * - ``datetime-shift``
     - | *Arguments:*
       |   FROM_TIMEZONE(string{1})
       |   TO_TIMEZONE(string{1})
       |   VALUES(value-expression{1})
       |
       | Shifts all the input datetime values from one timezone to another timezone. Any values that aren't datetime
         values will be silently ignored. Click :ref:`here<supported_timezones>` to see the list of supported timezones.
       | Internally, SESAM stores datetimes as UTC, and timezone converting is usually done automatically by the datasources.
         Sometimes, though, there is need to explicitly convert a timezone in a non-UTC timezone into some other timezone; An
         example is if you are reading from a CSV-file where one of the columns is a date-string with no explicit timezone information,
         but where you know that the dates are in some non-UTC timezone. In this case you could use the datetime-shift function
         to convert the dates from the CSV-file into correct UTC datetimes. |
     - | ``["datetime-shift", "Europe/Oslo", "UTC",``
       |     ``["datetime-parse",``
       |         ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"]]``
       |
       | Returns one datetime value: ``"~t2015-07-28T07:46:00Z"``.
       | ``["datetime-shift", "UTC", "Europe/Oslo",``
       |     ``["datetime-parse",``
       |         ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"]]``
       |
       | Returns one datetime value: ``"~t2015-07-28T11:46:00Z"``.
       |
       | ``["datetime-shift", "Europe/Oslo", "UTC",``
       |     ``["list",``
       |         ``["datetime-parse",``
       |           ``"%Y/%m/%d %H:%M", "2015/07/28 09:46"],``
       |         ``["datetime-parse",``
       |           ``"%Y/%m/%d %H:%M", "2015/07/28 04:46"]]``
       |
       | Returns two datetime values: ``["~t2015-07-28T07:46:00Z",``
       |                               ``"~t2015-07-28T02:46:00Z"]``.

       .. _is_datetime_dtl_function:
   * - ``is-datetime``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a datetime value or
         if it is a list, that the first element in the list is a datetime value.
       |
     - | ``["is-datetime", ["now"]]``
       |
       | Returns true.
       |
       | ``["is-datetime",``
       |   ``["datetime", "2015-07-28T09:46:00.12345Z"]]``
       |
       | Returns true.
       |
       | ``["is-datetime", "2015-07-28T09:46:00.12345Z"]``
       |
       | Returns false.
       |
       | ``["is-datetime", ["list", "1", 2]]``
       |
       | Returns false.

Strings
-------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _string_dtl_function:
   * - ``string``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to strings.

       .. NOTE::

          Complex types like list and dict are JSON encoded (no transit encoding).
          Bytes are decoded to strings using ``utf-8`` encoding.
     - | ``["string", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["string", "hello"]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["string", null]``
       |
       | Returns ``null``.
       |
       | ``["string",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["abc", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"http://www.example.org/", "124.4", "12345"]``.

       .. _is_string_dtl_function:
   * - ``is-string``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a string literal or if
         it is a list, that the first element
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

       .. _upper_dtl_function:
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

       .. _lower_dtl_function:
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

       .. _length_dtl_function:
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

       .. _concat_dtl_function:
   * - ``concat``
     - | *Arguments:*
       |   VALUES(value-expression{>1})
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
       |
       | ``["concat", "Hello ", "_S.name", "!"]``
       |
       | Returns ``"Hello John!"`` if the ``name`` property is ``John``.
       |
       | ``["concat", "a", ["list", "b", "c"], "d", 123, ["list", "!"]]``
       |
       | Returns ``"abcd!"``.
       |
       | ``["concat", 123, 3.14]``
       |
       | Returns ``""``, because non-string values are ignored.

       .. _join_dtl_function:
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

       .. _split_dtl_function:
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
       | ``["split", "", "abc"]``
       |
       | Returns ``["a", "b", "c"]``.
       | ``["split", "", ["list", "ab", "cd", "e"]]``
       |
       | Returns ``["a", "b", "c", "d", "e"]``.
       |
       | ``["split", "-", ["list", "a-b", "c-d", "e"]]``
       |
       | Returns ``["a", "b", "c", "d", "e"]``.
       |
       | ``["split", "-", "_S.uuid"]``
       |
       | Returns a list of strings of the source entity's tags separated by dashes.

       .. _strip_dtl_function:
   * - ``strip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from both sides. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["strip", ["list", " ab ", "cd ", "ef"]]``
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
       | ``["strip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123", "456"]``.

       .. _lstrip_dtl_function:
   * - ``lstrip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the left side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["lstrip", ["list", " ab ", "cd ", "ef"]]``
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
       | ``["lstrip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123xyx", "456yx"]``.

       .. _rstrip_dtl_function:
   * - ``rstrip``
     - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the right side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["rstrip", ["list", " ab ", "cd ", "ef"]]``
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
       | ``["rstrip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123", "xy456"]``.

       .. _ljust_dtl_function:
   * - ``ljust``
     - | *Arguments:*
       |   WIDTH(integer-expression{1})
       |   FILL_CHARACTER(character-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns a left-justified version of its input strings. The WIDTH defines the minimum
         length of the returned strings. If the input strings are longer than WIDTH, then the
         input string is returned as-is. If the input string is shorter than WIDTH then it is
         justified to the left using the FILL_CHARACTER.
       |
       | Non-string values are ignored. If the WIDTH is not an integer or FILL_CHARACTER is
         not a single character then the function returns ``null``.
     - | ``["ljust", 10, "0", "123"]``
       |
       | Returns ``"1230000000"``.
       |
       | ``["ljust", 5, " ", ["list", "abc", "def", "ghijklm"]]``
       |
       | Returns ``["abc  ", "def  ", "ghijklm"]``.

       .. _rjust_dtl_function:
   * - ``rjust``
     - | *Arguments:*
       |   WIDTH(integer-expression{1})
       |   FILL_CHARACTER(character-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns a right-justified version of its input strings. The WIDTH defines the minimum
         length of the returned strings. If the input strings are longer than WIDTH, then the
         input string is returned as-is. If the input string is shorter than WIDTH then it is
         justified to the right using the FILL_CHARACTER.
       |
       | Non-string values are ignored. If the WIDTH is not an integer or FILL_CHARACTER is
         not a single character then the function returns ``null``.
     - | ``["rjust", 10, "0", "123"]``
       |
       | Returns ``"0000000123"``.
       |
       | ``["rjust", 5, " ", ["list", "abc", "def", "ghijklm"]]``
       |
       | Returns ``["  abc", "  def", "ghijklm"]``.

       .. _replace_dtl_function:
   * - ``replace``
     - | *Arguments:*
       |   (REPLACEMENTS(dict{1}) or
            (OLD_STRING(string{1})
             NEW_STRING(string{1})))
       |   VALUES(value-expression{1})
       |
       | Replaces occurrences of OLD_STRING with NEW_STRING in VALUES, or replaces the keys
         in the REPLACEMENT dict with the respective values. Non-string values
         are ignored.
     - | ``["replace", "http://", "https://",``
       |   ``"http://www.sesam.io/"]``
       |
       | Returns ``"https://www.sesam.io/"``.
       |
       | ``["replace", ":", ".", "_S.date"]]``
       |
       | Returns a date string where the colon has been replaced by a period.
       |
       | ``["replace", {"Hello": "HELLO", "world": "WORLD"}, "Hello world!"]]``
       |
       | Returns ``"HELLO WORLD!"``.
       |
       | ``["replace", ["dict", "a", "A", "b", "B"], "abc"]]``
       |
       | Returns ``"ABc"``.

       .. _substring_dtl_function:
   * - ``substring``
     - | *Arguments:*
       |   START_INDEX(integer{1})
       |   END_INDEX(integer{0|1})
       |   VALUES(value-expression{1})
       |
       | Extracts the substring between START_INDEX and END_INDEX. If the indexes are negative they start from the end.

     - | ``["substring", 2, 4, "abcdef"]``
       |
       | Returns ``"cd"``.
       |
       | ``["substring", 2, "abcdef"]``
       |
       | Returns ``"cdef"``.
       |
       | ``["substring", -3, -1, "abcdef"]``
       |
       | Returns ``"de"``.

       .. _matches_dtl_function:
   * - ``matches``
     - | *Arguments:*
       |   PATTERN(string{1})
       |   VALUES(value-expression{1})
       |
       | Returns true if all the values in VALUES match the pattern in PATTERN. The '*' and '?'
         wildcard characters can be used. Non-string values are not matched and will cause the
         function to return false. If PATTERN contains multiple string values then only the
         first one is used.
     - | ``["matches", "a*p*a", ["list", "alpha", "alpaca"]]``
       |
       | Returns ``true``.
       |
       | ``["matches", "*_sport", "_S.tags"]``
       |
       | Returns ``true``, unless ``_S.tags`` is empty or ``null``, if all the tags that have a "_sport" suffix.
       |
       | ``["matches", "*", null]``
       |
       | Returns ``false``.
       |
       | ``["matches", "*", ["list"]]``
       |
       | Returns ``false``.

Bytes
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _bytes_dtl_function:
   * - ``bytes``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input string values to bytes using ``utf-8`` encoding.
       |
     - | ``["bytes", "abc"]``
       |
       | Returns one bytes object: ``~bYWJj``.

       .. _is_bytes_dtl_function:
   * - ``is-bytes``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a bytes literal or value or if
         it is a list, that the first element in the list is a bytes type value or literal
       |
     - | ``["is-bytes", ["bytes", "abc"]]``
       |
       | Returns true.
       |
       | ``["is-bytes", "~bYWJj"]``
       |
       | Returns true.
       |
       | ``["is-bytes", "some-string"]``
       |
       | Returns false.
       |
       | ``["is-bytes", ["list", "~bYWJj", "12345"]]``
       |
       | Returns true.
       |
       | ``["is-bytes", ["list", "12345", "~bYWJj"]]]``
       |
       | Returns false.
       |

       .. _base64_encode_dtl_function:
   * - ``base64-encode``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the base64 encoded version of its input bytes.
         Non-bytes values are ignored.
     - | ``["base64-encode", ["bytes", "abc"]]``
       |
       | Returns ``"YWJj"``.
       |
       | ``["base64-encode", ["list", 1, ["bytes", "abc"], 2, ["bytes", "def"], 3]]``
       |
       | Returns ``["YWJj", "ZGVm"]``.
       |


       .. _base64_decode_dtl_function:
   * - ``base64-decode``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the base64 decoded version of its input strings.
         Non-string values and non-base64 encoded values are ignored.
     - | ``["base64-decode", "YWJj"]``
       |
       | Returns ``"~babc"``.
       |
       | ``["base64-decode", ["list", 1, "YWJj", 2, "ZGVm", 3]]``
       |
       | Returns ``["~bYWJj", "~bZGVm"]``.
       |
       | (Note that the JSON string representation of a bytes object is represented as a base64 encoded string, hence
       | the similar looking output and input)


Encryption
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _encrypt_dtl_function:
   * - ``encrypt``
     - | *Arguments:*
       |   KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the VALUES using the key in KEY
       | the data wil be encrypted using a symmetric Fernet algorithm with the key as the password. Note that this
       | function by itself does not offer an end-to-end secure system of encryption
       | as the key is stored along with the encrypted data. This applies even when using a ``$SECRET(secret key)`` via
       | the secrets manager.
       |
     - | ``["encrypt", "secret", ["list", "a", "b", "c"]]``
       |
       | Returns an encrypted bytes object.

       .. _encrypt_pki_dtl_function:
   * - ``encrypt-pki``
     - | *Arguments:*
       |   PUBLIC_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the strings in VALUES using the public key in PUBLIC_KEY
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings so
       | if you want to encrypt some property that is not a string or a list of strings,
       | you must convert it this form first, for example using the ``json`` or ``json-transit`` serialize functions.
       |
       | The PUBLIC_KEY parameter must be a RSA public key in PEM format (PKCSv8, which starts with the header
       | "-----BEGIN PUBLIC KEY-----"). The input is encrypted using an asymmetric RSA 2048 bits
       | encryption algorithm - to decrypt the data you must use the corresponding private key. See ``decrypt-pki``.
       |
       | Note that this function can't encrypt large strings, it is intended to encrypt shorter passphrases or similar
       | identifiers. Use the ``encrypt-pgp`` function instead if you need to encrypt larger blocks of data.
       |
     - | ``["encrypt-pki", "RSA_PEM_public_key", ["json-transit", ["list", "a", "b", "c"]]]``
       |
       | Returns a list of bytes objects: ``["~bDHAERS..", "~bHDURKSS..", "~bXYSERS.."]``
       |
       | ``["encrypt-pki", "RSA_PEM_public_key", "secret-passphrase"]``
       |
       | Returns a single bytes object: ``"~bDHAERS.."``
       |
       | ``["encrypt-pki", "$SECRET(key-secret-name)", "$SECRET(secret-passphrase-name)"]``
       |
       | Returns a single bytes object: ``"~bDHAERS.."``

       .. _encrypt_pgp_dtl_function:
   * - ``encrypt-pgp``
     - | *Arguments:*
       |   PUBLIC_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Encrypts the strings in VALUES in OpenPGP format using the PGP public key in PUBLIC_KEY
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings so
       | if you want to encrypt some property that is not a string or a list of strings,
       | you must convert it this form first, for example using the ``json`` or ``json-transit`` serialize functions.
       |
       | The PUBLIC_KEY parameter must be a PGP public key which starts with the header
       | "-----BEGIN PGP PUBLIC KEY-----"). The resulting encrypted data is stored in OpenPGP form (RFC4880, https://tools.ietf.org/html/rfc4880)
       | To decrypt the data you must use the corresponding private key and associated password. See ``decrypt-pgp``.
       |
       |
     - | ``["encrypt-pgp", "OpenPGP_public_key", ["json-transit", ["list", "a", "b", "c"]]]``
       |
       | Returns a list of strings in OpenPGP ASCII format:
       | ``["----BEGIN PGP MESSAGE..", "----BEGIN PGP MESSAGE..", "----BEGIN PGP MESSAGE.."]``
       |
       | ``["encrypt-pgp", "OpenPGP_public_key", "secret-message"]``
       |
       | Returns a single OpenPGP message in ASCII format: ``"----BEGIN PGP MESSAGE.."``
       |
       | ``["encrypt-pgp", "$SECRET(key-secret-name)", "secret-message"]``
       |
       | Returns a single OpenPGP message in ASCII format: ``"----BEGIN PGP MESSAGE.."``

       .. _decrypt_dtl_function:
   * - ``decrypt``
     - | *Arguments:*
       |   KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | The key is assumed to be a matching password used by a previous ``encrypt``
       | function, i.e. it is symmetric with ``encrypt`` if the same key is used:
       |
     - | ``["decrypt", "secret", ["encrypt", "secret", ["list", "a", "b", "c"]]]``
       |
       | Returns ``["a", "b", "c"]``
       |
       | ``["decrypt", "$SECRET(secret-name)", ["encrypt", "$SECRET(secret-name)", ["list", "a", "b", "c"]]]``
       |
       | Returns ``["a", "b", "c"]``
       |

       .. _decrypt_pki_dtl_function:
   * - ``decrypt-pki``
     - | *Arguments:*
       |   PRIVATE_KEY(string{1})
       |   VALUES(value-expression{1})
       |
       | Decrypts the bytes objects in VALUES using the private key in PRIVATE_KEY.
       |
       | Note that this function requires the VALUES parameter to either be a single bytes object or a list of bytes
       | objects.
       |
       | The PRIVATE_KEY parameter must be a RSA private key in PEM format (PKSv8, which starts with the header
       | "-----BEGIN RSA PRIVATE KEY-----"). The bytes data in VALUE is then decrypted to a string using the asymmetric
       | RSA 2048 bits algorithm - the data must have been encrypted with the corresponding public key. If the data
       | is encoded as a string, it must be cast (for example using ``datetime-parse``) or decoded using an appropriate
       | function such as ``json-parse`` or ``json-transit-parse``.
       |
     - | ``["json-transit-parse",``
       |    ``["decrypt-pki", "-----BEGIN RSA PRIVATE KEY-----..-----END RSA PRIVATE KEY-----",``
       |       ``["encrypt-pki", "-----BEGIN PUBLIC KEY-----..-----END PUBLIC KEY-----",``
       |           ``["json-transit", ["list", ["list", "a", "b", "c"]]]]]``

       | Returns ``["a", "b", "c"]``
       |
       | ``["json-transit-parse",``
       |    ``["decrypt-pki", "$SECRET(private-key-name)",``
       |       ``["encrypt-pki", "-----BEGIN PUBLIC KEY-----..-----END PUBLIC KEY-----",``
       |           ``["json-transit", ["list", ["list", "a", "b", "c"]]]]]``

       | Returns ``["a", "b", "c"]``
       |

       .. _decrypt_pgp_dtl_function:
   * - ``decrypt-pgp``
     - | *Arguments:*
       |   PRIVATE_KEY(string{1})
       |   PASSPHRASE(string{1})
       |   VALUES(value-expression{1})
       |
       | Decrypts the strings in VALUES in OpenPGP format using the PGP private key in PRIVATE_KEY and the password in
       | PASSPHRASE.
       |
       | Note that this function requires the VALUES parameter to either be a string or a list of strings in OpenPGP
       | message format (these are ASCII strings starting with the header "----BEGIN PGP MESSAGE..", see RFC4880,
       | https://tools.ietf.org/html/rfc4880).
       |
       | The PRIVATE_KEY parameter must be a PGP private key which starts with the header
       | "-----BEGIN PGP PRIVATE KEY-----") and the password in PASSPHRASE must match this key so it can be unlocked.
       |
     - | ``["decrypt-pgp", "-----BEGIN PGP PRIVATE KEY..", "valid-password",``
       |     ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", ["list", "data", "data2"]]]``
       |
       | Returns a list: ``["data", "data2"]``
       |
       | ``["decrypt-pgp", "-----BEGIN PGP PRIVATE KEY..", "valid-password",``
       |    ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", "secret message"]]``
       |
       | Returns a string: ``"secret message"``
       |
       | ``["decrypt-pgp", "$SECRET(private-key-name)", "$SECRET(password-name)",``
       |    ``["encrypt-pgp", "-----BEGIN PGP PUBLIC KEY..", "secret message"]]``
       |
       | Returns a string: ``"secret message"``

JSON
----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _json_dtl_function:
   * - ``json``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to JSON strings (no transit encoding).
         The keys of dicts are sorted lexically.
     - | ``["json", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["json", "hello"]``
       |
       | Returns one string: ``"\"hello\""``.
       |
       | ``["json",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["\"abc\"", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"http://www.example.org/", "124.4", "12345"]``.

       .. _json_transit_dtl_function:
   * - ``json-transit``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to transit encoded JSON strings.
         The keys of dicts are sorted lexically. This function behaves like
         the ``json`` function, except that it transit encodes values.
     - | ``["json-transit", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["json-transit", "hello"]``
       |
       | Returns one string: ``"\"hello\""``.
       |
       | ``["json-transit",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["\"abc\"", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"~rhttp://www.example.org/", "124.4", "12345"]``.

       .. _json_parse_dtl_function:
   * - ``json-parse``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Parses all input values as JSON strings (no transit decoding).
       |
       | If no default value expression is given, then invalid values that don't
         parse as valid JSON will be silently ignored. If not, the evaluated value
         from the default expression will be used as a replacement value.

     - | ``["json-parse", "1"]``
       |
       | Returns one number: ``1``.
       |
       | ``["json-parse", "\"hello\""]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["is-uri", ["json-parse",``
       |   ``"\"~rhttp://www.example.org/\""]]``
       |
       | Returns ``false``.
       |
       | ``["json-parse", "{\"a\": 1, \"b\": 2}"``
       |
       | Returns a dictionary: ``{"a": 1, "b": 2}",``
       |
       | ``["json-parse", "hello"]``
       |
       | Returns ``null`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-parse",``
       |   ``["list", "hello", "123", "null",``
       |     ``"\"abc\"", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``[123, null, "abc", "~rhttp://example.org/"]``. Note that ``null``
         is a valid JSON expression, so ``null`` is included in the result list. Note
         also that ``"~rhttp://www.example.org/"`` is not parsed as a URI since we don't do
         transit decoding here.
       |
       | ``["json-parse", "no-value", "hello"]``
       |
       | Returns ``"no-value"`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-parse", "no-value", "null"]``
       |
       | Returns ``null`` because ``"null"`` is a valid JSON string.

       .. _json_transit_parse_dtl_function:
   * - ``json-transit-parse``
     - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Parses all input values as transit-encoded JSON strings.
       |
       | If no default value expression is given, then invalid values that don't
         parse as valid JSON will be silently ignored. If not, the evaluated value
         from the default expression will be used as a replacement value.
       |
       | This function behaves like
         the ``json-parse`` function, except that it transit decodes values.
     - | ``["json-transit-parse", "1"]``
       |
       | Returns one number: ``1``.
       |
       | ``["json-transit-parse", "\"hello\""]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["is-uri", ["json-transit-parse",``
       |   ``"\"~rhttp://www.example.org/\""]]``
       |
       | Returns ``true``.
       |
       | ``["json-transit-parse", "hello"]``
       |
       | Returns ``null`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-transit-parse",``
       |   ``["list", "hello", "123", "null",``
       |     ``"\"abc\"", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``[123, null, "abc", "~rhttp://example.org/"]``. Note that ``null``
         is a valid JSON expression, so ``null`` is included in the result list. Note
         also that "~rhttp://www.example.org/" is parsed as a URI since we are
         doing transit decoding.
       |
       | ``["json-transit-parse",``
       |   ``"no-value", "~rhttp://example.org/"]``
       |
       | Returns ``"no-value"`` because ``~rhttp://example.org/`` is not
         a valid JSON string.
       |
       | ``["is-uri",``
       |   ``["json-transit-parse",``
       |     ``"no-value", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``true`` because ``"\"~rhttp://example.org/\""`` is a valid JSON string
         and the return value is a URI.

URIs
----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _uri_dtl_function:
   * - ``uri``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates input values to URIs. Only strings in VALUES will be
         cast to URIs. Note that *no* URI escaping is done on the strings.
     - | ``["uri", "http://www.example.org/"]``
       |
       | Returns one URI.
       |
       | ``["uri",``
       |    ``["list", "http://www.example.org/",``
       |       ``"http://www.sesam.io/", 12345]]``
       |
       | Returns a list of two URIs. The number is silently ignored because
         it is not a string.

       .. _is_uri_dtl_function:
   * - ``is-uri``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a URI literal, or if it is
         a list, that the first element in the list is a URI.
     - | ``["is-uri", ["uri", "foo:bar"]]``
       |
       | Returns ``true``.
       |
       | ``["is-uri", "foo:bar"]``
       |
       | Returns ``false``.
       |
       | ``["is-uri", ["list", ["uri", "foo:bar"], 12345]]``
       |
       | Returns ``true``.
       |
       | ``["is-uri", ["list", 1, ["uri", "foo:bar"]]]``
       |
       | Returns ``false``.

       .. _url_quote_dtl_function:
   * - ``url-quote``
     - | *Arguments:*
       |   SAFE_CHARS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns the URL quoted versions of any string or list of strings in the
         argument list. Any non-strings are ignored and is not returned in the
         result. Returns either a single string (if the input is a single
         string literal) or a list (of strings).
       |
       | If you want some ASCII characters to not be encoded, e.g. the slash character ``/``,
         then specify the ``SAFE_CHARS`` argument. The default value is "". The ``SAFE_CHARS``
         argument must be a string that contains zero or more ASCII characters that should
         not be encoded. Note that this only is applicable for ASCII characters.
     - | ``["url-quote", "/foo bar/baz"]``
       |
       | Returns ``%2Ffoo%20bar%2Fbaz``. Note that the ``/`` characters have been encoded.
         To avoid this you can add the SAFE_CHARS argument:
       |
       | ``["url-quote", "/", "/foo bar/baz"]``
       |
       | Returns ``/foo%20bar/baz``.
       |
       | ``["url-quote",``
       |   ``["list", "å", 1, 2,``
       |     ``["uri", "http://example.com"], "foo bar"]]``
       |
       | Returns ``["%C3%A5", "foo%20bar]``.

       .. _url_unquote_dtl_function:
   * - ``url-unquote``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the URL unquoted versions of any string or list of strings in the
         argument list. Any non-strings are ignored and is not returned in the
         result. Returns either a single string (if the input is a single
         string literal) or a list (of strings).
       |
     - | ``["url-unquote", "%2Ffoo%20bar%2Fbaz"]``
       |
       | Returns ``/foo bar/baz``.
       |
       | ``["url-quote",``
       |   ``["list", 1, "%C3%A5", ["uri", "http://example.com"], "foo%20bar"]``
       |
       | Returns ``["å", "foo bar"]``.

UUIDs
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _uuid_dtl_function:
   * - ``uuid``
     - | *Arguments:*
       |   VALUES(value-expression{0|1})
       |
       | Create a new UUID object (version 4 ). It can optionally cast a single string or list of string UUID representations to
         UUID objects. Any input that can't be cast to a UUID object will be ignored.
       |
     - | ``["uuid"]``
       |
       | Returns a new random UUID object on the form "~u9f598f65-eea5-4906-a8f5-82f6d8e69726".
       |
       | ``["uuid", "abc98f65-ddf5-1234-a8f5-82f6d8e69726"]``
       |
       | Returns a new UUID object cast from the input argument: "~uabc98f65-ddf5-1234-a8f5-82f6d8e69726".
       |
       | ``["uuid", ["list", "abc98f65-ddf5-1234-a8f5-82f6d8e601a8", 2, "9f598f65-eea5-4906-a8f5-82f6d8e69726"]]``
       |
       | Returns two UUID objects: ["~uabc98f65-ddf5-1234-a8f5-82f6d8e69726", "~u9f598f65-eea5-4906-a8f5-82f6d8e69726"]
       | Note that the mismatched input argument ``2`` is ignored.

       .. WARNING::

          This function is non-deterministic and will return a
          different value every time it is evaluated. Be aware that if
          the pipe is rewound or reset then it will produce a
          different output. Dependency tracking will also have a
          similar effect as to produce a different value when entities
          are reprocessed.

          *Use this function with care and make sure
          that you are aware of the consequences of reprocessing
          entities.*

       .. _is_uuid_dtl_function:
   * - ``is-uuid``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a UUID literal or value or if
         it is a list, that the first element in the list is a UUID type value or literal
       |
     - | ``["is-uuid", ["uuid"]]``
       |
       | Returns true.
       |
       | ``["is-uuid", "~u9f598f65-eea5-4906-a8f5-82f6d8e69726"]``
       |
       | Returns true.
       |
       | ``["is-uuid", "some-string"]``
       |
       | Returns false.
       |
       | ``["is-uuid", ["list", ["uuid"], "12345"]]``
       |
       | Returns true.
       |
       | ``["is-uuid", ["list", "12345", ["uuid"]]]]``
       |
       | Returns false.
       |

Nested transformations
----------------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _apply_dtl_function:
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

       .. _apply_hops_dtl_function:
   * - ``apply-hops``
     - | *Arguments:*
       |   RULE_ID(string{1}),
       |   HOPS_SPEC(dict{>1})
       |
       | This function is a combined ``hops`` and ``apply`` function. It
         evaluates the hops, and then passes the result through
         the RULE_ID transform rule.

       | See the :ref:`apply <apply_dtl_function>`
         and the :ref:`hops <hops_dtl_function>` functions for more information
         about the parts.

       .. NOTE::

          Use this function instead of ``apply`` if you use ``hops`` inside
          the transformation rule. This is required so that
          `dependency tracking <concepts.html#dependency-tracking>`_
          can work. Calling ``apply`` on a rule that contains ``hops`` or
          ``apply-hops`` is not allowed.

     - | ``["apply-hops", "order", {``
       |   ``"datasets": ["orders o"],``
       |   ``"where": ["eq", "_S._id", "o.cust_id"]``
       |  ``}]``
       |
       | This will retrieve orders from the hops expression and then
         transform them using the ``order`` transformation rule. The output
         is the transformed order entities.


Paths
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _path_dtl_function:
   * - ``path``
     - | *Arguments:*
       |   PROPERTY_PATH(value-expression{1}),
       |   VALUES(value-expression{1})
       |
       | Traverses the PROPERTY_PATH path for each of the entities in
         VALUES. The result is all the values at the end of
         the traversal. This may be a single value or a list of values.
         PROPERTY_PATH is an expression that should resolve
         to a string or a list of strings. Those strings are treated as
         literals, i.e. property names, so no variables can be used. Only
         properties on the entity can be traversed. If you want to traverse
         to other entities use the ``hops`` function instead.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

         If namespaced identifiers are enabled and the path element is not
         a fully qualified namespaced identifier then all properties with
         the path element as its identifier part will be part of the result.
         In practice the result is the union of all those properties.

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
       |
       | ``["path", "age", {"age": 24}]``
       |
       | Returns ``24``.
       |
       | ``["path", "foo", {"bar": 123}]``
       |
       | Returns ``null``.
       |
       | ``["path", ["list", "a", "b"],``
       |   ``["list", {"a": {"b": 1}}, {"a": [{"b": 2}, {"b": 3}]}]]``
       |
       | Returns ``[1, 2, 3]``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | ``["path", "foo:a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``2`` as the path element ``"foo:a"`` is a fully qualified
         namespaced identifier.
       |
       | ``["path", "a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``[1, 2, 3, 4]``, i.e. the union of all the values in all
         the properties that have ``a`` in their identifiers part.
       |
       | ``["path", "::a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``1`` as ``"::a"`` uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to explicity reference the unqualified ``a`` property.
       |
       | ``["path", ":a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``[3, 4]`` as ``":a"`` uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to explicity reference the ``"a"`` property in the current namespace ``"bar"``.


Hops
----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _hops_dtl_function:
   * - ``hops``
     - | *Arguments:*
       |   HOPS_SPEC(dict{>1})
       |
       | The HOPS_SPEC is a dictionary that takes the following keys:

       1. ``datasets``: A list of strings with the dataset id
          whitespace separated by the dataset alias. The database
          aliases can be referenced in the ``where`` clause. The list
          must contain at least one element.

       2. ``where``: An expression or a list of expressions. If it is
          a list, then the expressions in the list will be wrapped
          with the ``and`` function. The expressions are then
          evaluated to perform the joins.

       3. ``recurse``: OPTIONAL. A boolean. The default is false. If
          true, then HOPS_SPEC should be traversed recursively. This
          makes it possible for a hops expression to be recursive. The
          output of one evaluation is fed as the input to the next
          evaluation until there are no more output. At that point the
          execution is moved on to the next HOPS_SPEC in the chain.

       4. ``exclude_root``: OPTIONAL. A boolean. The default is
          false. If true, then the original input to the recursion
          will not be included in the final output. This property is
          only meaningful on a HOP_SPEC where ``recurse`` is ``true``.

       5. ``max_depth``: OPTIONAL. An integer. The default is
          ``10``. The recursion will stop after the given number of
          recursion levels. A value of ``2`` means that the recursion will
          happen at most two times. Set it to ``null`` if you want the
          recursion will run until its output is exhausted. This
          property is only meaningful on a HOP_SPEC where ``recurse``
          is ``true``.

       6. ``return``: OPTIONAL. A string, or an expression, or not
          specified. If it is a string, then it should refer to a
          comma separated list of dataset aliases. In that case all
          the values of those aliases will be returned. If it is an
          expression then the expression is evaluated on the hops
          result and its result is returned. If not specified, then it
          will return the last dataset alias in the list. This is the
          default. It can only be specified on the last HOP_SPEC
          argument. ``return`` cannot be used with ``recurse``.

       7. ``track-dependencies``: OPTIONAL. A boolean. The default is
          true. Can be used to disable
          `dependency tracking <concepts.html#dependency-tracking>`_ for this
          particular HOP_SPEC.

       8. ``trace``: OPTIONAL. A string. The default is not set.
          If set, it is used to enable gathering of statistics for the execution of
          the ``hops`` function during runtime. Currently this tracks the maximum
          cardinality of the join statements in the ``hops``. This information
          will be available in the pipe execution log in the ``pump-completed`` and
          ``pump-failed`` entities. The value of the ``trace`` property
          should be unique to the particular ``hops`` function as it
          will be used to key the statistics gathered about its execution.
          The ``trace`` property should only be specified on the last HOP_SPEC argument.

       9. ``prefilters``: OPTIONAL. A dict where the keys must be dataset aliases
          specified in the ``datasets`` property. The values must be valid subset
          expressions, i.e. an ``eq`` DTL expression where the left hand side is
          the index expression and the right hand side is the value that represents
          the subset. Example: ``["eq", "_S.category", 72]``

       | If multiple HOP_SPEC arguments are given, then the output of
         a HOP_SPEC is passed on as the input to the next. This is a
         convenient way of chaining hops together. It is mostly useful
         when at least one of the HOP_SPEC arguments use recursion.

       | The join criteria are described by using the
         ``eq`` function. All dataset aliases defined in the
         ``datasets`` key have to be joined and all must by navigable
         from the source entity. If that is not the case, then an error
         will be raised at compile time.

       | The ``hops`` function produces a table inside, one column per
         dataset alias. This table is the projected down into a list
         of values by the ``return`` clause that is then returned by
         the function.

       | Note that the result of the ``hops`` function is deterministic based on the
         ``_id`` property of the entities processed within each dataset. I.e.. re-running a DTL transform with
         a ``hops`` function using the exact same entities in the source and in the datasets in the ``datasets`` property
         will yield the same order of the result. You should apply a ``sorted*`` function to the result to get a
         particular order (for example on a particular property, or if you use the ``return`` keyword).

       .. _hops_function_targeting_sink:

       .. WARNING::

          Hop-ing to the sink dataset is discouraged as there are some gotchas. In practice the pipe's ``batch_size`` must be set to ``1`` in order to guarantee that the hops is able to find the entities being written by the sink. Entities inside the current unflushed batch is not visible to the hops.

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
         ``country`` property with ``Country``'s ``_id`` property.
         Filter the addresses by type, so that only shipping and
         billing addresses are included in the result. Return the
         addresses found.

       ::

          ["hops", {
            "datasets": ["Person p"],
            "where": [
              ["eq", "_S.children", "p._id"],
              ["eq", "p.gender", "female"]],
            "recurse": true
           },
           {
            "datasets": ["Hobby h"],
            "where": ["eq", "_S.hobbies", "h._id"],
            "return": "h.name"
           }]

       | Recursively retrieve the source entity's daughters (and
         granddaughters and so on) and then return the names of all
         their hobbies. Please note that the result list is not automatically sorted on the ``name`` property - if order
         matters, a ``sorted`` function must be applied before the result is used.
       |

       ::

          ["hops", {
            "datasets": ["orders o", "product p"],
            "where": [
              ["eq", "_S._id", "o.customer_id"]
              ["eq", "o.lines.product_id", "p.product_id"]
            ],
            "prefilters": {
              "o": ["eq", "_S.webshop_id", "myshop"]
            }
           }]

       | Find the products that the customer has bought from a specific web shop. This example uses the ``prefilters``
         property to reference a subset of the ``orders`` dataset, i.e. the orders placed in the ``myshop`` web shop.

Entity lookups
--------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _lookup_entity_dtl_function:
   * - ``lookup-entity``
     - | *Arguments:*
       |   DATASET_ID(string{1})
       |   ENTITY_ID(string{1})
       |
       | Returns an entity in the given dataset.
     - | ``["lookup-entity", "code-table", "foo"]``
       |
       | Looks up the entity with the ``_id`` property value of ``foo`` in the ``code-table`` dataset.
       | Note that the dataset referenced has to be populated before the DTL transform can run.
       | If the entity doesn't exist in the dataset, ``null`` is returned.

       .. WARNING::

          This function does not support dependency tracking, so if
          the entity that is looked up changes then you may want to
          reset the pipe. This will not happen automatically.


Namespaced identifiers
----------------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _ni_dtl_function:
   * - ``ni``
     - | *Arguments:*
       |   NAMESPACE(string{0|1}),
       |   VALUES(value-expression{1})
       |
       | Translates input values to namespaced identifiers. Strings and URIs in VALUES
         will be cast to namespaced identifiers. Note that no escaping is done on
         the strings.
       |
       | If NAMESPACE is omitted, then the global namespace is used.
       |
       | URIs can be passed as values in VALUES only when NAMESPACE is not specified.
         The URIs will be collapsed, i.e. the prefix part of URIs will be collapsed into
         a namespace. If the prefix has been declared as a :ref:`namespace <namespaces>`
         then that namespace will be used, otherwise a generated namespace will be added.
     - | Constructs a new namespaced identifier.
       |
       | ``["ni", "foo", "bar"]``
       |
       | This will produce a namespaced identifier ``"~:foo:bar"``.
       |
       | ``["ni", "bar"]``
       |
       | This will produce a namespaced identifier in the global namespace; ``"~:bar"``.
       |
       | ``["ni", "foo", ["list", "bar", "x:y"]]``
       |
       | This will produce a list of two namespaced identifiers: ``["~:foo:bar", "~:foo:x:y"]``
       |
       | ``["ni", "foo", ["uri, "http://example.org/"]]``
       |
       | Returns ``null`` because URIs are not supported when NAMESPACE is specified.
       |
       | ``["ni", ["uri, "http://example.org/bar"]]``
       |
       | Returns ``"~:_:bar"``, i.e. a NI with the ``_`` namespace and ``bar`` as identifier.
         Note that the ``http://example.org/`` URI prefix is mapped to the  ``_`` namespace
         by default.
       |
       | ``["ni", ["uri, "http://unknown.org/something/baz"]]``
       |
       | If the ``"http://unknown.org/something/"`` URI prefix has not been declared as a
         namespace then it will return ``"~:your-pipe-1:baz"`` if the current pipe id is
         ``your-pipe``. The ``-1`` part is a sequence counter, so if you introduce other
         namespaces in your pipe they'll be assigned unique namespace ids. If the URI prefix
         had already been mapped to the ``unknown`` namespace then the expression would have
         returned ``"~:unknown:baz"``

       .. _is_ni_dtl_function:
   * - ``is-ni``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a namespaced
         identifier literal, or if it is a list, that the first element
         in the list is a namespaced identifier.
     - | ``["is-ni", ["ni", "foo:bar"]]``
       |
       | Returns ``true``.
       |
       | ``["is-ni", "foo:bar"]``
       |
       | Returns ``false``.
       |
       | ``["is-ni", ["list", ["ni", "foo:bar"], 12345]]``
       |
       | Returns ``true``.
       |
       | ``["is-ni", ["list", 1, ["ni", "foo:bar"]]]``
       |
       | Returns ``false``.

       .. _ni_ns_dtl_function:
   * - ``ni-ns``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Extracts the namespace part of namespaced identifiers. VALUES that
         are not namespaced identifiers are ignored.
       |
       | ``["ni-ns", "~:foo:bar"]``
       |
       | Returns ``"foo"``.
       |
       | ``["ni-ns", ["list", "~:foo:bar", "~:bar:baz"]]``
       |
       | Returns ``["foo", "bar"]``

       .. _ni_id_dtl_function:
   * - ``ni-id``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Extracts the namespace id part of namespaced identifiers. VALUES that
         are not namespaced identifiers are ignored.
       |
       | ``["ni-id", "~:foo:bar"]``
       |
       | Returns ``"bar"``.
       |
       | ``["ni-id", ["list", "~:foo:bar", "~:bar:baz"]]``
       |
       | Returns ``["bar", "baz"]``

       .. _ni_collapse_dtl_function:
   * - ``ni-collapse``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Uses the ``namespaces.default`` service metadata contents to produce a namespaced identifier from URLs.
         VALUES that are not URLs are ignored (i.e. it accepts strings and URI parameters). If there is no longest
         matching prefix in the ``namespaces.default`` settings, the functions will return a NI that contains the
         original input (i.e. the The ``http`` and ``https`` prefixes are implicitly defined). Non-http URIs are not
         supported.
         NOTE: this function is experimental and is meant to work with the ``global_defaults.symmetric_namespace_collapse``
         service metadata option set to ``true``.

       |
       | Given this ``namespaces.default`` mapping in the service metadata:
       |
       |  ``{``
            ``"foo": "http://psi.test.no/",``
            ``"sesam_male": "http://sesam.io/people/male/",``
            ``"sesam_female": "http://sesam.io/people/female/",``
            ``"sesam": "http://sesam.io/people/"``
          ``}``
       |
       | The following examples will produce this output:
       |
       | ``["ni-collapse", "http://psi.test.no/bar"]``
       |
       | Returns ``"~:foo:bar"``.
       |
       | ``["ni-collapse", ["list", "http://psi.test.no/bar", "http://psi.test.no/baz"]]``
       |
       | Returns ``["~:foo:bar", "~:foo:baz"]``
       |
       | ``["ni-collapse", "http://sesam.io/people/employees"]``
       |
       | Returns ``"~:sesam:employees"``
       |
       | ``["ni-collapse", "http://sesam.io/people/male/john"]``
       |
       | Returns ``"~:sesam_male:john"``
       |
       | ``["ni-collapse", "http://sesam.io/people/female/jane"]``
       |
       | Returns ``"~:sesam_female:jane"``
       |
       | The ``http`` and ``https`` namespaces are implicitly defined, so a URI that doesn't match any prefix will work:
       |
       | ``["ni-collapse", "http://example.com/path"]``
       |
       | Returns ``"~:http://example.com/path"``

       .. _ni_expand_dtl_function:
   * - ``ni-expand``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Uses the ``namespaces.default`` service metadata contents to produce a URL string from a namespaced identifier.
         VALUES that are not NIs are ignored. If there is no longest matching prefix in the ``namespaces.default``
         settings, the functions will return a string cast of the NI.
         NOTE: this function is experimental and is meant to work with the ``global_defaults.symmetric_namespace_collapse``
         service metadata option set to ``true``.

       |
       | Given this ``namespaces.default`` mapping in the service metadata:
       |
       |  ``{``
            ``"foo": "http://psi.test.no/",``
            ``"sesam_male": "http://sesam.io/people/male/",``
            ``"sesam_female": "http://sesam.io/people/female/",``
            ``"sesam": "http://sesam.io/people/"``
          ``}``
       |
       | The following examples will produce this output:
       |
       | ``["ni-expand", "~:foo:bar"]``
       |
       | Returns ``http://psi.test.no/bar``.
       |
       | ``["ni-expand", ["list", "~:foo:bar", "~:foo:baz"]]``
       |
       | Returns ``["http://psi.test.no/bar", "http://psi.test.no/baz"]``
       |
       | ``["ni-expand", "~:sesam:employees"]``
       |
       | Returns ``"http://sesam.io/people/employees"``
       |
       | ``["ni-expand", "~:sesam_male:john"]``
       |
       | Returns ``"http://sesam.io/people/male/john"``
       |
       | ``["ni-expand", "~:sesam_female:jane"]``
       |
       | Returns ``"http://sesam.io/people/female/jane"``
       |
       | ``["ni-expand", "~:http://example.com/path"]``
       |
       | Returns ``"http://example.com/path"``
       |
       | ``["ni-expand", "~:unknown:path"]``
       |
       | Returns ``"unknown:path"``

Lists
-----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _list_dtl_function:
   * - ``list``
     - | *Arguments:*
       |   VALUES(value-expression{>=0})
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

       .. _is_list_dtl_function:
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
       | Returns false.
       |
       | ``["is-list", ["items", ["dict", "1", 2]]]``
       |
       | Returns true.

       .. _first_dtl_function:
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

       .. _last_dtl_function:
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

       .. _in_dtl_function:
   * - ``in``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |   ITEMS(value-expression{1})
       |
       | Boolean function that returns ``true`` if all values in VALUES exist in ITEMS,
         i.e. if VALUES is a subset of ITEMS. Returns false if VALUES is null or empty.
     - | ``["in", "a", ["list", "a", "b", "c"]]``
       |
       | Returns ``true``.
       |
       | ``["in", "d", ["list", "a", "b", "c"]]``
       |
       | Returns ``false``.
       |
       | ``["in", ["list", 10], 10]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list"], 10]``
       |
       | Returns ``false``.
       |
       | ``["in", null, ["list", null]]``
       |
       | Returns ``false``.
       |
       | ``["in", ["list", null], ["list", 1, null, 2]]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list", "a", "c"],``
       |   ``["list", "a", "b", "c"]]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list", "a", "c", "d"],``
       |   ``["list", "a", "b", "c"]]``
       |
       | Returns ``false``.


       .. _nth_dtl_function:
   * - ``nth``
     - | *Arguments:*
       |   INDEX(integer-expression{1})
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

       .. _slice_dtl_function:
   * - ``slice``
     - | *Arguments:*
       |   START(integer-expression{1})
       |   END(integer-expression{0|1}}
       |   STRIDE(integer-expression{0|1}}
       |   VALUES(value-expression{1})
       |
       | Returns a slice of VALUES from START to END with STRIDE. If END is not specified, the slice will
         continue to the end of VALUES. If no STRIDE is specified every element is returned (same as STRIDE=1).

     - | ``["slice", 2, -2, 2, ["list", 0, 1, 2, 3, 4, 5, 6]]``
       | Returns ``[2, 4]``
       |
       | ``["slice", 2, ["list", 0, 1, 2, 3, 4, 5, 6]]``
       | Returns ``[2, 3, 4, 5, 6]``

       .. _insert_dtl_function:
   * - ``insert``
     - | *Arguments:*
       |   INDEX(integer-expression{1})
       |   VALUES(value-expression{1})
       |   OBJECT(value-expression{1})
       |
       | Inserts OBJECT at INDEX in VALUES. A negative INDEX means starting from the end.

     - | ``["insert", 1, 2, 3]``
       | Returns ``[2, 3]``
       |
       | ``["insert", 1, ["list", 1, 2], ["list", 3, 4]]``
       | Returns ``[1, [3, 4], 2]``
       |
       | ``["insert", -2, ["list", 1, 2, 3], 4]``
       | Returns ``[1, 4, 2, 3]``

       .. _combine_dtl_function:
   * - ``combine``
     - | *Arguments:*
       |   VALUES(value-expression{>=1})
       |
       | Combines the VALUES into a single list.

     - | ``["combine", null]``
       | Returns ``[]``
       |
       | ``["combine", 1]``
       | Returns ``[1]``
       |
       | ``["combine", 1, 4]``
       | Returns ``[1, 4]``
       |
       | ``["combine", 1, ["list", 2, 3]]``
       | Returns ``[1, 2, 3]``
       |
       | ``["combine", 1, ["list", 2, 3, ["list", 4]]]``
       | Returns ``[1, 2, 3, [4]]``
       |
       | ``["combine", ["list", 1, 2], ["list", 3, 4], 5]``
       | Returns ``[1, 2, 3, 4, 5]``

       .. _flatten_dtl_function:
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
       | ``["flatten",``
       |   ``["list", ["list", 1, 2],``
       |     ``["list", 3, ["list", 4], 5]]]``
       |
       | Returns ``[1, 2, 3, [4], 5]``.
       |
       | ``["flatten", ["list", "_S.sisters", "_S.brothers"]]``
       |
       | Returns a list that contains the sisters and brothers.

       .. _filter_dtl_function:
   * - ``filter``
     - | *Arguments:*
       |   FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | Filters out the the values in VALUES for which the FUNCTION expression
         does *not* evaluate to *true*.
     - | ``["filter", ["gt", "_.age", 42],``
       |     ``["list", {"age": 30}, {"age": 50}, {"age": 40}]]``
       |
       | Returns ``[{"age": 50}]``.
       |
       | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the order entities that have an amount of more than 100.

       .. _min_dtl_function:
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

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["min", ["list", 4, 2, 5, 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", ["list", "b", 2, "a", 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", ["list", {"x": 1}, "b", "a"]]``
       |
       | Returns ``"a"``.
       |
       | ``["min", ["list", "B", "b", "A", "a"]]``
       |
       | Returns ``"A"`` (Based on `ASCII ordering <https://ascii.cl/>`_).
       |
       | ``["min", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the lowest amount.

       .. _max_dtl_function:
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

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["max", ["list", 4, 2, 5, 3]]``
       |
       | Returns ``5``.
       |
       | ``["max", ["list", "b", 2, "a", 3]]``
       |
       | Returns ``"b"``.
       |
       | ``["max", ["list", {"x": 1}, "b", 2, "a"]]``
       |
       | Returns ``{"x": 1}``.
       |
       | ``["max", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the highest amount.

       .. _sum_dtl_function:
   * - ``sum``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the sum of the numeric values in VALUES. Any non-numeric
         values are ignored.
     - | ``["sum", ["list", 2, 4, 6]]``
       |
       | Returns ``12``.
       |
       | ``["sum", "_S.amounts"]]``
       |
       | Returns the sum of the amounts.

       .. _count_dtl_function:
   * - ``count``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the number of elements in VALUES.
     - | ``["count", ["list", 2, 4, 6]]``
       |
       | Returns ``3``.
       |
       | ``["count", null]]``
       |
       | Returns ``0``.
       |
       | ``["count", 123]]``
       |
       | Returns ``1``.
       |
       | ``["count", "_S.orders"]]``
       |
       | Returns the the number of orders.

       .. _range_dtl_function:
   * - ``range``
     - | *Arguments:*
       |   START(integer-expression{1})
       |   STOP(integer-expression{1})
       |   STEP(integer-expression{0|1})
       |
       | Returns a list of integers ranging from START (inclusive) to STOP
         (exclusive) in STEP increments. Note that STEP cannot be 0 and all
         arguments must be integers or integer expressions.
     - | ``["range", 0, 4]``
       |
       | Returns ``[0, 1, 2, 3]``.
       |
       | ``["range", 4, 0, -1]]``
       |
       | Returns ``[4, 3, 2, 1]``.

       .. _enumerate_dtl_function:
   * - ``enumerate``
     - | *Arguments:*
       |   START(integer-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Enumerates the values by returning dictionaries with ``key``
         and ``value`` keys. ``value`` contains the value and ``key`` the
         enumerator count. The enumeration counter starts at START and uses an
         increment of 1. The default value of START is 0.
     - | ``["enumerate", "a"]``
       |
       | Returns ``{"key": 0, "value": "a"}``.
       |
       | ``["enumerate", 1, "a"]``
       |
       | Returns ``{"key": 1, "value": "a"}``.
       |
       | ``["enumerate", ["list", 17, 32, 21]]``
       |
       | Returns ``[{"key": 0, "value": 17},``
       |    ``{"key": 1, "value": 32},``
       |    ``{"key": 2, "value": 21}]``.
       |
       | ``["enumerate", 2, ["list", 17, 32, 21]]``
       |
       | Returns ``[{"key": 2, "value": 17},``
       |   ``{"key": 3, "value": 32},``
       |   ``{"key": 4, "value": 21}]``.

       .. _distinct_dtl_function:
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

       .. _sorted_dtl_function:
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

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["sorted", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[2, 3, 4, 4, 5]``.
       |
       | ``["sorted", ["list", "b", 2, {"x": 1}, "a", 4]]``
       |
       | Returns ``[2, 4, "a", "b", {"x": 1}]``.
       | Note that the values are sorted using :ref:`mixed type ordering <mixed_type_ordering>`.
       |
       | ``["sorted",``
       |   ``["list", {"x": 1}, {"x": "abc"}, {"x": 2}]]``
       |
       | Returns ``[{"x": 1}, {"x": 2}, {"x": "abc"}]``
       |
       | ``["sorted", "_.age",``
       |   ``["list",``
       |     ``{"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 20}, {"age": 30}, {"age": 50}]``.
       |
       | ``["sorted", "_S.tags"]]``
       |
       | Returns the tags in ascending order.

       .. _sorted_descending_dtl_function:
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

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["sorted-descending", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[5, 4, 4, 3, 2]``.
       |
       | ``["sorted-descending", ["list", "b", 2, {"x": 1}, "a", 4]]``
       |
       | Returns ``[{"x": 1}, "b", "a", 4, 2]``.
       | Note that the values are sorted using :ref:`mixed type ordering <mixed_type_ordering>`.
       |
       | ``["sorted-descending",``
       |   ``["list", {"x": 1}, {"x": "abc"}, {"x": 2}]]``
       |
       | Returns ``[{"x": "abc"}, {"x": 2}, {"x": 1}]``
       |
       | ``["sorted-descending", "_.age",``
       |   ``["list",``
       |     ``{"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 50}, {"age": 30}, {"age": 20}]``.
       |
       | ``["sorted-descending", "_S.tags"]]``
       |
       | Returns the tags in descending order.

       .. _reversed_dtl_function:
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

       .. _map_dtl_function:
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
       |   ``["list", ["list", "A", "A"],``
       |     ``["list", "B", "C"]]]``
       |
       | Returns ``[["A"], ["B", "C"]]``.

       .. _map_values_dtl_function:
   * - ``map-values``
     - | *Arguments:*
       |   VALUE_FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each dictionary in VALUES apply the VALUE_FUNCTION to the
         dictionary's values. The function maps over the values of dictionaries
         and returns a list of mapped values. Non-dictionary values are ignored.
     - | ``["map-values",``
       |     ``["lower", "_."],``
       |     ``{"key1": "A", "key2": "B"}]``
       |
       | Returns ``["a", "b"]``.
       |
       | ``["map-values",``
       |     ``["lower", "_."],``
       |     ``["list", {"key1": "A", "key2": "B"}, 100,``
       |       ``{"key1": "B", "key2": "A", "key3": "C"}]]``
       |
       | Returns ``["a", "b", "b", "a", "c"]``.
       |

       .. _map_dict_dtl_function:
   * - ``map-dict``
     - | *Arguments:*
       |   KEY_FUNCTION(function-expression(1}
       |   VALUE_FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each dictionary in VALUES construct a new dictionary by applying
         the KEY_FUNCTION function and the VALUE_FUNCTION to all its key+value
         pairs. If the KEY_FUNCTION returns a non-string value then the key+value
         pair is ignored. Empty dictionaries are not returned.
     - | ``["map-dict",``
       |     ``["upper", "_."], ["plus", 1, "_."],``
       |     ``{"A": 1, "B": 2}]``
       |
       | Returns ``{"A": 2, "B": 3}``.
       |
       | ``["map-dict",``
       |     ``["if", ["gt", ["length", "_."], 2],``
       |         ``["concat", "x:", "_."]], "_.",``
       |     ``["list",``
       |         ``{"abc": 1, "ab": 2, "abcd": 3},``
       |         ``{"def": 4}, {"gh": 5}]]``
       |
       | Returns ``[{"x:abc": 1, "x:abcd": 3}, {"x:def": 4}]``.

       .. _group_by_dtl_function:
   * - ``group-by``
     - | *Arguments:*
       |   KEY_FUNCTION(function-expression(0|1}
       |   STRING_FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Groups the values in VALUES by the result of executing the KEY_FUNCTION
         function on them. Returns a dictionary, where the key is the
         group key and the value is the list of values in VALUES that were
         grouped under that key.

       .. NOTE::

          The keys in the returned dict are strings only. The reason
          is that the :ref:`entity data model <entity_data_types>`
          (and `JSON <http://json.org/>`_) only supports string keys.

          The group keys are :ref:`transit encoded <extension-types>`
          JSON strings, i.e. the same kind of strings generated by the
          :ref:`json-transit <json_transit_dtl_function>` function.

          If you do not want the keys to be transit encoded JSON, then you have the
          option of specifying STRING_FUNCTION, a function that then will be used to
          generate the string key.
     - | ``["group-by", ["length", "_."],``
       |   ``["list", "phi", "alpha", "rho"]]``
       |
       | Returns ``{"3": ["phi", "rho"], "5": ["alpha"]}``.
       |
       | ``["group-by", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns order lines grouped by EAN, i.e. product number.
       |
       | ``["group-by", "_.gender", "_S.people"]]``
       |
       | Returns a dictionary of people grouped by their gender.
       |
       | ``["group-by",``
       |   ``["upper", "_."], ["list", "a", "b"]]``
       |
       | Returns ``{"\"A\"": ["a"], "\"B\"": ["b"]}``. The keys are
         transit-encoded JSON strings.
       |
       | ``["group-by",``
       |   ``["upper", "_."],``
       |   ``["string", "_."], ["list", "a", "b"]]``
       |
       | Returns ``{"A": ["a"], "B": ["b"]}``. Same as above, but we specify
         a STRING_FUNCTION function that creates string keys.


Sets
----

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _union_dtl_function:
   * - ``union``
     - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the union of the two sets VALUES1 and VALUES2, i.e. the elements that
         are either in VALUES1 or in VALUES2. The two arguments do not have to be real
         sets, but will be coerced into sets before applying the union operator. The
         return type is a list of distinct values.
     - | ``["union",``
       |     ``["list", "A", "B"], ["list", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union", "A", ["list", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.

       .. _intersection_dtl_function:
   * - ``intersection``
     - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the intersection of the two sets VALUES1 and VALUES2, i.e. the elements
         that are in both VALUES1 and VALUES2. The two arguments do not have to be real sets,
         but will be coerced into sets before applying the intersection operator. The
         return type is a list of distinct values.
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

       .. _intersects_dtl_function:
   * - ``intersects``
     - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Same as ``intersection``, but returns a boolean value. Returns true if the two
         arguments have elements in common.
     - | ``["intersects",``
       |     ``["list", "A", "B"], ["list", "B", "C"]]``
       |
       | Returns ``true``.
       |
       | ``["intersects", "B", ["list", "B", "C"]]``
       |
       | Returns ``true``.
       |
       | ``["intersects", "A", ["list", "B", "C"]]``
       |
       | Returns ``false``.

       .. _difference_dtl_function:
   * - ``difference``
     - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the difference of the two sets VALUES1 and VALUES2, i.e. the elements
         that are in VALUES1, but not in VALUES2. The two arguments do not have to be real
         sets, but will be coerced into sets before applying the difference operator. The
         return type is a list of distinct values.
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


Dictionaries
------------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _items_dtl_function:
   * - ``items``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of key+value tuples.
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
       | Returns ``[["A", 1]]``.

       .. _dict_dtl_function:
   * - ``dict``
     - | *Arguments:*
       |   EMPTY{0} or ITEMS(value-expression{1}) or (KEY, VALUE){>=0)
       |
       | If EMPTY, i.e. no arguments given, then an empty dict (``{}``) is returned.
       |
       | If ITEMS specified, then it takes a list of key+value pair tuples and
         returns a dictionary with those tuples as keys and values. Note that
         last key  wins. Values that are not two-element tuples are ignored.
       |
       | If KEY+VALUE pairs are given, then a new dict with those pairs as keys and
         values. Note that last key  wins.
     - | ``["dict"]``
       |
       | Returns ``{}``.
       |
       | ``["dict",``
       |     ``["list",``
       |         ``["list", "A", 1],``
       |         ``["list", "B", 2],``
       |         ``["list", "C", 3]]]``
       |
       | Returns ``{"A": 1, "B": 2, "C": 3}``.
       |
       | ``["dict", ["list", "X", 123, ["list", "A", 1]]``
       |
       | Returns ``{"A": 1}``.
       |
       | ``["dict",``
       |   ``"a", ["upper", "a"],``
       |   ``["lower", "B"], "B"]``
       |
       | Returns ``{"a": "A", "b": "B"}``.

       .. _is_dict_dtl_function:
   * - ``is-dict``
     - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a dictionary or if it is a list, that the first element
       | in the list is a dictionary
       |
     - | ``["is-dict", "_S."]``
       |
       | Returns true.
       |
       | ``["is-dict", ["list", {"a": 1}, 123]``
       |
       | Returns true.
       |
       | ``["is-dict", ["list", 123, {"a": 1}]``
       |
       | Returns false.
       |
       | ``["is-dict", "abc"]``
       |
       | Returns false

       .. _keys_dtl_function:
   * - ``keys``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of keys.
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

       .. _values_dtl_function:
   * - ``values``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of values.
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

       .. _key_values_dtl_function:
   * - ``key-values``
     - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of dictionaries with "key"
         and "value" keys. For each key+value pair in the dictionaries one dict is added
         to the output list. Non-dictionary values are ignored. Note that entities are
         dictionaries, so you can use this function with them.
     - | ``["key-values",``
       |     ``["list", {"A": 1, "B": 2}, 123, {"C": 3, "A": 1}]]``
       |
       | Returns ``[{"key": "A", "value": 1},``
       |            ``{"key": "B", "value": 2},``
       |            ``{"key": "C", "value": 3},``
       |            ``{"key": "A", "value": 1}]``.
       |
       | ``["key-values", {"hello": "world"}]``
       |
       | Returns ``{"key": "hello", "value": "world"}``.


Tuples
------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _tuples_dtl_function:
   * - ``tuples``
     - | *Arguments:*
       |   VALUES(value-expression{>0})
       |
       | Constructs a list of tuples, the product of the values given in the
         arguments. The tuple length is equal to the number
         of function arguments. ``null`` values are ignored.
       |
       | This function is a good choice when you need to do joins on
         composite keys.
     - | ``["tuples"]``
       |
       | Returns ``[]``.
       |
       | ``["tuples", "a", "b", "c"]``
       |
       | Returns ``[["a", "b", "c"]]``.
       |
       | ``["tuples", ["list", 1, 2], 3]``
       |
       | Returns ``[[1, 3], [2, 3]]``.
       |
       | ``["tuples",``
       |   ``["list", 1, 2], ["list", 3, null, 4, 5]]``
       |
       | Returns ``[[1, 3], [1, 4], [1, 5],``
       |         ``[2, 3], [2, 4], [2, 5]]``. The ``null`` value was ignored.

Hashing
-------

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _hash128_dtl_function:
   * - ``hash128``
     - | *Arguments:*
       |   ALGORITM("murmur3")
       |   VALUES(value-expression{1})
       |
       | Generates 128 bit integer hashes from bytes and strings. Values of
         other types are ignored. This function can be used to generate
         content hashes. The only supported algoritm is "murmur3"
         (`MurmurHash3 <https://en.wikipedia.org/wiki/MurmurHash>`_).
     - | ``["hash128", "murmur3", "abc"]``
       |
       | Returns ``79267961763742113019008347020647561319``.
       |
       | ``["hash128", "murmur3", ["combine", "abc", 123, "def"]]``
       |
       | Returns ``[[79267961763742113019008347020647561319,``
       |           ``114697464648834432121201791580882983835]]``.


Math
----

The ``plus``, ``minus``, ``multiply``, ``divide``, ``mod`` and ``pow`` functions are ``map``-style functions that apply the first
argument to one or more values. For "natural order" math operators that operate on single numbers, use the symbolic
equivalents ``+``, ``-``, ``*``, ``/``, ``%`` and ``^``. If the argument(s) to the natural order functions
are lists, the first value is used. If either argument evaluates to ``null``, the result will also be
``null``.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _plus_dtl_function:
   * - ``plus``
     - | *Arguments:*
       |   INCREMENT(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of ``VALUES`` and increments them by ``INCREMENT``. Non-numeric
         values are ignored.
     - | ``["plus", 10, ["list", 1, 2, 3]]``
       |
       | Returns ``[11, 12, 13]``.
       |
       | ``["plus", 10, 10]``
       |
       | Returns ``20``.

       .. _plus_symbol_dtl_function:
   * - ``+``
     - | *Arguments:*
       |   VALUE1(value-expression{1})
       |   VALUE2(value-expression{1})
       |
       | Returns the result of ``VALUE1 + VALUE2``. The result is always a single number (or ``null``).
     - | ``["+", 10, 3]``
       |
       | Returns ``13``.
       |
       | ``["+", 10, ["list", 10, 20, 30]]``
       |
       | Returns ``20``.

       .. _minus_dtl_function:
   * - ``minus``
     - | *Arguments:*
       |   DECREMENT(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of ``VALUES`` and decrements them by ``DECREMENT``. Non-numeric
         values are ignored.
     - | ``["minus", 1, ["list", 1, 2, 3]]``
       |
       | Returns ``[0, 1, 2]``.
       |
       | ``["minus", 10, 12]``
       |
       | Returns ``2``.

       .. _minus_symbol_dtl_function:
   * - ``-``
     - | *Arguments:*
       |   VALUE1(value-expression{1})
       |   VALUE2(value-expression{1})
       |
       | Returns the result of ``VALUE1 - VALUE2``. The result is always a single number (or ``null``).

     - | ``["-", 1, ["list", 1, 2, 3]]``
       |
       | Returns ``0``.
       |
       | ``["-", 10, 12]``
       |
       | Returns ``-2``.

       .. _divide_dtl_function:
   * - ``divide``
     - | *Arguments:*
       |   DIVISOR(numeric-expression{1})
       |   DIVIDENDS(value-expression{1})
       |
       | Takes a list of ``DIVIDENDS`` and divides them by ``DIVISOR``. Non-numeric
         values are ignored.
     - | ``["divide", 2, ["list", 2, 4, 6]]``
       |
       | Returns ``[1, 2, 3]``.
       |
       | ``["divide", 10, 20]``
       |
       | Returns ``2``.
       |
       | ``["divide", ["list", 2, 8], 3]``
       |
       | Returns ``1.5``.

       .. _divide_symbol_dtl_function:
   * - ``/``
     - | *Arguments:*
       |   DIVIDEND(numeric-expression{1})
       |   DIVISOR(value-expression{1})
       |
       | Returns the result of ``DIVIDEND / DIVISOR``. The result is always a single number (or ``null``).
     - | ``["/", 2, ["list", 4, 6, 8]]``
       |
       | Returns ``0.5``.
       |
       | ``["/", 10, 20]``
       |
       | Returns ``0.5``.
       |
       | ``["/", ["list", -3, 10, 100], 2]``
       |
       | Returns ``-1.5``.
       |
       | ``["/", ["list", 3, 8], ["list", -2, 6]]``
       |
       | Returns ``-1.5``.
       |
       | ``["/", 5, 0]``
       |
       | Returns ``null``.

       .. _multiply_dtl_function:
   * - ``multiply``
     - | *Arguments:*
       |   MULTIPLIER(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of ``VALUES`` and multiplies them by ``MULTIPLIER``. Non-numeric
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

       .. _multiply_symbol_dtl_function:
   * - ``*``
     - | *Arguments:*
       |   VALUE(value-expression{1})
       |   MULTIPLIER(value-expression{1})
       |
       | Returns the result of the expression ``VALUE * MULTIPLIER``
     - | ``["*", 2, ["list", 2, 4, 6]]``
       |
       | Returns ``4``.
       |
       | ``["*", 10, 20]``
       |
       | Returns ``200``.
       |
       | ``["*", ["list", 2.3, 14], 2]``
       |
       | Returns ``4.6``.

       .. _mod_dtl_function:
   * - ``mod``
     - | *Arguments:*
       |   DIVISOR(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of ``VALUES`` and finds the remainder of dividing them
         by ``DIVISOR``. Non-numeric values are ignored.
     - | ``["mod", 2, ["list", 2, 5, 6]]``
       |
       | Returns ``[0, 1, 0]``.
       |
       | ``["mod", 3, 5]``
       |
       | Returns ``2``.

       .. _mod_symbol_dtl_function:
   * - ``%``
     - | *Arguments:*
       |   DIVIDEND(numeric-expression{1})
       |   DIVISOR(value-expression{1})
       |
       | Takes a ``DIVIDEND`` value finds the remainder of dividing them by ``DIVISOR``:
         ``DIVIDEND % DIVISOR``. Non-numeric values are ignored.
     - | ``["%", 2, ["list", 2, 5, 6]]``
       |
       | Returns ``0``.
       |
       | ``["%", 5, 3]``
       |
       | Returns ``2``.
       |
       | ``["%", ["list", 5, 8, 9], 3]``
       |
       | Returns ``2``.
       |
       | ``["%", ["list", 5, 8, 9], ["list", 3, -2.3]]``
       |
       | Returns ``2``.

       .. _pow_dtl_function:
   * - ``pow``
     - | *Arguments:*
       |   EXPONENT(numeric-expression{1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of ``VALUES`` and raises them to the power of ``EXPONENT``.
         Non-numeric values are ignored.
     - | ``["pow", 2, ["list", 2, 5, 6]]``
       |
       | Returns ``[4, 25, 36]``.
       |
       | ``["pow", 3, 10]``
       |
       | Returns ``1000``.

       .. _pow_symbol_dtl_function:
   * - ``^``
     - | *Arguments:*
       |   VALUE(value-expression{1})
       |   EXPONENT(value-expression{1})
       |
       | Takes a ``VALUE`` and raises it to the power of ``EXPONENT``:
         ``VALUE^EXPONENT``. The result is always a single value (or ``null``).
         Non-numeric values are ignored.
     - | ``["^", 2, ["list", 2, 5, 6]]``
       |
       | Returns ``4``.
       |
       | ``["^", 5, 2]``
       |
       | Returns ``25``.
       |
       | ``["^", ["list", 2, 8, 9], 3]``
       |
       | Returns ``8``.
       |
       | ``["^", ["list", 2, 8, 9], ["list", 3, -2.3]]``
       |
       | Returns ``8``.

       .. _round_dtl_function:
   * - ``round``
     - | *Arguments:*
       |   DIGITS(numeric-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and optionally rounds them to the number of DIGITS and then returns the nearest integer
         digit (adjusted for the number of digits specified, default is 0). Non-numeric
         values are ignored. In contrast to ``ceil`` or ``floor`` it uses the "half to even" rule to decide if to round
         up or down (see `this wikipedia article <https://en.wikipedia.org/wiki/Rounding#Round_half_to_even>`_ for details).
     - | ``["round", ["list", 2.2, 3.5, 4.5]]``
       |
       | Returns ``[2, 4, 4]``.
       |
       | ``["round", 1, ["list", 2.2, 4.778, 6]]``
       |
       | Returns ``[2.2, 4.8, 6]``.
       |
       | ``["round", 2, 2.299]``
       |
       | Returns ``2.30``.
       |
       | ``["round", 2.299]``
       |
       | Returns ``3``.
       |
       | Note that the even/odd rule also applies to negative numbers:
       | ``["round", -4.5]``
       |
       | Returns ``-4``.
       |
       | ``["round", -3.5]``
       |
       | Returns ``-4``.
       |
       | If ``DIGITS`` is 0 or not provided, the return value will be of type integer. In all other cases
       | it will be a decimal or a float.

       .. _ceil_dtl_function:
   * - ``ceil``
     - | *Arguments:*
       |   DIGITS(numeric-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and optionally rounds them to the number of DIGITS and then returns the nearest integer
         that is larger than the value (adjusted for the number of digits specified, default is 0). Non-numeric
         values are ignored.
     - | ``["ceil", ["list", 2.2, 4.778, 6]]``
       |
       | Returns ``[3, 5, 6]``.
       |
       | ``["ceil", 1, ["list", 2.2, 4.778, 6]]``
       |
       | Returns ``[2.2, 4.8, 6]``.
       |
       | ``["ceil", 2, 2.299]``
       |
       | Returns ``2.30``.
       |
       | ``["ceil", 2.299]``
       |
       | Returns ``3``.
       |
       | Note that if ``DIGITS`` is 0 or not provided, the return value will be of type integer. In all other cases
       | it will be a decimal or a float.


       .. _floor_dtl_function:
   * - ``floor``
     - | *Arguments:*
       |   DIGITS(numeric-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Takes a list of VALUES and optionally rounds them to the number of DIGITS and then returns the nearest integer
         that is lower than the value (adjusted for the number of digits specified, default is 0). Non-numeric
         values are ignored.
     - | ``["floor", ["list", 2.2, 4.778, 6]]``
       |
       | Returns ``[2, 4, 6]``.
       |
       | ``["floor", 1, ["list", 2.2, 4.778, 6]]``
       |
       | Returns ``[2.2, 4.7, 6]``.
       |
       | ``["floor", 2, 2.299]``
       |
       | Returns ``2.29``.
       |
       | ``["floor", 2.299]``
       |
       | Returns ``2``.
       |
       | Note that if ``DIGITS`` is 0 or not provided, the return value will be of type integer. In all other cases
       | it will be a decimal or a float.

       .. _abs_dtl_function:
   * - ``abs``
     - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the absolute value. If the VALUE is an integer,
         an integer will be returned. If not, a decimal or a float.
     - | ``["abs", ["list", -2, 4, -6]]``
       |
       | Returns ``[2, 4, 6]``.
       |
       | ``["abs", 2]``
       |
       | Returns ``2``.
       |
       | ``["abs", -2.23]``
       |
       | Returns ``2.23``.

       .. _sqrt_dtl_function:
   * - ``sqrt``
     - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the square root of the value. If the result is not a real number,
         ``None`` is returned instead.
     - | ``["sqrt", ["list", 4, 9, 16]]``
       |
       | Returns ``[2.0, 3.0, 4.0]``.
       |
       | ``["sqrt", -2]``
       |
       | Returns ``None``.
       |
       | ``["sqrt", 9.0]``
       |
       | Returns ``3.0``.

       .. _sin_dtl_function:
   * - ``sin``
     - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the sinus of the value, where value is in
         radians.
     - | ``["sin", ["list", 0, 3.14159265]]``
       |
       | Returns ``[0.0, ~0.0]``.
       |
       | ``["sin", 0.0]``
       |
       | Returns ``0.0``.

       .. _cos_dtl_function:
   * - ``cos``
     - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the cosinus of the value, where value is in
         radians.
     - | ``["cos", ["list", 0, 3.14159265]]``
       |
       | Returns ``[1.0, ~-1.0]``.
       |
       | ``["cos", 0.0]``
       |
       | Returns ``1.0``.

       .. _tan_dtl_function:
   * - ``tan``
     - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the tangens of the value, where value is in
         radians. Note that values approaching very close to multiples of PI/2 will be
         undefined (+-infinite) and the result will be a ``None`` value.
     - | ``["tan", ["list", 0, 3.14159265]]``
       |
       | Returns ``[0.0, ~0.0]``.


Misc
----


.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _fail_dtl_function:
   * - ``fail!``
     - | *Arguments:*
       |   MESSAGE(string{1})
       |
       | A function that makes the pump fail. It can be used to conditionally fail the pump. A string error message can be specified in the first argument.
     - | ``["fail!", "Processing stopped because of invalid input. Please review."]``
       |
       | Causes the pump to fail. The error message is reported in the `pump-failed` event in the pump execution dataset.



.. _supported_timezones:

Supported timezones
===================
The :ref:`datetime-shift<datetime_shift_dtl_function>` dtl-function supports the following timezones:

..
  TODO get this list from same pytz library version that the node uses

'Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET' and 'Zulu'.
