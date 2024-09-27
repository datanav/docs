==============================
Shopify to Custom PMS Dataflow
==============================

Generated: 2024-09-27 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Custom PMS. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Custom PMS Customer
---------------------------------------
Every Shopify Customer will be synchronized with a Custom PMS Customer.

Once a link between a Shopify Customer and a Custom PMS Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Custom PMS Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Custom PMS Customer Property
     - Custom PMS Data Type

