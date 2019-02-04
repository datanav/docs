.. _deprecations:

============
Deprecations
============

.. contents:: Table of Contents
   :depth: 2
   :local:

This document contains deprecated sections from the documentation. Do
not make use of these features.

Transformations
===============

.. _properties_to_curies:

The properties to CURIEs transform
----------------------------------

This transform can transform entity properties to `RDF CURIEs <https://www.w3.org/TR/curie/>`__ (a superset of `XML QNames <https://en.wikipedia.org/wiki/QName>`_)
based on wildcard patterns. It is used primarily when dealing with or preparing to output
`RDF <https://www.w3.org/standards/techs/rdf#w3c_all>`__ data. Note that URL quoting is applied to the property names
as part of the transform. Also note that by default the path separator character ("/) is not quoted, but the behaviour
is configurable.

Prototype
^^^^^^^^^

::

    {
        "type": "properties_to_curies",
        "rule": "rdf-registry-entry",
        "quote_safe_characters": "/",
        "id": "optional-id-prefix",
        "properties": [
          "optional_some_prefix", ["optional_some_pattern"]
        ]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rule``
     - String
     - The id of the key in the :ref:`RDF registry <rdf_registry>` containing the prefix rules to to use for the transformation.
       See :doc:`RDF support <rdf-support>` for more information about the RDF registry and how to configure it.
     -
     - Yes*

   * - ``quote_safe_characters``
     - String
     - A string of characters that should be treated as "safe" from URL quoting by the transform. By default this is
       the slash character ("/").  If this property is set to the empty string (""), all characters of the property name
       will be URL quoted. This property can also be set at the RDF registry level, but this value will be overridden
       if set directly on the transform configuration.
     -
     -

   * - ``id``
     - String
     - The prefix to use for ``_id`` properties
     -
     - Yes*


   * - ``properties``
     - List<(String, List<String>)>
     - A list of String,List pairs that make up the rules for which properties should be assigned which prefixes.
       See the example section below for a fuller explanation of this property.
     -
     - Yes*

Note that ``rule`` and ``id`` and ``properties`` are mutually exclusive. If all three are present,
``rule`` is given precedence and ``id`` and ``properties`` are ignored.

Example
^^^^^^^


The ``rule`` property references a :ref:`RDF registry entry <rdf_registry>` containing a ``prefix_rules`` object.
See :doc:`RDF support <rdf-support>` for more information about the RDF registry and how to configure it.
Alternatively, the contents of the ``prefix_rules`` entry (i.e. .the ``id`` and ``properties``) can be included inline
in the transform configuration.

Given a pre-existing RDF registry entry ``my_entry``:

::

    "my_entry": {
       ..
       "prefix_rules": {
           "id": "x",
           "properties": [
                "c", ["status", "code"],
                "_", ["status"],
                "t", ["t_*"],
                "m", ["status", "**", "m*"],
                "s", ["status", "**"],
                "x", ["**"]
           ]
       }
       ..
    }

And a transform configuration:

::

    {
        "type": "properties_to_curies",
        "rule": "my_entry"
    }

And the input entity:

::

    {
        "_id": "foo/bar",
        "name": "John",
        "born": "1980-01-23",
        "code": "AB32",
        "t_a": "A",
        "a/b": "A/B",
        "status": {
            "married": true,
            "spouse": "Pam",
            "code": 123,
            "t_b": {
                "t_c": "C",
                "hello": "world",
                "<s:hi>": "bye"
            }
        }
    }

The transform will output the following transformed entity:

::

    {
        "_id": "<x:foo/bar>",
        "<x:name>": "John",
        "<x:born>": "1980-01-23",
        "<x:code>": "AB32",
        "<t:t_a>": "A",
        "<x:a/b>": "A",
        "<_:status>": {
            "<m:married>": true,
            "<s:spouse>": "Pam",
            "<c:code>": 123,
            "<t:t_b>": {
                "<t:t_c>": "C",
                "<s:hello>": "world",
                "<s:hi>": "bye"
            }
        }
    }

Setting ``quote_safe_characters`` to "" would instead yield:

::

    {
        "_id": "<x:foo%2Fbar>",
        "<x:name>": "John",
        "<x:born>": "1980-01-23",
        "<x:code>": "AB32",
        "<t:t_a>": "A",
        "<x:a%2Fb>": "A",
        "<_:status>": {
            "<m:married>": true,
            "<s:spouse>": "Pam",
            "<c:code>": 123,
            "<t:t_b>": {
                "<t:t_c>": "C",
                "<s:hello>": "world",
                "<s:hi>": "bye"
            }
        }
    }

Notice that now "/" has also been URL quoted ("%2F")

.. _uris_to_curies_transform:

The URIs to CURIEs transform
----------------------------

This transform can transform entity properties containing URIs in the keys and/or the values to a more compact form
using `RDF CURIEs <https://www.w3.org/TR/curie/>`_ (a superset of `XML QNames <https://en.wikipedia.org/wiki/QName>`_).
It is used primarily when dealing with or reading RDF data. See the :doc:`rdf-support` document for more information
about working with `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ data in Sesam.

Prototype
^^^^^^^^^

::

    {
        "type": "uris_to_curies",
        "prefix_includes": ["entry1", "entry2"]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``prefix_includes``
     - List<String>
     - A list of string keys to look up in the instance-wide :ref:`RDF registry <rdf_registry>`. These keys reference
       objects which contain RDF support structures such as CURIE prefixes (and possibly references to other prefix
       sets to include).
       The prefixes collected from the RDF registry will be used to compress full URIs to CURIEs.
       See :doc:`RDF support <rdf-support>` for more information about the RDF registry and how to configure it.
       The :ref:`common RDF prefixes <built_in_prefixes>` are built-in and you don't have to provide the mapping for it
       (i.e. RDF, RDFS, OWL etc).
     -
     -

Example
^^^^^^^

Given the configuration:

::

    {
        "transform": [
           {
             "type": "uris_to_curies",
             "prefix_includes": ["my_entry"]
           }
        ]
    }

The RDF registry entry:

::

    "my_entry": {
       "prefixes": {
          "foo": "http://psi.foo.com/"
          "test": "http://psi.test.com/"
       }
       ..
    }

And the input entity:

::

    {
        "_id": "http://psi.test.com/2",
        "http://psi.test.com/name": "John",
        "born": "1980-01-23",
        "http://psi.test.com/code": "AB32",
        "status": {
            "http://psi.foo.com/married": true,
            "spouse": "Pam",
            "url1": "~rhttp://www.foo.com",
            "url2": "~rhttp://psi.foo.com/url2",
            "code": 123,
            "child": {
                "t_c": "C",
                "http://psi.test.com/hello": "http://psi.foo.com/world",
                "http://psi.tests.com/s": "bye"
            }
        }
    }

The transform will output the following compact/"compressed" transformed entity:

::

    {
        "_id": "<test:2>",
        "<test:name>": "John",
        "born": "1980-01-23",
        "<test:code>": "AB32",
        "status": {
            "<foo:married>": true,
            "spouse": "Pam",
            "code": 123,
            "url1": "~rhttp://www.foo.com",
            "url2": "~rfoo:url2",
            "child": {
                "t_c": "C",
                "<test:hello>": "<foo:world>",
                "http://psi.tests.com/s": "bye"
            }
        }
    }


Note that the transform will not attempt to unquote the remainder elements after the matched prefixes.


DTL Functions
=============

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Function
     - Description
     - Examples

       .. _curie_function:
   * - ``curie``
     - | *Arguments:*
       |   PREFIX(string{1}),
       |   VALUES(value-expression{1})
       |
     - | Constructs new CURIEs as URI objects based on a the PREFIX
         and VALUES arguments.
       |
       | ``["curie", "foo", "bar"]``
       |
       | This will produce a URI object with the value ``"~rfoo:bar"``.
       |
       | ``["curie", "foo", ["list", "bar", "zoo"]]``
       |
       | This will produce a list of two URI objects with the
         values ``["~rfoo:bar", "~rfoo:zoo"]``.

       .. _uri_expand_function:
   * - ``uri-expand``
     - | *Arguments:*
       |   FUNCTION(function-expression(0|1}
       |   ENTITIES(value-expression{1})
       |
     - | Runs the given entities through the prefixing rules and the
         prefix expansion mapping defined in the node metadata RDF registry.
         The given entities must have a ``_dataset`` property containing the
         id of the dataset to which they belong *or* the key to look up the
         prefixes must be computed by the (optional) FUNCTION argument. The
         result of the FUNCTION argument will override any ``_dataset``
         property on the entity. The id given or computed will be used to locate
         the prefix rules and prefix expansion mapping within the node RDF registry.
         Note that the result of FUNCTION must be a single string value.

       | The main purpose of this function is to prepare entities for
         translation into RDF form. See the :doc:`RDF support <rdf-support>`
         document for more information about how this works.

       | Example node metadata:

         ::

            {
                "rdf": {
                  "people": {
                     "prefixes": {
                       "p": "http://example.org/people/"
                     },
                     "prefix_rules": {
                       "id": "p",
                       "properties": [
                          "p", ["name"],
                          "c", ["Employer"],
                          "_", ["**"]
                       ]
                     }
                  }
                }
            }

       | Example input entity:

         ::

            {
              "_id": "john_doe",
              "_dataset": "people",
              "name": "John Doe",
              "employer": "Example Ltd.",
              "born": "1973-01-21"
            }

       | Given the above configuration you should expect the following URI-expanded
         entity in the result:

         ::

            {
              "_id": "<http://example.org/people/john_doe>",
              "_dataset": "people",
              "<http://example.org/people/name>": "John Doe",
              "<http://example.org/company/employer>": "Example Ltd.",
              "<http://example.org/born>": "1973-01-21"
            }

       | ``["uri-expand",``
       |   ``{"_id": "mary", "_dataset": "people", "name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity.
       |
       | ``["uri-expand",``
       |   ``["lookup", ["list", "~rsesam:A/foo"], "bar"]]``
       |
       | Looks up the ``foo`` entity in the ``A`` dataset and ``bar`` in the current
         dataset, then URI expands them.
       | ``["uri-expand",``
       |   ``["list", {"_id": "mary", "name": "Mary Jones"}]]``
       |
       | Returns an empty list because the ``mary`` entity is missing the ``_dataset``
         property.
       | ``["uri-expand", ["string", "people"],``
       |    ``{"_id": "mary", "_dataset": "employees",``
       |      ``"name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity using the prefixes
         registered by the "people" key in the node RDF registry (i.e. the
         ``_dataset`` value of "employees" is overriden by the computed value)

       | ``["uri-expand", ["string", "_.type"],``
       |   ``{"_id": "mary", "_dataset": "employees",``
       |     ``"type": "person", "name": "Mary Jones"}]``
       |
       | Returns an URI expanded version of the ``mary`` entity using the prefixes
         registered by the "person" key in the node RDF registry. The ``_dataset``
         value of "employees" is overriden by the computed value (based on
         the contents of the entity's ``type`` property in this example).

Sinks
=====


Deprecated Properties
---------------------

The ``prefix_includes`` property has been deprecated for the :ref:`sparql <sparql_sink>`, :ref:`sdshare <sdshare_push_sink>`, :ref:`databrowser <databrowser_sink>`, and :ref:`http_endpoint <http_endpoint_sink>` sinks.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``prefix_includes``
     - List<String>
     - A list of string keys to look up in the node-wide :ref:`RDF registry <rdf_registry>`. These keys reference objects which contain
       RDF support structures such as CURIE prefixes (and possibly references to other prefix sets to include).
       The prefixes collected from the RDF registry will be used to expand CURIEs into full URIs.
       See :doc:`RDF support <rdf-support>` for more information about the RDF registry and how to configure it.
       You do not need include any prefix sets to use the :ref:`common RDF prefixes <built_in_prefixes>` (i.e. RDF,
       RDFS, OWL and so on).
     -
     -


.. _rdf_registry:

The RDF registry
================

When working with RDF data in Sesam, we would like to be able to define, maintain and share these RDF prefixes
among our datasets and DTL transforms. For this purpose Sesam has a built-in *RDF registry*.
You can configure the registry by including an entity in your configuration on the form:

::

    {
       "_id": "node"
       "type": "metadata",
       "rdf": {
          "dataset1": {
              "prefixes": {
                  "foo": "http://example.com/foo/",
                  "foo_schema": "http://example.com/foo/schema/"
              },
              "prefix_rules": {
                  "id": "foo",
                  "properties": [
                      "foo_schema", ["**"]
                  ]
              }
          },
          "dataset2": {
              "prefixes": {
                  "bar": "http://example.com/bar/",
                  "bar_schema": "http://example.com/bar/schema/"
              },
              "prefix_includes": ["dataset1"],
              "quote_safe_characters": "",
              "prefix_rules": {
                  "id": "bar",
                  "properties": [
                      "foo_schema", ["some_prop"],
                      "bar_schema", ["**"]
                  ]
              }
          }
    }

The root key ``rdf`` above contains the entire configuration of the RDF registry. Its sub-keys will usually correspond
to dataset ids, although you can register any valid key here.

RDF registry items
------------------

The "prototype" of a RDF registry entry ``entry_id`` look like:

::

    ..
    "entry_id": {
        "prefixes": {
           "foo" : "http://example.com/foo/",
           "baz" : "http://example.com/baz/",
           "bar" : "http://example.com/baz/"
        },
        "prefix_includes": ["list_of", "other", "registry", "entries"],
        "prefix_rules": {
            "id": "bar",
            "properties": [
                "foo", ["some_prop"],
                "baz", ["**"]
            ]
        },
        "quote_safe_characters": "/æåø",
    }

Note that the ``quote_safe_characters`` is an optional property of the RDF registry entity. If specified, it should
contains a string of characters that should be excluded from URL quoting when constructing CURIEs. It can also be
specified on the :ref:`properties to CURIEs transform <properties_to_curies>` where, if specified, will take precedence
over any value it might have in the RDF registry entry. This property defaults to "/" and would normally not need
to be changed. A value of "" (the emtpy string) means "quote all characters". See below for more detail on the use of
this transform.

Prefixes
^^^^^^^^

Each registry item must contain at least a single property ``prefixes`` which is a object containing prefix
to URI mappings for CURIE generation or expansion. The registry items can also contain a list property ``prefix_includes``
which must be references to other existing RDF registry keys. When looking up items in the RDF registry, any prefix elements
in this list will be recursively included. Take care that you don't have overlapping prefix names, as the final result
will be undefined. Also make sure you don't create circular references using this property.


.. _built_in_prefixes:

Built-in prefixes
^^^^^^^^^^^^^^^^^

The Sesam RDF registry has built-in support for the common prefixes in RDF, such as ``rdf``, ``rdfs`` and ``owl``.
This means you don't have to define these yourself to use them in your CURIEs. The full list of built-in prefixes is:

::

   {
       "_": "http://example.org/",
       "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
       "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
       "owl": "http://www.w3.org/2002/07/owl#",
       "xsd": "http://www.w3.org/2001/XMLSchema#",
       "skos": "http://www.w3.org/2004/02/skos/core#",
       "foaf": "http://xmlns.com/foaf/0.1/",
       "wgs84": "http://www.w3.org/2003/01/geo/wgs84_pos#",
       "dc": "http://purl.org/dc/elements/1.1/",
       "dcterms": "http://purl.org/dc/terms/",
       "gs": "http://www.opengis.net/ont/geosparql#"
   }

The "_" prefix is used in general as a fallback if no prefix is defined for a property when mapping an entity
to its RDF representation.

Prefix rules
^^^^^^^^^^^^

The final property that can exist in a RDF registry item is ``prefix_rules``. This element tells us how to create RDF
CURIEs from a plain entity: the ``id`` property contains the prefix to use for the ``_id`` property of the entity
(i.e. the subject in RDF) and the ``properties`` property is a list of property pairs that encode the rules for what
prefix to apply to which property of the entity.

The ``properties`` format is tuples of string/list pairs, where the first item is the prefix to add and the second is
the path expression that is used to match against. The number of elements in the list must be even. Path expressions
are evaluated in order and the first matching path expression will win, so if a path expression matches the prefix will
be assigned to the matching key.

A path expression is a list of strings. The left-most string value is the most specific. ``**`` can be used to denote
nestedness at an arbitrary depth. ``*`` can be used as a wildcard in the string values themselves.


.. _the_properties_to_curie_transform_local:

The property to CURIE transform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A complete example of how the ``prefix_rules`` property works; we want to transform an entity that looks like:

::

    {
        "_id": "2",
        "name": "John",
        "born": "1980-01-23",
        "code": "AB32",
        "t_a": "A",
        "status": {
            "married": True,
            "spouse": "Pam",
            "code": 123,
            "t_b": {
                "t_c": "C",
                "hello": "world",
                "<s:hi>": "bye"
            }
        }
    }

to RDF form using CURIEs. We start by defining the rules for this transformation in the RDF registry entry ``my_entry``:

::

    "my_entry": {
       ..
       "prefix_rules": {
           "id": "x",
           "properties": [
                "c", ["status", "code"],
                "_", ["status"],
                "t", ["t_*"],
                "m", ["status", "**", "m*"],
                "s", ["status", "**"],
                "x", ["**"]
           ]
       }
       ..
    }


We then add a :ref:`properties to CURIEs transform <properties_to_curies>` to the start of our pipe's
``transform`` section:

::

    ..
        "transform": [
            {
                "type": "properties_to_curies",
                "rule": "my_entry"
            }
            ..
        ]

This transform will use our ``my_entry`` rules and produce the following transformed entity:

::

    {
        "_id": "<x:2>",
        "<x:name>": "John",
        "<x:born>": "1980-01-23",
        "<x:code>": "AB32",
        "<t:t_a>": "A",
        "<_:status>": {
            "<m:married>": True,
            "<s:spouse>": "Pam",
            "<c:code>": 123,
            "<t:t_b>": {
                "<t:t_c>": "C",
                "<s:hello>": "world",
                "<s:hi>": "bye"
            }
        }
    }

RDF input
=========

Sesam supports RDF input from several different sources:

* :ref:`The RDF source <rdf_source>`
* :ref:`The SDShare source <sdshare_source>`
* :ref:`The SPARQL source <sparql_source>`

Additionally, you can set up a :ref:`HTTP endpoint source <http_endpoint_source>` which includes a `SDShare Push` capable
HTTP endpoint where you can post RDF data in NTriples format in accordance with the ``SDShare Push protocol``.

The URIs to CURIEs transform
----------------------------

All of these methods of RDF input will provide entities to your data flows on the general form:

::

   {
       "_id": "<http://example.com/bar>",
       "<http://example.com/schema/some_predicate>": "Some literal",
       "<http://example.com/schema/other_predicate>": "~rhttp://example.com/zoo"
   }

When processing this data in the flow, we would like to first transform these entities to CURIE form using the
RDF registry to manage the prefixes. In the above example we can add a :ref:`URIs to CURIEs transform <uris_to_curies_transform>`
to the pipe to achieve this:

::

    {
        "_id": "my-pipe",
        ..
        "transform": [
           {
             "type": "uris_to_curies",
             "prefix_includes": ["my_entry"]
           }
        ]

where the corresponding ``my_entry`` in the RDF registry looks like:

::

    ..
    "my_entry": {
        "prefixes": {
            "foo": "http://example.com/",
            "foo_schema": "http://example.com/schema/"
        }
        ..
    }
    ..

This transform will then produce the following entity:

::

    {
       "_id": "<foo:bar>",
       "<foo_schema:some_predicate>": "Some literal",
       "<foo_schema:other_predicate>": "~rfoo:zoo"
    }

RDF in transforms
=================

The Sesam DTL language features several functions that are useful when working with RDF data in your flow.

Accessing CURIEs properties
---------------------------

When addressing properties in CURIEs form in DTL transform, you can simply use their names verbatim. For example:

::

    ..
    ["rename", "<foo:third_predicate>", "<foo:some_predicate>"],
    ["copy", "_S.<foo_schema:other_predicate>"],
    ["add", "<rdfs:label>", "Bob"]
    ..

You can also use the CURIEs in path expressions in the same way as any other property name. If you want to add a URI
literal as part of your transformed entity you can use the DTL :ref:`curie function <curie_function>`, which takes
a prefix and a value expression (i.e. a literal or a function) and produces a URI property value:

::

    ..
    ["add", "<foo_schema:baz>", ["curie", "foo", "zoo"]]
    ..

This will add a property that looks like:

::

   {
     ..
     "<foo_schema:baz>": "~rfoo:zoo"
     ..
   }

CURIE expansion in DTL
----------------------

When processing RDF data in a flow, we sometimes would like to expand an entity or a child entity from CURIEs to full
URI form (for example if there are conflicting usages of prefixes). This can be done using the DTL
:ref:`uri-expand <uri_expand_function>`:

::

    ..
    ["add", "<baz:expanded>", ["uri-expand", ["string", "my_entry"], {"_id": "<foo:bob>", "<foo:name>": "Bob Jones"}]]
    ..

This will expand the properties of the entity (here shown inline, but typically will be from a :ref:`hops <hops_function>` join or some
other function) to its "full" form:

::

    {
      ..
      "<baz:expanded>": {
          "_id": "<http://example.com/foo/bob>",
          "<http://example.com/foo/name>": "Bob Jones"
      }
      ..
    }

Note that expanding CURIEs is normally done at the endpoint of your flow (i.e. by the sink or a SDShare feed, see below).
However, if the sink you are using to output the final data is not RDF aware (i.e. supports automatic prefix expansion)
you can use the ``uri-expand`` function to achieve the same functionality.
