======================================
Unieconomy to Businesscentral Dataflow
======================================

Generated: 2024-03-26 14:26:08

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Customers to Businesscentral Customers company
---------------------------------------------------------
Every Unieconomy Customers will be synchronized with a Businesscentral Customers company.

Once a link between a Unieconomy Customers and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
   * - WebUrl
     - website
     - "string"

