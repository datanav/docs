==================================
WooCommerce to Unieconomy Dataflow
==================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Unieconomy Customers
--------------------------------------------
Every WooCommerce Customer will be synchronized with a Unieconomy Customers.

Once a link between a WooCommerce Customer and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Unieconomy Customers Property
     - Unieconomy Data Type

