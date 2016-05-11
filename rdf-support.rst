================
Working with RDF
================

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

Sesam node has several features to facilitate working with RDF data both as input, when doing transforms and finally
when exposing or producing data for external consumption.

In this document we will cover what you need to know when working with RDF data with the Sesam Node.

Core Concepts
-------------

First, a short recap of the core concepts when working with RDF, see the `RDF standard <https://www.w3.org/standards/techs/rdf#w3c_all>`_ for more detail:

The RDF data model consists in essence of statements about a particular subject. This is given as a *triple*:

::

    subject predicate object


Where subjects and predicates are URIs and object can be either a literal (i.e. a quoted string, representing dates,
numbers, strings etc) or another subject (URI). There are other optional elements to these subjects such as language
and/or datatype identifiers - again refer to the standard for more detail. You can have multiple statements for a single subject.

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

Now, this is pretty straight forward albeit a bit verbose in the long run. Also, it is easy to get typos in the
exact URI patterns we have used. Additionally, if you want to change one of the URI patterns, you will have to reload all
your data. To alleviate this, we can use the concept of *prefixes* and `RDF curies <https://www.w3.org/TR/curie/>`_.
A *prefix* is the "constant" part of a URL, i.e. everything up to a certain path-element (usually the last).

Let us define some prefixes for the above example, and give them short form names:

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

When working with RDF data in the node, we would like to be able to define, maintain and share these RDF prefixes
among our datasets and transforms. To achieve this, the Sesam node has a built-in *RDF registry* for this purpose.
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

The key `rdf` above contains the configuration of the RDF registry. It contains keys which usually correspond
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

Each entity referenced by these keys contain at least a single property `prefixes` which is a entity containing prefix
to URI mappings for CURIE generation or expansion. These registry items can also contain a list property `prefix_includes`
which must be references to existing RDF registry keys. When looking up items in the RDF registry, any prefix elements
in this list will be recursively included. Take care that you don't have overlapping prefix names, as the final result
will be undefined.

Prefix rules
^^^^^^^^^^^^

The final property that can exist in an RDF registry item is `prefix_rules`. This element tells us how to create RDF
CURIES from a plain entity: the `id` property contains the prefix to use for the `_id` property of the entity
(i.e. the subject in RDF) and the `properties` property is a list of property pairs that encode the rules for what
prefix to apply to which property of the entity.

The `properties` format is tuples of string+list pairs, where the first item is the prefix to add and the second is
the path expression that is used to match against. The number of elements in the list must be even. Path expressions
are evaluated in order and the first matching path expression will win, so if a path expression matches the prefix will
be assigned to the matching key.

A path expression is a list of strings. The left-most string value is the most specific. "**" can be used to denote
nestedness at an arbitrary depth. "*" can be used as a wildcard in the string values themselves.

A complete example of how the `prefix_rules` property works; given a pre-existing RDF registry entry ``my_entry``:

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

And a DTL transform configuration:

::

    {
        "type": "properties_to_curies",
        "rule": "my_entry"
    }

And the input entity:

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

The transform will output the following transformed entity. using the RDF registry entry above:

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

The Sesam Node supports RDF input from three different sources:

* :ref:`The RDF source <rdf_source>`
* :ref:`The SDShare source <rdf_source>`
* :ref:`The SPARQL source <sparql_source>`

Additionally, you can set up a :ref:`HTTP endpoint source <_http_endpoint_source>` which includes a `SDShare Push` capable
HTTP endpoint where you can post NTriples data to according to the SDShare Push protocol.


The URIs to CURIES transform
----------------------------

All of these sources will provide entities on the general form:

::

   {
       "_id": "<http://example.com/bar",
       "<http://example.com/schema/some_predicate>": "Some literal",
       "<http://example.com/schema/other_predicate>": "~rhttp://example.com/zoo"
   }

When processing this RDF data further, it is often convenient to transform these entities to CURIE form using the
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

Where `my_entry` in the RDF registry looks like:

::

    ..
    "my_entry": {
        "prefixes": {
            "foo": "http://example.com/",
            "foo_schema": "http://example.com/schema/"
        }
    }
    ..

Will produce the following entity out of the pipe (i.e. before it is entered into any dataset):

::

    {
       "_id": "~rfoo:bar",
       "<foo_schema:some_predicate>": "Some literal",
       "<foo_schema:other_predicate>": "~rfoo:zoo"
    }

RDF output
==========

Sesam node has several ways of outputting RDF data:

* The SPARQL sink
* The SDShare Push sink
* A SDShare feed from a dataset
* The Databrowser sink

