===============================
Unieconomy to Wikidata Dataflow
===============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Wikidata. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Countries to Wikidata Country
----------------------------------------
Before any synchronization can take place, a link between a Unieconomy Countries and a Wikidata Country must be established.

A Unieconomy Countries will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Wikidata Country Property
   * - Name
     - ps:P1476
   * - CountryCode
     - ps:P297

Once a link between a Unieconomy Countries and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Countries and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Wikidata Country Property
     - Wikidata Data Type

