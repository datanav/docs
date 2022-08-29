Tuples
======

.. _tuples_dtl_function:

``tuples``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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
