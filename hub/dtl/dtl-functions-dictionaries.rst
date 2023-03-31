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

.. _has_key_dtl_function:

``has-key``
-----------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   KEY(value-expression{1}),
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if the key exists in the dictionary or false if not. Any non-dictionary
         argument will return null. If the VALUES argument is a list, only the first element will be used.
       |
     - | ``["has-key", "a", {"a": 1}]``
       |
       | Returns true.
       |
     - | ``["has-key", "b", {"a": 1}]``
       |
       | Returns false.
       |
       | ``["has-key", "a", ["list", {"a": 1}, 123]``
       |
       | Returns true.
       |
       | ``["has-key", "b", ["list", {"a": 1}, {"b": 1}]``
       |
       | Returns false.
       |
       | ``["has-key", "a", ["list", 123, {"a": 1]``
       |
       | Returns null.

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

.. _apply_ns_dtl_function:

``apply-ns``
------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   NAMESPACE_OR_CONFIGDICT(string|dict)
       |   VALUES(value-expression{1})
       |
       | The apply-ns function can be used to add a namespace to the properties of a dict (recursively by default ), like the :ref:`add_namespaces <namespaces_feature_add_namespaces>` pipe feature does.
         The NAMESPACE_OR_CONFIGDICT is either a static string value or a static dict value.
         The static dict value is technically a set of keyword arguments. The default value is
       |    ``{``
       |        ``"property_namespace": <pipe's property_namespace (defaults to the pipe id)>,``
       |        ``"identity_namespace": <pipe's identity_namespace (defaults to the pipe id)>,``
       |        ``"skip_underscore": true,``
       |        ``"skip_dollar": true,``
       |        ``"recursive": true``
       |    ``}``
       | and reflects the behaviour of the :ref:`add_namespaces=true <namespaces_feature_add_namespaces>` pipe property.
       |
       | By default properties starting with an ``"_"`` (underscore) character is left as-is, except for the ``_id`` property, where the property-value is prefixed with ``<identity_namespace>:``.  The ``skip_underscore`` configdict setting can be set to ``false`` to treat properties starting with ``"_"`` as "normal" properties.
       |
       | By default properties starting with an ``"$"`` (dollar) character is left as-is. The ``skip_dollar`` configdict setting can be set to ``false`` to treat properties starting with ``"$"`` as "normal" properties.

     - | Example: with static string argument (and using defaults):
       | ``["apply-ns", "myns", {"_id": "123", "foo": 1, "$bar": {"baz": 2}}```
       | Returns ``{"_id": "myns:123", "myns:foo": 1, "$bar": {"baz": 2}}``
       |
       | Example: add namespace to everything recursively:
       | ``["apply-ns", {"property_namespace": "myns", "identity_namespace": "myns", "skip_underscore": false, "skip_dollar": false, "recursive": true},``
       |   ``{"_id": "123", "foo": 1, "$bar": {"baz": 2}}``
       | Returns ``{"myns:_id": "myns:123", "myns:foo": 1, "myns:$bar": {"myns:baz": 2}}``
       |
       | Example: setting property_namespace or identity_namespace to null explicitly means that we won't add a namespace:
       | ``["apply-ns", {"property_namespace": "myns", "identity_namespace": null, "skip_underscore": false, "skip_dollar": false, "recursive": false},``
       |              ``{"_id": "123", "myns:foo": 1, "$bar": {"baz": 2}}``
       | Returns ``{"myns:_id": "123", "myns:foo": 1, "myns:$bar": {"baz": 2}}``


.. _path_dtl_function:

``path``
--------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   PROPERTY_PATH(value-expression{1}),
       |   VALUES(value-expression{1})
       |
       | Traverses the PROPERTY_PATH path for each of the entities in
         VALUES. The result is all the values at the end of
         the traversal. This may be a single value or a list of values.
         PROPERTY_PATH is an expression that should resolve
         to a string or a list of strings. Those strings are treated as
         literals, i.e. property names, so no variables can be used. Only
         properties on the entity can be traversed. If you want to traverse
         to other entities use the ``hops`` function instead.

       .. NOTE::

         This transform function is :ref:`namespaced identifiers <namespaces-feature>` aware.

         If namespaced identifiers are enabled and the path element is not
         a fully qualified namespaced identifier then all properties with
         the path element as its identifier part will be part of the result.
         In practice the result is the union of all those properties.

     - | ``["path", "age", ["list", {"age": 23}, {"age": 24}]]``
       |
       | Traverses the ``age`` field of the VALUES entities.
         Returns ``[23, 24]``.
       |
       | ``["path", ["list", "order_lines", "item_name"], "_S.orders"]``
       |
       | This will traverse from the source entity's orders to the
         order lines and then return their item names. The output is a
         list of product item names.
       |
       | ``["path", "age", {"age": 24}]``
       |
       | Returns ``24``.
       |
       | ``["path", "foo", {"bar": 123}]``
       |
       | Returns ``null``.
       |
       | ``["path", ["list", "a", "b"],``
       |   ``["list", {"a": {"b": 1}}, {"a": [{"b": 2}, {"b": 3}]}]]``
       |
       | Returns ``[1, 2, 3]``.
       |
       | **With namespaced identifiers enabled:**
       |
       | ``{``
       |   ``"namespaced_identifiers": true,``
       |   ``"namespaces": {``
       |     ``"identity": "foo",``
       |     ``"property": "bar"``
       |   ``}``
       | ``}``
       |
       | ``["path", "foo:a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``2`` as the path element ``"foo:a"`` is a fully qualified
         namespaced identifier.
       |
       | ``["path", "a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``[1, 2, 3, 4]``, i.e. the union of all the values in all
         the properties that have ``a`` in their identifiers part.
       |
       | ``["path", "::a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``1`` as ``"::a"`` uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to explicity reference the unqualified ``a`` property.
       |
       | ``["path", ":a", {"a": 1, "foo:a": 2, "bar:a": [3, 4]}]``
       |
       | Returns ``[3, 4]`` as ``":a"`` uses the :ref:`NI escape syntax <ni_escape_syntax>`
         to explicity reference the ``"a"`` property in the current namespace ``"bar"``.

.. _apply_dtl_function:

``apply``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   RULE_ID(string{1}),
       |   VALUES(value-expression{1})
       |
       | Applies the RULE_ID transform rule on the values in VALUES.
         RULE_ID must be the id of a transform rule in the current DTL
         specification.
     - | ``["apply", "order", "_S.orders"]``
       |
       | This will transform the order values in the source entity's
         ``orders`` field using the ``order`` transform rules. The output is
         the transformed order values.

.. _apply_hops_dtl_function:

``apply-hops``
--------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   RULE_ID(string{1}),
       |   HOPS_SPEC(dict{>1})
       |
       | This function is a combined ``hops`` and ``apply`` function. It
         evaluates the hops, and then passes the result through
         the RULE_ID transform rule.

       | See the :ref:`apply <apply_dtl_function>`
         and the :ref:`hops <hops_dtl_function>` functions for more information
         about the parts.

       .. NOTE::

          Use this function instead of ``apply`` if you use ``hops`` inside
          the transformation rule. This is required so that
          `dependency tracking <concepts.html#dependency-tracking>`_
          can work. Calling ``apply`` on a rule that contains ``hops`` or
          ``apply-hops`` is not allowed.

     - | ``["apply-hops", "order", {``
       |   ``"datasets": ["orders o"],``
       |   ``"where": ["eq", "_S._id", "o.cust_id"]``
       |  ``}]``
       |
       | This will retrieve orders from the hops expression and then
         transform them using the ``order`` transformation rule. The output
         is the transformed order values.
