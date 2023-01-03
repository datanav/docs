.. _joins:

How joins work
==============

Given two entities ``A`` and ``B`` bound to the dataset aliases ``a``
and ``b`` in the expressions below:

.. code-block:: json

   {
     "_id": "A",
     "value": 1,
     "values": [1, 2, 4, 5]
   }

.. code-block:: json

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

.. important::

  The rule for joins is very simple: *if any of the values overlap, then the join succeeds*.

All of the four joins given above succeed for the two entities because
they all have overlapping values, i.e. the values ``1`` and ``4``.

Join expressions that contain functional expressions work the same
way, e.g. ``["eq", ["+", "a.value", 2], "b.values"]`` succeeds as ``3``
is a value shared by both.

If you need to do joins with composite keys then the :ref:`tuples <tuples_dtl_function>` DTL function is useful. Using composite keys is almost always a better choice than having multiple individual joins as the former will have better precision.

.. admonition:: Good to know

   ``null`` values and deleted entities are not indexed, so they are not traversed by joins.

.. NOTE::

   It is only ``eq`` functions that reference a single dataset alias in both left and right arguments that are considered join functions.

   There must be exactly one unique dataset alias reference in each ``eq`` argument.
