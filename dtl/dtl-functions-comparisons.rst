Comparisons
===========

.. _eq_dtl_function:

``eq``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
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

.. _gt_dtl_function:

``gt``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than the second argument.
     - | ``["gt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than 42.

.. _gte_dtl_function:

``gte``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is greater
         than or equal the second argument.
     - | ``["gte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value greater
         than or equal 42.

.. _lt_dtl_function:

``lt``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         the second argument.
     - | ``["lt", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than 42.

.. _lte_dtl_function:

``lte``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
       |
       | Compares the *first value* returned by the two value
         expressions. Returns *true* if the first argument is less than
         or equal the second argument.
     - | ``["lte", "_S.age", 42]``
       |
       | The source entity's ``age`` field must have a value less
         than or equal 42.

.. _neq_dtl_function:

``neq``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{2}
       |
       | Coerces the values returned from the value expressions into
         list and compares those lists. Returns ``false`` if the two
         arguments given are equal.
     - | ``["neq", "_S.age", 42]``
       |
       | The source entity's age field must *not* have the value 42.
