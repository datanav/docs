Numbers
=======

.. _is_integer_dtl_function:

``is-integer``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is an integer literal or
         if it is a list, that the first element in the list is an integer
       |
     - | ``["is-integer", 1]``
       |
       | Returns ``true``.
       |
       | ``["is-integer", "1"]``
       |
       | Returns ``false``.
       |
       | ``["is-integer", ["list", 1, "12345"]]``
       |
       | Returns ``true``.
       |
       | ``["is-integer", ["list", "1", 2]]``
       |
       | Returns ``false``.
       |
       | ``["is-integer", ["list", ["integer", "1"], 2]]``
       |
       | Returns ``true``.

.. _integer_dtl_function:

``integer``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to integers. If no default value expression
         is given, values that don't parse as integers will be silently ignored.
         If not, the evaluated value from the default expression will be used
         as a replacement value.
       |
       | Values that starts with ``"0x"`` are parsed as hexadecimal values in two's complement
         format.
     - | ``["integer", "1"]``
       |
       | Returns one integer: 1.
       |
       | ``["integer",``
       |   ``["list", "1", "~rhttp://www.example.org/", 124.4, 12345]]``
       |
       | Returns a list of integers: [1, 124, 12345]. The URI value is ignored.
       |
       | ``["integer", ["integer", 0],``
       |    ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, 0, 0, 12345]. The URI value and the
         string value are replaced with the literal value 0
       |
       | ``["integer", ["string", "n/a"],``
       |   ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "n/a", "n/a", 12345]. The URI value
         and the string value are replaced with the literal value "n/a"
       |
       | ``["integer", ["string", "_."],``
       |   ``["list", "1", "~rhttp://www.example.org/", "10^2", 12345]]``
       |
       | Returns a list of integers: [1, "http://www.example.org/", "10^2", 12345].
         The URI value and the non-integer string value are replaced with the
         their respective string casts.
       |
       | ``["integer", "0x00ff"]``
       |
       | Returns one integer: 255.
       |
       |
       | ``["integer", "0xff"]``
       |
       | Returns one integer: -1.
       |

.. _is_decimal_dtl_function:

``is-decimal``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a decimal literal or
         if it is a list, that the first element in the list is a decimal
       |
     - | ``["is-decimal", 1.0]``
       |
       | Returns false (it is a float literal).
       |
       | ``["is-decimal", ["decimal", "1.23"]]``
       |
       | Returns true.
       |
       | ``["is-decimal", 1]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", 1.0, "12345"]]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", "1.0", 2.0]]``
       |
       | Returns false.
       |
       | ``["is-decimal", ["list", ["decimal", "-1.0"], 1234]]``
       |
       | Returns true.

.. _decimal_dtl_function:

``decimal``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to decimals (a fractional number with
         unlimited precision). If no default value expression is given,
         values that don't parse as decimal values will be silently ignored.
         If not, the evaluated value from the default expression will be
         used as a replacement value.
       |
     - | ``["decimal", "1.0"]``
       |
       | Returns one decimal value: 1.0
       |
       | ``["decimal",``
       |   ``["list", "1.0", "~rhttp://www.example.org/", 2.2, "one"]]``
       |
       | Returns a list of decimal values: [1.0, 2.2]. The URI and
         non-decimal string value are ignored.
       |
       | ``["decimal", ["boolean", false],``
       |   ``["list", "1.0", 2.1, "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns [1.0, 2.1, false, 124.4, false]. The URI value and the
         non-decimal string value are replaced with the literal value: false
       |
       | ``["decimal", ["string", "n/a"],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns [1.0, 2.0, "n/a", 124.4]. The URI value is replaced with the
       | literal value "n/a".
       |
       | ``["decimal", ["string", "_."],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "2.5"]]``
       |
       | Returns [1.0, 2.0, "http://www.example.org/", 2.5]. The URI value
         is replaced with its string cast.

.. _is_float_dtl_function:

``is-float``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a float literal or
         if it is a list, that the first element in the list is a float value
       |
     - | ``["is-float", 1.0]``
       |
       | Returns true.
       |
       | ``["is-float", ["decimal", "1.23"]]``
       |
       | Returns false (it is a decimal literal).
       |
       | ``["is-float", 1]``
       |
       | Returns false.
       |
       | ``["is-float", ["list", 1.0, "12345"]]``
       |
       | Returns true.
       |
       | ``["is-float", ["list", "1.0", 2.0]]``
       |
       | Returns false.
       |
       | ``["is-float", ["list", ["decimal", "-1.0"], 123.4]]``
       |
       | Returns false.

.. _float_dtl_function:

``float``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to floats (a  IEEE 754 binary 64 format).
         if no default value expression is given,
         values that don't parse as float values will be silently ignored.
         If not, the evaluated value from the default expression will be
         used as a replacement value. Note that if you cast decimals to floats
         you can lose precision.
       |
     - | ``["float", "1.0"]``
       |
       | Returns one float value: 1.0
       |
       | ``["float",``
       |   ``["list", "1.0", "~rhttp://www.example.org/", 2.2, "one"]]``
       |
       | Returns a list of float values: [1.0, 2.2]. The URI and
         non-numeric string value are ignored.
       |
       | ``["float", ["boolean", false],``
       |   ``["list", "1.0", 2.1, "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns [1.0, 2.1, false, 124.4, false]. The URI value and the
         non-numeric string value are replaced with the literal value: false
       |
       | ``["float", ["string", "n/a"],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns [1.0, 2.0, "n/a", 124.4]. The URI value is replaced with the
       | literal value "n/a".
       |
       | ``["float", ["string", "_."],``
       |   ``["list", "1.0", 2.0, "~rhttp://www.example.org/", "2.5"]]``
       |
       | Returns [1.0, 2.0, "http://www.example.org/", 2.5]. The URI value
         is replaced with its string cast.

.. _hex_dtl_function:

``hex``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to a string containing an hexadecimal representation of the value
         in two's complement format.
       | Values that don't parse as integers will be silently ignored.
     - | ``["hex", 1]``
       |
       | Returns one string: ``"0x01"``.
       |
       | ``["hex", 255]``
       |
       | Returns one string: ``"0x00ff"``.
       |
       | ``["hex", -1]``
       |
       | Returns one string: ``"0xff"``.
       |
       | ``["hex",``
       |   ``["list", 1, "~rhttp://www.example.org/", 124.4, 12345]]``
       |
       | Returns a list of strings: ["0x1", "0x3039"]. The URI value and the float value are ignored.
