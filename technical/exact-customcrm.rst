==================
Exact to  Dataflow
==================

Generated: 2024-09-10 13:27:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Customer
---------------------------
Every Exact Accounts will be synchronized with a  Customer.

Once a link between a Exact Accounts and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Customer:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Customer Property
     -  Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
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

