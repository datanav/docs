Lists
=====

.. _combine_dtl_function:

``combine``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{>=1})
       |
       | Combines the VALUES into a single list.

     - | ``["combine", null]``
       | Returns ``[]``
       |
       | ``["combine", 1]``
       | Returns ``[1]``
       |
       | ``["combine", 1, 4]``
       | Returns ``[1, 4]``
       |
       | ``["combine", 1, ["list", 2, 3]]``
       | Returns ``[1, 2, 3]``
       |
       | ``["combine", 1, ["list", 2, 3, ["list", 4]]]``
       | Returns ``[1, 2, 3, [4]]``
       |
       | ``["combine", ["list", 1, 2], ["list", 3, 4], 5]``
       | Returns ``[1, 2, 3, 4, 5]``

.. _count_dtl_function:

``count``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the number of elements in VALUES.
     - | ``["count", ["list", 2, 4, 6]]``
       |
       | Returns ``3``.
       |
       | ``["count", null]]``
       |
       | Returns ``0``.
       |
       | ``["count", 123]]``
       |
       | Returns ``1``.
       |
       | ``["count", "_S.orders"]]``
       |
       | Returns the the number of orders.

.. _distinct_dtl_function:

``distinct``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns a list of distinct values in VALUES, i.e. it returns a list
         where duplicates have been removed from VALUES. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used to check for duplicates. Note that even though FUNCTION is
         given it is the value in VALUES that is returned.
     - | ``["distinct", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[4, 2, 5, 3]``.
       |
       | ``["distinct", "_S.tags"]]``
       |
       | Returns a deduplicated list of tags.
       |
       | ``["distinct", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns a list of order lines, but only one per unique EAN, i.e. product
         number.

.. _enumerate_dtl_function:

``enumerate``
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   START(integer-expression{0|1})
       |   VALUES(value-expression{1})
       |
       | Enumerates the values by returning dictionaries with ``key``
         and ``value`` keys. ``value`` contains the value and ``key`` the
         enumerator count. The enumeration counter starts at START and uses an
         increment of 1. The default value of START is 0.
     - | ``["enumerate", "a"]``
       |
       | Returns ``{"key": 0, "value": "a"}``.
       |
       | ``["enumerate", 1, "a"]``
       |
       | Returns ``{"key": 1, "value": "a"}``.
       |
       | ``["enumerate", ["list", 17, 32, 21]]``
       |
       | Returns ``[{"key": 0, "value": 17},``
       |    ``{"key": 1, "value": 32},``
       |    ``{"key": 2, "value": 21}]``.
       |
       | ``["enumerate", 2, ["list", 17, 32, 21]]``
       |
       | Returns ``[{"key": 2, "value": 17},``
       |   ``{"key": 3, "value": 32},``
       |   ``{"key": 4, "value": 21}]``.

.. _filter_dtl_function:

``filter``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | Filters out the the values in VALUES for which the FUNCTION expression
         does *not* evaluate to *true*.
     - | ``["filter", ["gt", "_.age", 42],``
       |     ``["list", {"age": 30}, {"age": 50}, {"age": 40}]]``
       |
       | Returns ``[{"age": 50}]``.
       |
       | ``["filter", ["gt", "_.amount", 100], "_S.orders"]]``
       |
       | Returns the order entities that have an amount of more than 100.

.. _first_dtl_function:

``first``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the first value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["first", ["list", "a", "b", "c"]]``
       |
       | Returns ``"a"``.
       |
       | ``["first", "_S.tags"]``
       |
       | Returns the first tag in the source entity's ``tags`` field.

.. _flatten_dtl_function:

``flatten``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Flattens its input values in VALUES. Note that it does *not* do so
         recursively. Constructs a new list.
     - | ``["flatten", ["list", 1, 2, ["list", 3, 4]]]``
       |
       | Returns ``[1, 2, 3, 4]``.
       |
       | ``["flatten",``
       |   ``["list", ["list", 1, 2],``
       |     ``["list", 3, ["list", 4], 5]]]``
       |
       | Returns ``[1, 2, 3, [4], 5]``.
       |
       | ``["flatten", ["list", "_S.sisters", "_S.brothers"]]``
       |
       | Returns a list that contains the sisters and brothers.

.. _group_by_dtl_function:

``group-by``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   KEY_FUNCTION(function-expression(0|1}
       |   STRING_FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Groups the values in VALUES by the result of executing the KEY_FUNCTION
         function on them. Returns a dictionary, where the key is the
         group key and the value is the list of values in VALUES that were
         grouped under that key.

       .. NOTE::

          The keys in the returned dict are strings only. The reason
          is that the :ref:`entity data model <entity_data_types>`
          (and `JSON <http://json.org/>`_) only supports string keys.

          The group keys are :ref:`transit encoded <extension-types>`
          JSON strings, i.e. the same kind of strings generated by the
          :ref:`json-transit <json_transit_dtl_function>` function.

          If you do not want the keys to be transit encoded JSON, then you have the
          option of specifying STRING_FUNCTION, a function that then will be used to
          generate the string key.
     - | ``["group-by", ["length", "_."],``
       |   ``["list", "phi", "alpha", "rho"]]``
       |
       | Returns ``{"3": ["phi", "rho"], "5": ["alpha"]}``.
       |
       | ``["group-by", "_.ean", "_S.orders.line_item"]]``
       |
       | Returns order lines grouped by EAN, i.e. product number.
       |
       | ``["group-by", "_.gender", "_S.people"]]``
       |
       | Returns a dictionary of people grouped by their gender.
       |
       | ``["group-by",``
       |   ``["upper", "_."], ["list", "a", "b"]]``
       |
       | Returns ``{"\"A\"": ["a"], "\"B\"": ["b"]}``. The keys are
         transit-encoded JSON strings.
       |
       | ``["group-by",``
       |   ``["upper", "_."],``
       |   ``["string", "_."], ["list", "a", "b"]]``
       |
       | Returns ``{"A": ["a"], "B": ["b"]}``. Same as above, but we specify
         a STRING_FUNCTION function that creates string keys.

.. _in_dtl_function:

``in``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |   ITEMS(value-expression{1})
       |
       | Boolean function that returns ``true`` if all values in VALUES exist in ITEMS,
         i.e. if VALUES is a subset of ITEMS. Returns false if VALUES is null or empty.
     - | ``["in", "a", ["list", "a", "b", "c"]]``
       |
       | Returns ``true``.
       |
       | ``["in", "d", ["list", "a", "b", "c"]]``
       |
       | Returns ``false``.
       |
       | ``["in", ["list", 10], 10]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list"], 10]``
       |
       | Returns ``false``.
       |
       | ``["in", null, ["list", null]]``
       |
       | Returns ``false``.
       |
       | ``["in", ["list", null], ["list", 1, null, 2]]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list", "a", "c"],``
       |   ``["list", "a", "b", "c"]]``
       |
       | Returns ``true``.
       |
       | ``["in", ["list", "a", "c", "d"],``
       |   ``["list", "a", "b", "c"]]``
       |
       | Returns ``false``.         

.. _insert_dtl_function:

``insert``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   INDEX(integer-expression{1})
       |   VALUES(value-expression{1})
       |   OBJECT(value-expression{1})
       |
       | Inserts OBJECT at INDEX in VALUES. A negative INDEX means starting from the end.

     - | ``["insert", 1, 2, 3]``
       | Returns ``[2, 3]``
       |
       | ``["insert", 1, ["list", 1, 2], ["list", 3, 4]]``
       | Returns ``[1, [3, 4], 2]``
       |
       | ``["insert", -2, ["list", 1, 2, 3], 4]``
       | Returns ``[1, 4, 2, 3]``

.. _is_empty_dtl_function:

``is-empty``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is 0.
     - | ``["is-empty", "_S.hobbies"]``
       |
       | Returns true if the source entity's ``hobbies`` field is
         empty (has no values).

.. _is_list_dtl_function:

``is-list``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a list
       |
     - | ``["is-list", ["list", "foo:bar"]]``
       |
       | Returns true.
       |
       | ``["is-list", "foo:bar"]``
       |
       | Returns false.
       |
       | ``["is-list", ["list", ["uri", "foo:bar"], 12345]]``
       |
       | Returns true
       |
       | ``["is-list", ["dict", "1", 2]]``
       |
       | Returns false.
       |
       | ``["is-list", ["items", ["dict", "1", 2]]]``
       |
       | Returns true.

.. _is_not_empty_dtl_function:

``is-not-empty``
----------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:* value-expression{1}
       |
       | Coerces the values returned from the value expressions into
         list. Returns *true* if the number of elements in the first
         argument is greater than 0.
     - | ``["is-not-empty", "_S.hobbies"]``
       |
       | Returns true if the source entity's ``hobbies`` field is not
         empty (has one or more values).

.. _last_dtl_function:

``last``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the last value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned. If VALUES is empty, then
         null is returned.
     - | ``["last", ["list", "a", "b", "c"]]``
       |
       | Returns ``"c"``.
       |
       | ``["last", "_S.tags"]``
       |
       | Returns the last tag in the source entity's ``tags`` field.

.. _list_dtl_function:

``list``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{>=0})
       |
       | Constructs a list of the values in VALUES.
     - | ``["list"]``
       |
       | Returns ``[]``.
       |
       | ``["list", "a", "b", "c"]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["list", "a", ["list", "b"], "c"]``
       |
       | Returns ``["a", ["b"], "c"]``.

.. _map_dtl_function:

``map``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each value in VALUES apply the FUNCTION function and construct a new
         list of the return values.
     - | ``["map", ["lower", "_."], ["list", "A", "B", "C"]]``
       |
       | Returns ``["a", "b", "c"]``.
       |
       | ``["map", ["distinct", "_."],``
       |   ``["list", ["list", "A", "A"],``
       |     ``["list", "B", "C"]]]``
       |
       | Returns ``[["A"], ["B", "C"]]``.

.. _map_dict_dtl_function:

``map-dict``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   KEY_FUNCTION(function-expression(1}
       |   VALUE_FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each dictionary in VALUES construct a new dictionary by applying
         the KEY_FUNCTION function and the VALUE_FUNCTION to all its key+value
         pairs. If the KEY_FUNCTION returns a non-string value then the key+value
         pair is ignored. Empty dictionaries are not returned.
     - | ``["map-dict",``
       |     ``["upper", "_."], ["plus", 1, "_."],``
       |     ``{"A": 1, "B": 2}]``
       |
       | Returns ``{"A": 2, "B": 3}``.
       |
       | ``["map-dict",``
       |     ``["if", ["gt", ["length", "_."], 2],``
       |         ``["concat", "x:", "_."]], "_.",``
       |     ``["list",``
       |         ``{"abc": 1, "ab": 2, "abcd": 3},``
       |         ``{"def": 4}, {"gh": 5}]]``
       |
       | Returns ``[{"x:abc": 1, "x:abcd": 3}, {"x:def": 4}]``.

.. _map_values_dtl_function:

``map-values``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUE_FUNCTION(function-expression(1}
       |   VALUES(value-expression{1})
       |
       | For each dictionary in VALUES apply the VALUE_FUNCTION to the
         dictionary's values. The function maps over the values of dictionaries
         and returns a list of mapped values. Non-dictionary values are ignored.
     - | ``["map-values",``
       |     ``["lower", "_."],``
       |     ``{"key1": "A", "key2": "B"}]``
       |
       | Returns ``["a", "b"]``.
       |
       | ``["map-values",``
       |     ``["lower", "_."],``
       |     ``["list", {"key1": "A", "key2": "B"}, 100,``
       |       ``{"key1": "B", "key2": "A", "key3": "C"}]]``
       |
       | Returns ``["a", "b", "b", "a", "c"]``.
       |

.. _max_dtl_function:

``max``
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
       | Returns the maximum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the maximal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["max", ["list", 4, 2, 5, 3]]``
       |
       | Returns ``5``.
       |
       | ``["max", ["list", "b", 2, "a", 3]]``
       |
       | Returns ``"b"``.
       |
       | ``["max", ["list", {"x": 1}, "b", 2, "a"]]``
       |
       | Returns ``{"x": 1}``.
       |
       | ``["max", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the highest amount.

.. _min_dtl_function:

``min``
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
       | Returns the minimum value in VALUES. If FUNCTION is given, the
         function is evaluated for each value in VALUES to, and the return
         value is used to for ordering to figure out what is the minimal value.
         Note that even though FUNCTION is given it is the value in VALUES that
         is returned.

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["min", ["list", 4, 2, 5, 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", ["list", "b", 2, "a", 3]]``
       |
       | Returns ``2``.
       |
       | ``["min", ["list", {"x": 1}, "b", "a"]]``
       |
       | Returns ``"a"``.
       |
       | ``["min", ["list", "B", "b", "A", "a"]]``
       |
       | Returns ``"A"`` (Based on `ASCII ordering <https://ascii.cl/>`_).
       |
       | ``["min", "_.amount", "_S.orders"]]``
       |
       | Returns the order with the lowest amount.

.. _nth_dtl_function:

``nth``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   INDEX(integer-expression{1})
       |   VALUES(value-expression{1})
       |
       | Returns the nth value in VALUES. If VALUES is not a sequence
         of values, then VALUES is returned only if INDEX is 0. If VALUES is
         empty or the INDEX is out of bounds, then null is returned.
         Note that INDEX is zero-based.

     - | ``["nth", 1, ["list", "a", "b", "c"]]``
       |
       | Returns ``"b"``.
       |
       | ``["nth", 5, ["list", "a", "b", "c"]]``
       |
       | Returns ``null``.
       |
       | ``["nth", 1, "_S.tags"]``
       |
       | Returns the second tag in the source entity's ``tags`` field.

.. _range_dtl_function:

``range``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   START(integer-expression{1})
       |   STOP(integer-expression{1})
       |   STEP(integer-expression{0|1})
       |
       | Returns a list of integers ranging from START (inclusive) to STOP
         (exclusive) in STEP increments. Note that STEP cannot be 0 and all
         arguments must be integers or integer expressions.
     - | ``["range", 0, 4]``
       |
       | Returns ``[0, 1, 2, 3]``.
       |
       | ``["range", 4, 0, -1]]``
       |
       | Returns ``[4, 3, 2, 1]``.

.. _reversed_dtl_function:

``reversed``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns VALUES in reversed order.
     - | ``["reversed", ["list", 1, 3, 2]]``
       |
       | Returns ``[2, 3, 1]``.
       |
       | ``["reversed", ["sorted", "_S.tags"]]``
       |
       | Returns list of tags sorted in descending order.

.. _slice_dtl_function:

``slice``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   START(integer-expression{1})
       |   END(integer-expression{0|1}}
       |   STRIDE(integer-expression{0|1}}
       |   VALUES(value-expression{1})
       |
       | Returns a slice of VALUES from START to END with STRIDE. If END is not specified, the slice will
         continue to the end of VALUES. If no STRIDE is specified every element is returned (same as STRIDE=1).

     - | ``["slice", 2, -2, 2, ["list", 0, 1, 2, 3, 4, 5, 6]]``
       | Returns ``[2, 4]``
       |
       | ``["slice", 2, ["list", 0, 1, 2, 3, 4, 5, 6]]``
       | Returns ``[2, 3, 4, 5, 6]``

.. _sorted_dtl_function:

``sorted``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns VALUES sorted in ascending order. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that. If VALUES is not
         a list, then VALUES is returned.

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["sorted", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[2, 3, 4, 4, 5]``.
       |
       | ``["sorted", ["list", "b", 2, {"x": 1}, "a", 4]]``
       |
       | Returns ``[2, 4, "a", "b", {"x": 1}]``.
       | Note that the values are sorted using :ref:`mixed type ordering <mixed_type_ordering>`.
       |
       | ``["sorted",``
       |   ``["list", {"x": 1}, {"x": "abc"}, {"x": 2}]]``
       |
       | Returns ``[{"x": 1}, {"x": 2}, {"x": "abc"}]``
       |
       | ``["sorted", "_.age",``
       |   ``["list",``
       |     ``{"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 20}, {"age": 30}, {"age": 50}]``.
       |
       | ``["sorted", "_S.tags"]]``
       |
       | Returns the tags in ascending order.

.. _sorted_descending_dtl_function:

``sorted-descending``
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   VALUES(value-expression{1})
       |
       | Returns VALUES sorted in descending order. If FUNCTION is given, then
         function is evaluated for each value in VALUES, and the return
         value is used as the sort key. Note that even though FUNCTION is
         given it is the value in VALUES that is returned. Note that this function
         does *not* remove duplicates. Use ``distinct`` to do that. If VALUES is not
         a list, then VALUES is returned.

       .. NOTE::

          Values of different types are ordered using
          :ref:`mixed type ordering <mixed_type_ordering>`.
     - | ``["sorted-descending", ["list", 4, 2, 5, 4, 3]]``
       |
       | Returns ``[5, 4, 4, 3, 2]``.
       |
       | ``["sorted-descending", ["list", "b", 2, {"x": 1}, "a", 4]]``
       |
       | Returns ``[{"x": 1}, "b", "a", 4, 2]``.
       | Note that the values are sorted using :ref:`mixed type ordering <mixed_type_ordering>`.
       |
       | ``["sorted-descending",``
       |   ``["list", {"x": 1}, {"x": "abc"}, {"x": 2}]]``
       |
       | Returns ``[{"x": "abc"}, {"x": 2}, {"x": 1}]``
       |
       | ``["sorted-descending", "_.age",``
       |   ``["list",``
       |     ``{"age": 30}, {"age": 50}, {"age": 20}]]``
       |
       | Returns ``[{"age": 50}, {"age": 30}, {"age": 20}]``.
       |
       | ``["sorted-descending", "_S.tags"]]``
       |
       | Returns the tags in descending order.

.. _sum_dtl_function:

``sum``
-------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Returns the sum of the numeric values in VALUES. Any non-numeric
         values are ignored.
     - | ``["sum", ["list", 2, 4, 6]]``
       |
       | Returns ``12``.
       |
       | ``["sum", "_S.amounts"]]``
       |
       | Returns the sum of the amounts.
