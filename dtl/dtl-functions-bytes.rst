Bytes
=====

.. _bytes_dtl_function:

``bytes``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input string values to bytes using ``utf-8`` encoding.
       |
     - | ``["bytes", "abc"]``
       |
       | Returns one bytes object: ``~bYWJj``.

.. _is_bytes_dtl_function:

``is-bytes``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a bytes literal or value or if
         it is a list, that the first element in the list is a bytes type value or literal
       |
     - | ``["is-bytes", ["bytes", "abc"]]``
       |
       | Returns true.
       |
       | ``["is-bytes", "~bYWJj"]``
       |
       | Returns true.
       |
       | ``["is-bytes", "some-string"]``
       |
       | Returns false.
       |
       | ``["is-bytes", ["list", "~bYWJj", "12345"]]``
       |
       | Returns true.
       |
       | ``["is-bytes", ["list", "12345", "~bYWJj"]]]``
       |
       | Returns false.
       |

.. _base64_encode_dtl_function:

``base64-encode``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the base64 encoded version of its input bytes.
         Non-bytes values are ignored.
     - | ``["base64-encode", ["bytes", "abc"]]``
       |
       | Returns ``"YWJj"``.
       |
       | ``["base64-encode", ["list", 1, ["bytes", "abc"], 2, ["bytes", "def"], 3]]``
       |
       | Returns ``["YWJj", "ZGVm"]``.
       |


.. _base64_decode_dtl_function:

``base64-decode``
-----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the base64 decoded version of its input strings.
         Non-string values and non-base64 encoded values are ignored.
     - | ``["base64-decode", "YWJj"]``
       |
       | Returns ``"~babc"``.
       |
       | ``["base64-decode", ["list", 1, "YWJj", 2, "ZGVm", 3]]``
       |
       | Returns ``["~bYWJj", "~bZGVm"]``.
       |
       | (Note that the JSON string representation of a bytes object is represented as a base64 encoded string, hence
       | the similar looking output and input)
