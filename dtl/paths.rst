.. _path_expressions_and_hops:

Path Expressions and Hops
=========================

There are three ways that one can access properties on entities:

Property path strings
---------------------

``"_S.orders.amount"``, which will start from the given variable, in this case the source entity ``_S``, and then traverse to the ``orders`` property and then to the ``amount`` property. The end result is a list of amounts.

.. note::

  The property path strings function can only access property on the entity it operates on, including nested entities.

One can also refer to the content of the variables themselves, e.g. ``"_S."`` would refer to the source entity itself (note the dot after the variable name). ``"_T."`` refers to the target entity, and ``"_."`` refers to the current value.

You can have periods in path elements if you quote them. Example:
``"_S.foo.'john.doe''s'.bar"`` is equivalent to ``["path", ["list", "foo", "john.doe's", "bar"], , "_S."]``. A quoted path element must begin and end with a single quote. Single quotes can be escaped with ``''``.

The "path" function
-------------------

``["path", "placed_by", ["sorted", "_.amount", "_S.orders"]]``, which will first evaluate the rightmost expression. Then it will traverse the path given in the first argument for each of them and return the end result. The first argument is an expression that resolve to either a single string or a list of strings.

.. note::
  Note that the ``path`` function can only access property on the dictionary/entity it operates on, including nested ones.

The "hops" function
-------------------

The ``hops`` function can be used to perform :ref:`joins <joins>` across two or more datasets, so if you want to navigate beyond the current entity use ``hops``.

This following example will join the source entity with entities from the ``orders`` dataset using the ``["eq","_S._id", "o.cust_id"]`` join expression and then filter the orders by ``["eq", "o.type", "BILLING"]``.

.. code-block:: json

    ["hops", {
    "datasets": ["orders o"],
      "where":
      [
        ["eq", "_S._id", "o.cust_id"],
        ["eq", "o.type", "BILLING"]
      ]
    }
   ]


.. note::
  It is important to mention that only ``eq`` functions will be treated as join expressions.

  All other function are treated as filter expressions. For an ``eq`` to be a join expression it will have to refer to variables from two different datasets.
