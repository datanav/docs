Strings
=======

.. _string_dtl_function:

``string``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Translates all non-null input values to strings.

       .. NOTE::

          Complex types like list and dict are JSON encoded (no transit encoding).
          Bytes are decoded to strings using ``utf-8`` encoding.
     - | ``["string", 1]``
       |
       | Returns one string: ``"1"``.
       |
       | ``["string", "hello"]``
       |
       | Returns one string: ``"hello"``.
       |
       | ``["string", null]``
       |
       | Returns ``null``.
       |
       | ``["string",``
       |   ``["list", "abc", ["list", 1, 2, 3],``
       |     ``{"b": 2, "a": 1}, ["uri", "http://www.example.org/"],``
       |       ``124.4, 12345]]``
       |
       | Returns a list of strings:
       |
       | ``["abc", "[1, 2, 3]", "{\"a\": 1, \"b\": 2}",``
       |   ``"http://www.example.org/", "124.4", "12345"]``.

.. _is_string_dtl_function:

``is-string``
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a string literal or if
         it is a list, that the first element
       | in the list is a string
       |
     - | ``["is-string", "foo:bar"]``
       |
       | Returns true.
       |
       | ``["is-string", 1]``
       |
       | Returns false.
       |
       | ``["is-string", ["list", "foo:bar", 12345]]``
       |
       | Returns true
       |
       | ``["is-string", ["list", 1, "foo:bar"]]``
       |
       | Returns false

.. _upper_dtl_function:

``upper``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the uppercase version of its input strings.
         Non-string values are ignored.
     - | ``["upper", ["list", "a", "b", "c"]]``
       |
       | Returns ``["A", "B", "C"]``.
       |
       | ``["upper", "_S.name"]``
       |
       | Returns an uppercased version of the source entity's name.

.. _lower_dtl_function:

``lower``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the lowercase version of its input strings.
         Non-string values are ignored.
     - | ``["lower", ["list", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["lower", "_S.name"]``
       |
       | Returns a lowercased version of the source entity's name.

.. _length_dtl_function:

``length``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the length (number of characters) of its input strings.
         Non-string values are ignored.
     - | ``["length", ["list", "", "a", "bb", "ccc"]]``
       |
       | Returns ``[0, 1, 2, 3]``.
       |
       | ``["length", "_S.name"]``
       |
       | Returns the length of the source entity's name.

.. _concat_dtl_function:

``concat``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{>1})
       |
       | Returns a concatenated string of its input strings.
         Non-string values are ignored.
     - | ``["concat", ["list", "a", "b", "c"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["concat", "_S.tags"]``
       |
       | Returns a concatenated version of the source entity's tags.
       |
       | ``["concat", "Hello ", "_S.name", "!"]``
       |
       | Returns ``"Hello John!"`` if the ``name`` property is ``John``.
       |
       | ``["concat", "a", ["list", "b", "c"], "d", 123, ["list", "!"]]``
       |
       | Returns ``"abcd!"``.
       |
       | ``["concat", 123, 3.14]``
       |
       | Returns ``""``, because non-string values are ignored.

.. _join_dtl_function:

``join``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   SEPARATOR(string{1})
       |   VALUES(value-expression{1})
       |
       | Returns a string created by joining its input strings by SEPARATOR.
         Non-string values are ignored.
     - | ``["join", "-", ["list", "a", "b", 123, "c"]]``
       |
       | Returns ``"a-b-c"``.
       |
       | ``["join", "-", "_S.tags"]``
       |
       | Returns a joined string of the source entity's tags separated by dashes.

.. _split_dtl_function:

``split``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   SEPARATOR(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a list of strings created by splitting its input strings by SEPARATOR.
         Non-string values are ignored.
     - | ``["split", "-", "a-b-c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["split", "", "abc"]``
       |
       | Returns ``["a", "b", "c"]``.
       | ``["split", "", ["list", "ab", "cd", "e"]]``
       |
       | Returns ``["a", "b", "c", "d", "e"]``.
       |
       | ``["split", "-", ["list", "a-b", "c-d", "e"]]``
       |
       | Returns ``["a", "b", "c", "d", "e"]``.
       |
       | ``["split", "-", "_S.uuid"]``
       |
       | Returns a list of strings of the source entity's tags separated by dashes.

.. _strip_dtl_function:

``strip``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from both sides. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["strip", ["list", " ab ", "cd ", "ef"]]``
       |
       | Returns ``["ab", "cd", "ef"]``.
       |
       | ``["strip", "  abc"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["strip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed.
       |
       | ``["strip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123", "456"]``.

.. _lstrip_dtl_function:

``lstrip``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the left side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["lstrip", ["list", " ab ", "cd ", "ef"]]``
       |
       | Returns ``["ab ", "cd ", "ef"]``.
       |
       | ``["lstrip", "  abc"]]``
       |
       | Returns ``"abc"``.
       |
       | ``["lstrip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed
         from the left.
       |
       | ``["lstrip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123xyx", "456yx"]``.

.. _rstrip_dtl_function:

``rstrip``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   CHARACTERS(string{0|1})
       |   VALUES(value-expression{1})
       |
       | Returns a version of its input strings where characters in CHARACTERS are removed
         from the right side. Non-string values are ignored. The default value of
         CHARACTERS is all whitespace characters.
     - | ``["rstrip", ["list", " ab ", "cd ", "ef"]]``
       |
       | Returns ``[" ab", "cd", "ef"]``.
       |
       | ``["rstrip", "  abc"]]``
       |
       | Returns ``"  abc"``.
       |
       | ``["rstrip", "_S.name"]``
       |
       | Returns a stripped version of the source entity's name where whitespace is removed
         from the right.
       |
       | ``["rstrip", "xy", ["list", "123xyx", "xy456yx"]]``
       |
       | Returns ``["123", "xy456"]``.

.. _ljust_dtl_function:

``ljust``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   WIDTH(integer-expression{1})
       |   FILL_CHARACTER(character-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns a left-justified version of its input strings. The WIDTH defines the minimum
         length of the returned strings. If the input strings are longer than WIDTH, then the
         input string is returned as-is. If the input string is shorter than WIDTH then it is
         justified to the left using the FILL_CHARACTER.
       |
       | Non-string values are ignored. If the WIDTH is not an integer or FILL_CHARACTER is
         not a single character then the function returns ``null``.
     - | ``["ljust", 10, "0", "123"]``
       |
       | Returns ``"1230000000"``.
       |
       | ``["ljust", 5, " ", ["list", "abc", "def", "ghijklm"]]``
       |
       | Returns ``["abc  ", "def  ", "ghijklm"]``.

.. _rjust_dtl_function:

``rjust``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   WIDTH(integer-expression{1})
       |   FILL_CHARACTER(character-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns a right-justified version of its input strings. The WIDTH defines the minimum
         length of the returned strings. If the input strings are longer than WIDTH, then the
         input string is returned as-is. If the input string is shorter than WIDTH then it is
         justified to the right using the FILL_CHARACTER.
       |
       | Non-string values are ignored. If the WIDTH is not an integer or FILL_CHARACTER is
         not a single character then the function returns ``null``.
     - | ``["rjust", 10, "0", "123"]``
       |
       | Returns ``"0000000123"``.
       |
       | ``["rjust", 5, " ", ["list", "abc", "def", "ghijklm"]]``
       |
       | Returns ``["  abc", "  def", "ghijklm"]``.

.. _replace_dtl_function:

``replace``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   (REPLACEMENTS(dict{1}) or
            (OLD_STRING(string{1})
             NEW_STRING(string{1})))
       |   VALUES(value-expression{1})
       |
       | Replaces occurrences of OLD_STRING with NEW_STRING in VALUES, or replaces the keys
         in the REPLACEMENT dict with the respective values. Non-string values
         are ignored.
     - | ``["replace", "http://", "https://",``
       |   ``"http://www.sesam.io/"]``
       |
       | Returns ``"https://www.sesam.io/"``.
       |
       | ``["replace", ":", ".", "_S.date"]]``
       |
       | Returns a date string where the colon has been replaced by a period.
       |
       | ``["replace", {"Hello": "HELLO", "world": "WORLD"}, "Hello world!"]]``
       |
       | Returns ``"HELLO WORLD!"``.
       |
       | ``["replace", ["dict", "a", "A", "b", "B"], "abc"]]``
       |
       | Returns ``"ABc"``.

.. _substring_dtl_function:

``substring``
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   START_INDEX(integer{1})
       |   END_INDEX(integer{0|1})
       |   VALUES(value-expression{1})
       |
       | Extracts the substring between START_INDEX and END_INDEX. If the indexes are negative they start from the end.

     - | ``["substring", 2, 4, "abcdef"]``
       |
       | Returns ``"cd"``.
       |
       | ``["substring", 2, "abcdef"]``
       |
       | Returns ``"cdef"``.
       |
       | ``["substring", -3, -1, "abcdef"]``
       |
       | Returns ``"de"``.

.. _matches_dtl_function:

``matches``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PATTERN(string{1})
       |   VALUES(value-expression{1})
       |
       | Returns true if all the values in VALUES match the pattern in PATTERN. The '*' and '?'
         wildcard characters can be used. Non-string values are not matched and will cause the
         function to return false. If PATTERN contains multiple string values then only the
         first one is used.
     - | ``["matches", "a*p*a", ["list", "alpha", "alpaca"]]``
       |
       | Returns ``true``.
       |
       | ``["matches", "*_sport", "_S.tags"]``
       |
       | Returns ``true``, unless ``_S.tags`` is empty or ``null``, if all the tags that have a "_sport" suffix.
       |
       | ``["matches", "*", null]``
       |
       | Returns ``false``.
       |
       | ``["matches", "*", ["list"]]``
       |
       | Returns ``false``.
