Math
====

The ``plus``, ``minus``, ``multiply``, ``divide``, ``mod`` and ``pow`` functions are ``map``-style functions that apply the first
argument to one or more values. For "natural order" math operators that operate on single numbers, use the symbolic
equivalents ``+``, ``-``, ``*``, ``/``, ``%`` and ``^``. If the argument(s) to the natural order functions
are lists, the first value is used. If either argument evaluates to ``null``, the result will also be
``null``.

.. _minus_symbol_dtl_function:

``-``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _multiply_symbol_dtl_function:

``*``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _divide_symbol_dtl_function:

``/``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _mod_symbol_dtl_function:

``%``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _pow_symbol_dtl_function:

``^``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _plus_symbol_dtl_function:

``+``
-----

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _abs_dtl_function:

``abs``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _ceil_dtl_function:

``ceil``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _cos_dtl_function:

``cos``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _divide_dtl_function:

``divide``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _floor_dtl_function:

``floor``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _minus_dtl_function:

``minus``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _mod_dtl_function:

``mod``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _multiply_dtl_function:

``multiply``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _plus_dtl_function:

``plus``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _pow_dtl_function:

``pow``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _round_dtl_function:

``round``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _sin_dtl_function:

``sin``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _sqrt_dtl_function:

``sqrt``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
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

.. _tan_dtl_function:

``tan``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUE(numeric-expression{1})
       |
       | Takes a list of VALUES and returns the tangens of the value, where value is in
         radians. Note that values approaching very close to multiples of PI/2 will be
         undefined (+-infinite) and the result will be a ``None`` value.
     - | ``["tan", ["list", 0, 3.14159265]]``
       |
       | Returns ``[0.0, ~0.0]``.
