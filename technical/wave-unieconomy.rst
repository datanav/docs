=====================================
Wave Financial to Unieconomy Dataflow
=====================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Unieconomy Customers
-------------------------------------
Every Wave Customer will be synchronized with a Unieconomy Customers.

Once a link between a Wave Customer and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - website
     - WebUrl
     - "string"

