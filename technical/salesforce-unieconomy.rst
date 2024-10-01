=================================
Salesforce to Unieconomy Dataflow
=================================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Unieconomy Customers
-------------------------------------------
Every Salesforce Customer will be synchronized with a Unieconomy Customers.

Once a link between a Salesforce Customer and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Unieconomy Customers Property
     - Unieconomy Data Type


Salesforce Organization to Unieconomy Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Unieconomy Companies.

Once a link between a Salesforce Organization and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - Name
     - Name
     - "string"

