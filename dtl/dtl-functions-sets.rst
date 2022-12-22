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
