Boolean logic
=============


.. _and_dtl_function:

``and``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns true only if all arguments evaluate to true.
     - | ``["and",``
       |    ``["gt", "_S.age", 26],``
       |    ``["eq", "_S.gender", "male"]]``
       |
       | Age must be greater than 26 and the gender must be male.

.. _or_dtl_function:

``or``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* boolean-expression{>0}
       |
       | Takes at least one boolean expression argument.
         Returns true if any of the arguments evaluate to true.
     - | ``["or",``
       |   ``["eq", "_S.category", "A"],``
       |   ``["eq", "_S.category", "B"]]``
       |
       | The category field must contain "A" or "B".

.. _not_dtl_function:

``not``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* boolean-expression{>0}
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

``all``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

``any``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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
