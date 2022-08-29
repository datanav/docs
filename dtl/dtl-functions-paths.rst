Paths
=====

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

         This transform function is :ref:`namespaced identifiers <namespaces>` aware.

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
