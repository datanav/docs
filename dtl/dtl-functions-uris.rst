URIs
====

.. _uri_dtl_function:

``uri``
-------
.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates input values to URIs. Only strings in VALUES will be
         cast to URIs. Note that *no* URI escaping is done on the strings.
     - | ``["uri", "http://www.example.org/"]``
       |
       | Returns one URI.
       |
       | ``["uri",``
       |    ``["list", "http://www.example.org/",``
       |       ``"http://www.sesam.io/", 12345]]``
       |
       | Returns a list of two URIs. The number is silently ignored because
         it is not a string.

.. _is_uri_dtl_function:

``is-uri``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a URI literal, or if it is
         a list, that the first element in the list is a URI.
     - | ``["is-uri", ["uri", "foo:bar"]]``
       |
       | Returns ``true``.
       |
       | ``["is-uri", "foo:bar"]``
       |
       | Returns ``false``.
       |
       | ``["is-uri", ["list", ["uri", "foo:bar"], 12345]]``
       |
       | Returns ``true``.
       |
       | ``["is-uri", ["list", 1, ["uri", "foo:bar"]]]``
       |
       | Returns ``false``.

.. _url_quote_dtl_function:

``url-quote``
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   SAFE_CHARS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns the URL quoted versions of any string or list of strings in the
         argument list. Any non-strings are ignored and is not returned in the
         result. Returns either a single string (if the input is a single
         string literal) or a list (of strings).
       |
       | If you want some ASCII characters to not be encoded, e.g. the slash character ``/``,
         then specify the ``SAFE_CHARS`` argument. The default value is "". The ``SAFE_CHARS``
         argument must be a string that contains zero or more ASCII characters that should
         not be encoded. Note that this only is applicable for ASCII characters.
     - | ``["url-quote", "/foo bar/baz"]``
       |
       | Returns ``%2Ffoo%20bar%2Fbaz``. Note that the ``/`` characters have been encoded.
         To avoid this you can add the SAFE_CHARS argument:
       |
       | ``["url-quote", "/", "/foo bar/baz"]``
       |
       | Returns ``/foo%20bar/baz``.
       |
       | ``["url-quote",``
       |   ``["list", "å", 1, 2,``
       |     ``["uri", "http://example.com"], "foo bar"]]``
       |
       | Returns ``["%C3%A5", "foo%20bar]``.

.. _url_unquote_dtl_function:

``url-unquote``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the URL unquoted versions of any string or list of strings in the
         argument list. Any non-strings are ignored and is not returned in the
         result. Returns either a single string (if the input is a single
         string literal) or a list (of strings).
       |
     - | ``["url-unquote", "%2Ffoo%20bar%2Fbaz"]``
       |
       | Returns ``/foo bar/baz``.
       |
       | ``["url-quote",``
       |   ``["list", 1, "%C3%A5", ["uri", "http://example.com"], "foo%20bar"]``
       |
       | Returns ``["å", "foo bar"]``.
