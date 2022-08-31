Namespaced identifiers
======================

.. _ni_dtl_function:

``ni``
------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   NAMESPACE(string{0|1}),
       |   VALUES(value-expression{1})
       |
       | Translates input values to namespaced identifiers. Strings and URIs in VALUES
         will be cast to namespaced identifiers. Note that no escaping is done on
         the strings.
       |
       | If NAMESPACE is omitted, then the global namespace is used.
       |
       | URIs can be passed as values in VALUES only when NAMESPACE is not specified.
         The URIs will be collapsed, i.e. the prefix part of URIs will be collapsed into
         a namespace. If the prefix has been declared as a :ref:`namespace <namespaces-feature>`
         then that namespace will be used, otherwise a generated namespace will be added.
     - | Constructs a new namespaced identifier.
       |
       | ``["ni", "foo", "bar"]``
       |
       | This will produce a namespaced identifier ``"~:foo:bar"``.
       |
       | ``["ni", "bar"]``
       |
       | This will produce a namespaced identifier in the global namespace ``"~:bar"``.
       |
       | ``["ni", "foo", ["list", "bar", "x:y"]]``
       |
       | This will produce a list of two namespaced identifiers: ``["~:foo:bar", "~:foo:x:y"]``.
       |
       | ``["ni", "foo", ["uri, "http://example.org/"]]``
       |
       | Returns ``null`` because URIs are not supported when NAMESPACE is specified.
       |
       | ``["ni", ["uri, "http://example.org/bar"]]``
       |
       | Returns ``"~:_:bar"``, i.e. a NI with the ``_`` namespace and ``bar`` as identifier.
         Note that the ``http://example.org/`` URI prefix is mapped to the  ``_`` namespace
         by default.
       |
       | ``["ni", ["uri, "http://unknown.org/something/baz"]]``
       |
       | If the ``"http://unknown.org/something/"`` URI prefix has not been declared as a
         namespace then it will return ``"~:your-pipe-1:baz"`` if the current pipe id is
         ``your-pipe``. The ``-1`` part is a sequence counter, so if you introduce other
         namespaces in your pipe they'll be assigned unique namespace ids. If the URI prefix
         had already been mapped to the ``unknown`` namespace then the expression would have
         returned ``"~:unknown:baz"``.

.. _is_ni_dtl_function:

``is-ni``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
       | Boolean function that returns true if value is a namespaced
         identifier literal, or if it is a list, that the first element
         in the list is a namespaced identifier.
     - | ``["is-ni", ["ni", "foo:bar"]]``
       |
       | Returns ``true``.
       |
       | ``["is-ni", "foo:bar"]``
       |
       | Returns ``false``.
       |
       | ``["is-ni", ["list", ["ni", "foo:bar"], 12345]]``
       |
       | Returns ``true``.
       |
       | ``["is-ni", ["list", 1, ["ni", "foo:bar"]]]``
       |
       | Returns ``false``.

.. _ni_ns_dtl_function:

``ni-ns``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Extracts the namespace part of namespaced identifiers. VALUES that
         are not namespaced identifiers are ignored.
       |
       | ``["ni-ns", "~:foo:bar"]``
       |
       | Returns ``"foo"``.
       |
       | ``["ni-ns", ["list", "~:foo:bar", "~:bar:baz"]]``
       |
       | Returns ``["foo", "bar"]``.

.. _ni_id_dtl_function:

``ni-id``
---------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Extracts the namespace id part of namespaced identifiers. VALUES that
         are not namespaced identifiers are ignored.
       |
       | ``["ni-id", "~:foo:bar"]``
       |
       | Returns ``"bar"``.
       |
       | ``["ni-id", ["list", "~:foo:bar", "~:bar:baz"]]``
       |
       | Returns ``["bar", "baz"]``.

.. _ni_collapse_dtl_function:

``ni-collapse``
---------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Uses the ``namespaces.default`` service metadata contents to produce a namespaced identifier from URLs.
         VALUES that are not URLs are ignored (i.e. it accepts strings and URI parameters). If there is no longest
         matching prefix in the ``namespaces.default`` settings, the functions will return a NI that contains the
         original input (i.e. the The ``http`` and ``https`` prefixes are implicitly defined). Non-http URIs are not
         supported.
         NOTE: this function is experimental and is meant to work with the ``global_defaults.symmetric_namespace_collapse``
         service metadata option set to ``true``.

       |
       | Given this ``namespaces.default`` mapping in the service metadata:
       |
       |  ``{``
            ``"foo": "http://psi.test.no/",``
            ``"sesam_male": "http://sesam.io/people/male/",``
            ``"sesam_female": "http://sesam.io/people/female/",``
            ``"sesam": "http://sesam.io/people/"``
          ``}``
       |
       | The following examples will produce this output:
       |
       | ``["ni-collapse", "http://psi.test.no/bar"]``
       |
       | Returns ``"~:foo:bar"``.
       |
       | ``["ni-collapse", ["list", "http://psi.test.no/bar", "http://psi.test.no/baz"]]``
       |
       | Returns ``["~:foo:bar", "~:foo:baz"]``.
       |
       | ``["ni-collapse", "http://sesam.io/people/employees"]``
       |
       | Returns ``"~:sesam:employees"``.
       |
       | ``["ni-collapse", "http://sesam.io/people/male/john"]``
       |
       | Returns ``"~:sesam_male:john"``.
       |
       | ``["ni-collapse", "http://sesam.io/people/female/jane"]``
       |
       | Returns ``"~:sesam_female:jane"``.
       |
       | The ``http`` and ``https`` namespaces are implicitly defined, so a URI that doesn't match any prefix will work:
       |
       | ``["ni-collapse", "http://example.com/path"]``
       |
       | Returns ``"~:http://example.com/path"``.

.. _ni_expand_dtl_function:

``ni-expand``
-------------

.. list-table::
   :header-rows: 1
   :widths: 40, 60

   * - Description
     - Examples

   * - | *Arguments:*
       |   VALUES(value-expression{1})
       |
     - | Uses the ``namespaces.default`` service metadata contents to produce a URL string from a namespaced identifier.
         VALUES that are not NIs are ignored. If there is no longest matching prefix in the ``namespaces.default``
         settings, the functions will return a string cast of the NI.
         NOTE: this function is experimental and is meant to work with the ``global_defaults.symmetric_namespace_collapse``
         service metadata option set to ``true``.

       |
       | Given this ``namespaces.default`` mapping in the service metadata:
       |
       |  ``{``
            ``"foo": "http://psi.test.no/",``
            ``"sesam_male": "http://sesam.io/people/male/",``
            ``"sesam_female": "http://sesam.io/people/female/",``
            ``"sesam": "http://sesam.io/people/"``
          ``}``
       |
       | The following examples will produce this output:
       |
       | ``["ni-expand", "~:foo:bar"]``
       |
       | Returns ``http://psi.test.no/bar``.
       |
       | ``["ni-expand", ["list", "~:foo:bar", "~:foo:baz"]]``
       |
       | Returns ``["http://psi.test.no/bar", "http://psi.test.no/baz"]``.
       |
       | ``["ni-expand", "~:sesam:employees"]``
       |
       | Returns ``"http://sesam.io/people/employees"``.
       |
       | ``["ni-expand", "~:sesam_male:john"]``
       |
       | Returns ``"http://sesam.io/people/male/john"``.
       |
       | ``["ni-expand", "~:sesam_female:jane"]``
       |
       | Returns ``"http://sesam.io/people/female/jane"``.
       |
       | ``["ni-expand", "~:http://example.com/path"]``
       |
       | Returns ``"http://example.com/path"``.
       |
       | ``["ni-expand", "~:unknown:path"]``
       |
       | Returns ``"unknown:path"``.
