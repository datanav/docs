Dictionaries
============

.. _dict_dtl_function:

``dict``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   EMPTY{0} or ITEMS(value-expression{1}) or (KEY, VALUE){>=0)
       |
       | If EMPTY, i.e. no arguments given, then an empty dict (``{}``) is returned.
       |
       | If ITEMS specified, then it takes a list of key+value pair tuples and
         returns a dictionary with those tuples as keys and values. Note that
         last key  wins. Values that are not two-element tuples are ignored.
       |
       | If KEY+VALUE pairs are given, then a new dict with those pairs as keys and
         values. Note that last key  wins.
     - | ``["dict"]``
       |
       | Returns ``{}``.
       |
       | ``["dict",``
       |     ``["list",``
       |         ``["list", "A", 1],``
       |         ``["list", "B", 2],``
       |         ``["list", "C", 3]]]``
       |
       | Returns ``{"A": 1, "B": 2, "C": 3}``.
       |
       | ``["dict", ["list", "X", 123, ["list", "A", 1]]``
       |
       | Returns ``{"A": 1}``.
       |
       | ``["dict",``
       |   ``"a", ["upper", "a"],``
       |   ``["lower", "B"], "B"]``
       |
       | Returns ``{"a": "A", "b": "B"}``.

.. _is_dict_dtl_function:

``is-dict``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a dictionary or if it is a list, that the first element
       | in the list is a dictionary
       |
     - | ``["is-dict", "_S."]``
       |
       | Returns true.
       |
       | ``["is-dict", ["list", {"a": 1}, 123]``
       |
       | Returns true.
       |
       | ``["is-dict", ["list", 123, {"a": 1}]``
       |
       | Returns false.
       |
       | ``["is-dict", "abc"]``
       |
       | Returns false

.. _items_dtl_function:

``items``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of key+value tuples.
         For each key+value pair in the dictionaries one pair is added to the output
         list. Non-dictionary values are ignored. Note that entities are dictionaries,
         so you can use this function with them.
     - | ``["items",``
       |     ``["list", {"A": 1, "B": 2}, {"C": 3}]]``
       |
       | Returns ``[["A", 1], ["B", 2], ["C", 3]]``.
       |
       | ``["items", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``[["A", 1]]``.

.. _key_values_dtl_function:

``key-values``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of dictionaries with "key"
         and "value" keys. For each key+value pair in the dictionaries one dict is added
         to the output list. Non-dictionary values are ignored. Note that entities are
         dictionaries, so you can use this function with them.
     - | ``["key-values",``
       |     ``["list", {"A": 1, "B": 2}, 123, {"C": 3, "A": 1}]]``
       |
       | Returns ``[{"key": "A", "value": 1},``
       |            ``{"key": "B", "value": 2},``
       |            ``{"key": "C", "value": 3},``
       |            ``{"key": "A", "value": 1}]``.
       |
       | ``["key-values", {"hello": "world"}]``
       |
       | Returns ``{"key": "hello", "value": "world"}``.

.. _keys_dtl_function:

``keys``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of keys.
         For each key+value pair in the dictionaries one key is added to the output
         list. Non-dict values are ignored.
     - | ``["keys",``
       |     ``["list", {"A": 1, "B": 2}, {"A": 1, "C": 3}]]``
       |
       | Returns ``["A", "B", "A", "C"]``.
       |
       | ``["keys", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``["A"]``.

.. _values_dtl_function:

``values``
----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   DICTS(value-expression{1})
       |
       | Takes a list of dictionaries in and outputs a list of values.
         For each key+value pair in the dictionaries one value is added to the output
         list. Non-dict values are ignored.
     - | ``["values",``
       |     ``["list", {"A": 1, "B": 2}, {"A": 1, "C": 3}]]``
       |
       | Returns ``[1, 2, 1, 3]``.
       |
       | ``["values", ["list", "X", 123, {"A": 1}]]``
       |
       | Returns ``[1]``.
