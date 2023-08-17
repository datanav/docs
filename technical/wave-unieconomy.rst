=====================================
Wave Financial to UniEconomy Dataflow
=====================================

Generated: 2023-08-17 08:57:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to UniEconomy Customers
-------------------------------------
Every Wave Customer will be synchronized with a UniEconomy Customers.

Once a link between a Wave Customer and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - website
     - WebUrl
     - "string"

