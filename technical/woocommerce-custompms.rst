==================================
WooCommerce to Custom PMS Dataflow
==================================

Generated: 2024-09-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Custom PMS. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Custom PMS Customer
-------------------------------------------
Every WooCommerce Customer will be synchronized with a Custom PMS Customer.

Once a link between a WooCommerce Customer and a Custom PMS Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Custom PMS Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Custom PMS Customer Property
     - Custom PMS Data Type

