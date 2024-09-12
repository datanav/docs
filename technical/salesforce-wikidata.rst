===============================
Salesforce to Wikidata Dataflow
===============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Wikidata. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Wikidata Country
------------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a Wikidata Country must be established.

A Salesforce Order will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Wikidata Country Property
   * - BillingCountryCode
     - ps:P297
   * - ShippingCountryCode
     - ps:P297

Once a link between a Salesforce Order and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Wikidata Country Property
     - Wikidata Data Type


Salesforce Quote to Wikidata Country
------------------------------------
Before any synchronization can take place, a link between a Salesforce Quote and a Wikidata Country must be established.

A Salesforce Quote will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Wikidata Country Property
   * - BillingCountryCode
     - ps:P297
   * - ShippingCountryCode
     - ps:P297

Once a link between a Salesforce Quote and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Wikidata Country Property
     - Wikidata Data Type


Salesforce User to Wikidata Country
-----------------------------------
Before any synchronization can take place, a link between a Salesforce User and a Wikidata Country must be established.

A Salesforce User will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Wikidata Country Property
   * - CountryCode
     - ps:P297

Once a link between a Salesforce User and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Wikidata Country Property
     - Wikidata Data Type

