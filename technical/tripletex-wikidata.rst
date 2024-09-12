==============================
Tripletex to Wikidata Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wikidata. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Country to Wikidata Country
-------------------------------------
Before any synchronization can take place, a link between a Tripletex Country and a Wikidata Country must be established.

A Tripletex Country will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Wikidata Country Property
   * - name
     - ps:P1476
   * - isoAlpha2Code
     - ps:P297
   * - isoAlpha3Code
     - ps:P298

Once a link between a Tripletex Country and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Wikidata Country Property
     - Wikidata Data Type

