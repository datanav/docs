================
Working with RDF
================

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

Sesam has several features to facilitate working with RDF data both as input, when doing transforms and finally
when exposing or producing data for external consumption.

In this document we will cover what you need to know when working with RDF data with Sesam.

Core Concepts
-------------

First, a short recap of the core concepts when working with RDF, see the `RDF standard <https://www.w3.org/standards/techs/rdf#w3c_all>`_ for more details:

The RDF data model consists in essence of statements about a particular subject. This is given as a *triple*:

::

    subject predicate object


While subjects and predicates are always URIs, objects can be either a literal (i.e. a quoted string, representing dates,
numbers, strings etc) or another subject (URI). There are other optional elements to these subjects such as language
and/or datatype identifiers - again refer to the standard for more detail.

You can have multiple statements for a single subject.

A common representation of such RDF triples is `NTriples <https://www.w3.org/TR/2014/REC-n-triples-20140225/>`_,
where each URI is enclosed in brackets and every statement (triple) ends with a punctuation mark. Semicolon can also be
used to end a statement meaning that the subject on the next line will be omitted (i.e. the subjects stays the same/carries over).
An example:

::

   <http://company.com/employees/bob> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://company.com/schema/employee>;
       <http://company.com/schema/first-name> "Bob";
       <http://company.com/schema/employed-by> <http://company.com> .

Here we have three individual statements regarding the subject ``http://company.com/employees/bob``. We're stating
that is has a RDF ``type`` represented by the subject ``http://company.com/schema/employee`` and that this ``employee``
has a literal property "Bob" and is employed by a company represented by the subject ``http://company.com``.

Now, this is fairly straight forward but perhaps a bit verbose in the long run. To alleviate this, we can use the
concept of *prefixes* and `RDF curies <https://www.w3.org/TR/curie/>`_. A *prefix* is the "constant" part of a URL,
i.e. everything up to a certain path-element (usually the last). Using CURIES means giving these common prefixes short hand
 names enabling us to rewrite the full URI to a shorter "prefix:path" form.

Let us define some prefixes for the above example, and give them such short hand names. The example below is in
`RDF Turtle format <https://www.w3.org/TR/turtle/>`_, which is a superset of NTriples. Turtle syntax supports prefixes
and CURIES and is often used when writing RDF manually or intended to be read by humans. In general, it is considered
ood practice to reduce full URIs to CURIES using prefixes whenever possible. When working with RDF in Sesam we try to
follow this rule:

::

    PREFIX employees: <http://company.com/employees/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX emp_schema: <http://company.com/schema/>

Now, rewriting the original URIs with these short form CURIEs we get:

::

   <employees:bob> <rdf:type> <http://company.com/schema/employee> .
   <employees:bob> <emp_schema:first-name> "Bob" .
   <employees:bob> <emp_schema:employed-by> <http://company.com> .

This is both shorter, easier to work with and also makes it easier to *change the prefix* without having to
reprocess or reload any of our data.

.. _rdf_registry:

The RDF registry
================

When working with RDF data in Sesam, we would like to be able to define, maintain and share these RDF prefixes
among our datasets and DTL transforms. To achieve this, Sesam has a built-in *RDF registry* for this purpose.
You configure the registry by including an entity in your configuration on the form:

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
              "prefix_rules": {
                  "id": "bar",
                  "properties": [
                      "foo_schema", ["some_prop"]
                      "bar_schema", ["**"]
                  ]
              }
          }
    }

The key ``rdf`` above contains the configuration of the RDF registry. It contains keys which usually correspond
to dataset id's, although you can register any valid key here.

RDF registry items
------------------

Prototype

::

    ..
    "item_id": {
        "prefixes": {
           "foo" : "http://example.com/foo/",
           "baz" : "http://example.com/baz/",
           "bar" : "http://example.com/baz/"
        },
        "include_properties": ["list_of", "other", "registry", "entries"],
        "prefix_rules": {
            "id": "bar",
            "properties": [
                "foo", ["some_prop"]
                "baz", ["**"]
            ]
        }
    }

Prefixes
^^^^^^^^

Each entity referenced by these keys contain at least a single property ``prefixes`` which is a entity containing prefix
to URI mappings for CURIE generation or expansion. These registry items can also contain a list property ``prefix_includes``
which must be references to existing RDF registry keys. When looking up items in the RDF registry, any prefix elements
in this list will be recursively included. Take care that you don't have overlapping prefix names, as the final result
will be undefined.

Built-in prefixes
^^^^^^^^^^^^^^^^^

The Sesam RDF registry has built-in support for the common prefixes in RDF, such as ``rdf``, ``rdfs`` and ``owl``.
In other words, you do not have to define these to use them in your CURIES.

Prefix rules
^^^^^^^^^^^^

The final property that can exist in an RDF registry item is ``prefix_rules``. This element tells us how to create RDF
CURIES from a plain entity: the ``id`` property contains the prefix to use for the ``_id`` property of the entity
(i.e. the subject in RDF) and the ``properties`` property is a list of property pairs that encode the rules for what
prefix to apply to which property of the entity.

The ``properties`` format is tuples of string/list pairs, where the first item is the prefix to add and the second is
the path expression that is used to match against. The number of elements in the list must be even. Path expressions
are evaluated in order and the first matching path expression will win, so if a path expression matches the prefix will
be assigned to the matching key.

A path expression is a list of strings. The left-most string value is the most specific. ``**`` can be used to denote
nestedness at an arbitrary depth. ``*`` can be used as a wildcard in the string values themselves.

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

To RDF form using CURIES. We start by defining the rules for this transformation in the RDF registry entry ``my_entry``:

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


We then add a :ref:`properties to CURIES transform <properties_to_curies>` to the start of our pipe's
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

The URIs to CURIES transform
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
       "_id": "~rfoo:bar",
       "<foo_schema:some_predicate>": "Some literal",
       "<foo_schema:other_predicate>": "~rfoo:zoo"
    }

RDF in transforms
=================

The Sesam DTL language features several functions that are useful when working with RDF data in your flow.

Accessing CURIES properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When addressing properties in CURIES form in DTL transform, you can simply use their names verbatim. For example:

::

    ..
    ["rename", "<foo:third_predicate>", "<foo:some_predicate>"],
    ["copy", "_S.<foo_schema:other_predicate>"],
    ["add", "<rdfs:label>", "Bob"]
    ..

You can also use the CURIES in path expressions in the same way as any other property name. If you want to add a URI
literal as part of your transformed entity you can use the DTL :ref:``curie function <curie_function>``, which takes
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
^^^^^^^^^^^^^^^^^^^^^^

When processing RDF data in a flow, we sometimes would like to expand an entity or a child entity from CURIES to full
URI form (for example if there are conflicting usages of prefixes). This can be done using the DTL
:ref:``uri-expand <uri_expand_function>``:

::

    ..
    ["add", "<baz:expanded>", ["uri-expand", ["string", "my_entry"], {"_id": "<foo:bob>", "<foo:name>": "Bob Jones"}]]
    ..

This will expand the properties of the entity (here shown inline, but typically will be from a ``hops`` join or some
other function) to its "full" form:

::

    {
      ..
      "<baz:expanded>": {
          "_id": "http://example.com/foo/bob",
          "http://example.com/foo/name": "Bob Jones"
      }
      ..
    }

Note that expanding CURIES is normally done at the endpoint of your flow (i.e. the sink or a SDShare feed, see below).
However, if the sink you are using to output the final data is not RDF aware (i.e. supports automatic prefix expansion)
you can use the ``uri-expand`` function to achieve the same functionality.

RDF output
==========

Sesam has several ways of outputting RDF data:

* :ref:`The SPARQL sink <sparql_sink>`
* :ref:`The SDShare Push sink <sdshare_push_sink>`
* :ref:`The Databrowser sink <databrowser_sink>`
* :ref:`The HTTP endpoint sink <http_endpoint_sink>`

Consult the reference documentation for how to set up and use these sinks.

