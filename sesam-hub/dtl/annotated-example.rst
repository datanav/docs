Annotated Example
=================

Let's say that we have two datasets, ``person`` and ``orders``, and that
we want to transform the *persons* by joining in their *orders* and
apply a few other transform functions. In this section you'll find a
complete DTL transform that takes entities from the ``person`` dataset,
joins them with entities from the ``orders`` dataset and creates new
entities from them.

Given the following *source entity* (from the ``person`` dataset):

.. code-block:: json


  {
    "_id": "1",
    "name": "John Smith",
    "age": 25
  }

We then want to transform it into the following *target entity*:

.. code-block:: json

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

.. code-block:: json

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
     dataset. You can think of it as the entry point of the execution,
     similar to a ``main`` function in many programming languages.

3. | ``["copy", "_id"]`` copies the ``_id`` property from the source
     entity to the target entity.

4. | ``["add", "type", "customer"]`` adds the ``type`` property to the target
     entity with the literal value ``"customer"``.

5. | ``["add", "name", ["upper", "_S.name"]]`` adds the ``name``
     property to the target entity, uppercasing the name in the source
     entity.

.. code-block:: json

  ["add", "orders",
    ["sorted", "_.amount",
      ["apply-hops", "order", {
        "datasets": ["orders o"],
        "where": [
          ["eq", "_S._id", "o.cust_id"]
        ]
      }]
    ]
  ]

1. | The expression above adds the ``orders`` property to the target
     entity. It does this by joining the source entity's ``_id``
     property with the ``cust_id`` property of entities in the
     ``orders`` dataset. The join is done by the ``apply-hops`` function,
     which takes a hops specification that contains list of ``datasets``,
     assigns aliases to them, which then get exposed as variables that
     you can use in expressions in the ``where`` clause. The result of
     the join is a list of orders:

.. code-block:: json

  [
    {
      "_id": "100",
      "amount": 320,
      "order_lines": ["..."],
      "cust_id": "1"
    },
    {
      "_id": "200",
      "amount": 500,
      "order_lines": ["..."],
      "cust_id": "1"
    }
  ]

Next, the ``order`` transform is then applied. The result of this is a list of orders with two properties: ``_id`` and ``amount``:

.. code-block:: json


    [{
      "_id": "100",
      "amount": 320
    },
    {
      "_id": "200",
      "amount": 500
    }]

The order entities are then ``sorted`` by their ``amount`` property before being assigned to the ``orders`` property on the target entity:

.. code-block:: json


    [{
      "_id": "100",
      "amount": 320
    },
    {
      "_id": "200",
      "amount": 500
    }]

2. | ``["add", "order_count", ["count", "_T.orders"]]`` adds the
     ``order_count`` property to the target entity. Note that the value
     is the number of order entities in the target entity's ``orders``
     property. Note that we can access properties on the target entity
     once we've added them.

3. | Stop processing if the ``["filter", ["gt", "_T.order_count", 10]]``
     evaluates to true. If the filter is false the target entity is not
     emitted / created.

.. note::

  - Transform functions are applied in the order given. The order is
    significant, and one transform can use target entity properties
    created by earlier transform function.

  - The hops function is deterministic but not sorted (it produces deterministic order
    based on the ``_id`` property of the entities within each dataset it processes).
    You must apply the ``sorted`` function to the result of a hops join to achieve a
    particular order.

  - The filter function can be used to stop transformation of individual
    entities, effectively filtering them out of the output stream.

  - When the DTL of a pipe is modified, the pipe's "last-seen" value must be
    cleared in order to reprocess already seen entities with the new DTL.
    This can be done by setting the "last-seen" value to an empty string with the
    `update-last-seen <./api.html#api-reference-pump-update-last-seen>`_ operation in the SESAM API.
