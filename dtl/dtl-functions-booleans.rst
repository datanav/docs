Booleans
========

.. _is_boolean_dtl_function:

``is-boolean``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a boolean literal or if
         it is a list, that the first element in the list is a boolean
       |
     - | ``["is-boolean", false]``
       |
       | Returns true.
       |
       | ``["is-boolean", "True"]``
       |
       | Returns false.
       |
       | ``["is-boolean", ["list", true, "12345"]]``
       |
       | Returns true.
       |
       | ``["is-boolean", ["list", "12345", true]]``
       |
       | Returns false.
       |
       | ``["is-boolean", ["list", ["boolean", "FALSE"], 1234]]``
       |
       | Returns true.

.. _boolean_dtl_function:

``boolean``
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
       | Translates all non-null input values to booleans. If no default value expression
         is given, values that don't parse as boolean values will be silently
         ignored. If not, the evaluated value from the default expression will
         be used as a replacement value. String literals are case insensitive,
         and the supported values are "true" and "false".
       |
     - | ``["boolean", "false"]``
       |
       | Returns one boolean: false.
       |
       | ``["boolean", null]``
       |
       | Returns ``null``.
       |
       | ``["boolean",``
       |   ``["list", "true", "~rhttp://www.example.org/",``
       |     ``"True", false, 1234]]``
       |
       | Returns a list of booleans: [true, true, false]. The URI and integer
         values are ignored.
       |
       | ``["boolean", ["boolean", false],``
       |   ``["list", "true", "~rhttp://www.example.org/",``
       |     ``"124.4", "FALSE"]]``
       |
       | Returns a list of booleans: [true, false, false, false]. The URI value
         and the string value are replaced with the literal value: false
       |
       | ``["boolean", ["string", "n/a"],``
       |   ``["list", "true", "~rhttp://www.example.org/", "124.4"]]``
       |
       | Returns a list of booleans: [true, "n/a", "n/a"]. The URI value and
         the string value are replaced with the literal value "n/a"
       |
       | ``["boolean", ["string", "_."],``
       |   ``["list", "true", "~rhttp://www.example.org/", "False"]]``
       |
       | Returns a list of booleans: [true, "http://www.example.org/", false].
         The URI value is replaced with its string cast.
