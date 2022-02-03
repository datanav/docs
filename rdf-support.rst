.. _working-with-RDF:

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

First, a short recap of the core concepts when working with RDF, see the `RDF standard <https://www.w3.org/RDF/>`_ for more details:

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
concept of *prefixes* and `RDF CURIEs <https://www.w3.org/TR/curie/>`_. A *prefix* is the "constant" part of a URL,
i.e. everything up to a certain path-element (usually the last). Using CURIEs means giving these common prefixes short
hand names enabling us to rewrite the full URI to a shorter "prefix:path" form.

Let us define some prefixes for the above example, and give them such short hand names. The example below is in
`RDF Turtle format <https://www.w3.org/TR/turtle/>`_, which is a superset of NTriples. Turtle syntax supports prefixes
and CURIEs and is often used when writing RDF manually or intended to be read by humans. In general, it is considered
good practice to reduce full URIs to CURIEs using prefixes whenever possible. When working with RDF in Sesam we try to
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

.. _rdf-input:

RDF input
=========

Sesam supports RDF input from several different sources:

* :ref:`The RDF source <rdf_source>`
* :ref:`The SDShare source <sdshare_source>`
* :ref:`The SPARQL source <sparql_source>`

Additionally, you can set up a :ref:`HTTP endpoint source <http_endpoint_source>` which includes a `SDShare Push` capable
HTTP endpoint where you can post RDF data in NTriples format in accordance with the ``SDShare Push protocol``.

.. _rdf-output:

RDF output
==========

Sesam has several ways of outputting RDF data:

* :ref:`The SPARQL sink <sparql_sink>`
* :ref:`The SDShare Push sink <sdshare_sink>`
* :ref:`The Databrowser sink <databrowser_sink>`
* :ref:`The HTTP endpoint sink <http_endpoint_sink>`

Consult the reference documentation for how to set up and use these sinks to produce RDF output.

Notes on the RDF output
-----------------------

When converting your entities to RDF, some rules are applied:

 * Nested entities will be represented as `RDF Blank Nodes <https://en.wikipedia.org/wiki/Blank_node>`_ (aka BNodes),
 * List properties are represented by repeating the predicates as many times as there are entries in the lists
 * RDF datatypes are automatically added based on the type of the property
 * RDF language tags are currently not supported

Note that many RDF capable receivers are unable to deal with BNodes, so be sure to check this before finalizing
your flow configuration. If your data is nested and the receiver doesn't support BNodes, you must "flatten" your entity using a
DTL transform before being sent to the sink (see the DTL :ref:`merge <dtl_transform-merge>` and :ref:`merge-union <dtl_transform-merge-union>` functions).

SDShare feeds from datasets
---------------------------

Datasets feature built-in support for SDShare feeds. The SDShare feed from a dataset is available through the :ref:`Sesam REST API <sdshare_feed_from_dataset>`.
