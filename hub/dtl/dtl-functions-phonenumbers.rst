Phonenumbers
============

.. _phonenumber_parse_dtl_function:

``phonenumber-parse``
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DEFAULT_REGION(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to phonenumber values. The values must be strings
         or numbers that represent a valid phonenumber. Any values that don't parse as phonenumbers will
         be ignored. Phone numbers are represented as URI values on the
         `RFC3966 <https://datatracker.ietf.org/doc/html/rfc3966#section-5.1.4>`_ format. Example: "~rtel:+47-22-22-22-22"

       |
       | If the phonenumber doesn't start with a country code (for instance "+47") the DEFAULT_REGION argument will
         be used assign a country code.

     - | ``["phonenumber-parse", "+4722222222"]``
       |
       | Returns one phonenumber value: "~rtel:+47-22-22-22-22".
       |
       | ``["phonenumber-parse", "NO", "22225555"]``
       |
       | Returns one phonenumber value: "~rtel:+47-22-22-55-55".
       |
       | ``["phonenumber-parse", "NO", ["list", "22222222", "22225555"]]``
       |
       | Returns two phonenumber values: ["~rtel:+47-22-22-22-22", "~rtel:+47-22-22-55-55"]




.. _phonenumber_format_dtl_function:

``phonenumber-format``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FORMAT_STRING(string{1})
       |   VALUES(value-expression{1})
       |
       | Converts phonenumber values to strings. The values must be URI values on the
         `RFC3966 <https://datatracker.ietf.org/doc/html/rfc3966#section-5.1.4>`_ format. Example: "~rtel:+47-22-22-22-22"
       |
       | ``FORMAT_STRING`` can be one of the following values:
       |
       |   ``e164``
       |   ``rfc3966``
       |   ``national``
       |   ``international``
       |   ``national-e164``
       |   ``isocode``
       |   ``country-code``
       |

     - | ``["phonenumber-format", "e164", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one phonenumber string: "4722222222".
       |
       | ``["phonenumber-format", "national-e164", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one phonenumber string: "22222222".
       |
       | ``["phonenumber-format", "national", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one phonenumber string: "22 22 22 22".
       |
       | ``["phonenumber-format", "international", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one phonenumber string: "+47 22 22 22 22".
       |
       | ``["phonenumber-format", "rfc3966", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one phonenumber string: "tel:+47-22-22-22-22".
       |
       | ``["phonenumber-format", "isocode", "~rtel:+47-22-22-22-22"]``
       |
       | Returns one iso region code string: "NO".
       |
       | ``["phonenumber-format", "country-code", "~rtel:+47-22-22-22-22"]``
       |
       | Returns the country code as a string: "47".
       |
       | ``["phonenumber-format", "e164", ["list", "~rtel:+47-22-22-22-22", "~rtel:+47-22-22-55-55"]]``
       |
       | Returns two phonenumber strings: ["4722222222", "4722225555"]
       |
