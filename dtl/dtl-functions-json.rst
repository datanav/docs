JSON
====

.. _json_dtl_function:

``json``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to JSON strings (no transit encoding).
         The keys of dicts are sorted lexically.
     - | ``["json", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["json", "hello"]``
       |
       | Returns one string: ``"\"hello\""``.
       |
       | ``["json",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["\"abc\"", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"http://www.example.org/", "124.4", "12345"]``.

.. _json_transit_dtl_function:

``json-transit``
----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all input values to transit encoded JSON strings.
         The keys of dicts are sorted lexically. This function behaves like
         the ``json`` function, except that it transit encodes values.
     - | ``["json-transit", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["json-transit", "hello"]``
       |
       | Returns one string: ``"\"hello\""``.
       |
       | ``["json-transit",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["\"abc\"", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"~rhttp://www.example.org/", "124.4", "12345"]``.

.. _json_parse_dtl_function:

``json-parse``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Parses all input values as JSON strings (no transit decoding).
       |
       | If no default value expression is given, then invalid values that don't
         parse as valid JSON will be silently ignored. If not, the evaluated value
         from the default expression will be used as a replacement value.

     - | ``["json-parse", "1"]``
       |
       | Returns one number: ``1``.
       |
       | ``["json-parse", "\"hello\""]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["is-uri", ["json-parse",``
       |   ``"\"~rhttp://www.example.org/\""]]``
       |
       | Returns ``false``.
       |
       | ``["json-parse", "{\"a\": 1, \"b\": 2}"``
       |
       | Returns a dictionary: ``{"a": 1, "b": 2}",``
       |
       | ``["json-parse", "hello"]``
       |
       | Returns ``null`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-parse",``
       |   ``["list", "hello", "123", "null",``
       |     ``"\"abc\"", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``[123, null, "abc", "~rhttp://example.org/"]``. Note that ``null``
         is a valid JSON expression, so ``null`` is included in the result list. Note
         also that ``"~rhttp://www.example.org/"`` is not parsed as a URI since we don't do
         transit decoding here.
       |
       | ``["json-parse", "no-value", "hello"]``
       |
       | Returns ``"no-value"`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-parse", "no-value", "null"]``
       |
       | Returns ``null`` because ``"null"`` is a valid JSON string.

.. _json_transit_parse_dtl_function:

``json-transit-parse``
----------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(default-value-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Parses all input values as transit-encoded JSON strings.
       |
       | If no default value expression is given, then invalid values that don't
         parse as valid JSON will be silently ignored. If not, the evaluated value
         from the default expression will be used as a replacement value.
       |
       | This function behaves like
         the ``json-parse`` function, except that it transit decodes values.
     - | ``["json-transit-parse", "1"]``
       |
       | Returns one number: ``1``.
       |
       | ``["json-transit-parse", "\"hello\""]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["is-uri", ["json-transit-parse",``
       |   ``"\"~rhttp://www.example.org/\""]]``
       |
       | Returns ``true``.
       |
       | ``["json-transit-parse", "hello"]``
       |
       | Returns ``null`` because ``hello`` is not a valid JSON string.
       |
       | ``["json-transit-parse",``
       |   ``["list", "hello", "123", "null",``
       |     ``"\"abc\"", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``[123, null, "abc", "~rhttp://example.org/"]``. Note that ``null``
         is a valid JSON expression, so ``null`` is included in the result list. Note
         also that "~rhttp://www.example.org/" is parsed as a URI since we are
         doing transit decoding.
       |
       | ``["json-transit-parse",``
       |   ``"no-value", "~rhttp://example.org/"]``
       |
       | Returns ``"no-value"`` because ``~rhttp://example.org/`` is not
         a valid JSON string.
       |
       | ``["is-uri",``
       |   ``["json-transit-parse",``
       |     ``"no-value", "\"~rhttp://example.org/\""]]``
       |
       | Returns ``true`` because ``"\"~rhttp://example.org/\""`` is a valid JSON string
         and the return value is a URI.
