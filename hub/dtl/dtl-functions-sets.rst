Sets
====

.. _difference_dtl_function:

``difference``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the difference of the values in VALUES1 and VALUES2, i.e. the values
         that are in VALUES1, but not in VALUES2. The values in VALUES1 in that does not exist in
         VALUES2 are kept in their original relative positions.
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
       |
       | ``["difference",``
       |   ``["list", "D", "A", "D", "E", "B"],``
       |   ``["list", "A", "F", "F", "B", "C"]]``
       |
       | Returns ``["D", "D", "E"]``.

.. _intersection_dtl_function:

``intersection``
----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the intersection of the values in VALUES1 and VALUES2, i.e. the values
         that are in both VALUES1 and VALUES2. The values in VALUES1 in that exist in
         VALUES2 are kept in their original relative positions.
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
       |
       | ``["intersection",``
       |    ``["list", "B", "C", "B", "D", "A"],``
       |    ``["list", "A", "F", "F", "B", "E", "B", "C"]]``
       |
       | Returns ``["B", "C", "B", "A"]``.


.. _intersects_dtl_function:

``intersects``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Same as ``intersection``, but returns a boolean value. Returns true if the two
         arguments have values in common.
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

.. _union_dtl_function:

``union``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES1(value-expression{1})
       |   VALUES2(value-expression{1})
       |
       | Returns the union of the two sets VALUES1 and VALUES2, i.e. the values that
         are either in VALUES1 or in VALUES2.
     - | ``["union",``
       |     ``["list", "A", "B"], ["list", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union", "A", ["list", "B", "C"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["union",``
       |     ``["list", "B", "C", "B", "D", "A"],``
       |     ``["list", "A", "F", "F", "B", "E", "B", "C"]]``
       |
       | Returns ``["B", "C", "D", "A", "F", "E"]``.
