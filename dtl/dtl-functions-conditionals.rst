Conditionals
============

.. _if_dtl_function:

``if``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

``case-eq``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

``case``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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
