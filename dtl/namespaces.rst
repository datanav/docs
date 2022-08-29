.. _namespace_aware_functions:

Namespace aware functions
=========================

The following functions are namespace aware: :ref:`add <dtl_transform-add>`, :ref:`default <dtl_transform-default>`,
:ref:`make-ni <dtl_transform-make-ni>`, :ref:`remove
<dtl_transform-remove>`, :ref:`copy <dtl_transform-copy>`,
:ref:`rename <dtl_transform-rename>` and :ref:`path
<path_dtl_function>`. This means they behave slightly differently when
:ref:`namespaced identifiers <namespaces>` is enabled.

- Function arguments that are of type ``wildcard-string`` will make
  pattern matching aware of the boundary between the namespace and the
  identifier parts of namespaced identifiers.

- Function arguments that reference unqualified properties,
  i.e. properties with only the identifier part, will in general match
  that property in all namespaces.

See the individual functions for more details.

.. _ni_escape_syntax:

NI escape syntax
----------------

``"foo:bar"`` is an example of a fully qualified namespaced
identifier. ``"bar"`` is an unqualified one and consists of only the
identifier part.

There exists two special escape prefixes, ``":"`` and ``"::"``.

- If you want to make sure that the value is to be interpreted as-is
  then use the ``"::"`` prefix, e.g. ``"::bar"``. ``"::foo:bar"`` is
  equivalent to ``"foo:bar"``.

- If you want the value to be relative to the current namespace,
  i.e. identity or property namespace depending on the context, then use
  the ``":"`` prefix, e.g. ``":bar"``. If the current property namespace
  is ``"foo"`` then ``":bar"`` is equivalent to ``"foo:bar"``.
