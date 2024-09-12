================================
WooCommerce to Wikidata Dataflow
================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Wikidata. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Wikidata Country
----------------------------------------
Before any synchronization can take place, a link between a WooCommerce Customer and a Wikidata Country must be established.

A WooCommerce Customer will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wikidata Country Property
   * - billing.country
     - ps:P297
   * - shipping.country
     - ps:P297

Once a link between a WooCommerce Customer and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wikidata Country Property
     - Wikidata Data Type


WooCommerce Order to Wikidata Country
-------------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Wikidata Country must be established.

A WooCommerce Order will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wikidata Country Property
   * - billing.country
     - ps:P297
   * - shipping.country
     - ps:P297

Once a link between a WooCommerce Order and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wikidata Country Property
     - Wikidata Data Type

