===========================
Exact to Customcrm Dataflow
===========================

Generated: 2024-09-10 14:09:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Customcrm Customer
------------------------------------
Every Exact Accounts will be synchronized with a Customcrm Customer.

Once a link between a Exact Accounts and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - ID
     - Id
     - "string"
   * - Name
     - Name
     - "string"
   * - Postcode
     - ZipCode
     - "string"
   * - Website
     - Website
     - "string"

