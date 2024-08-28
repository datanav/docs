==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-28 09:32:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers person to  Customer
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customer.

Once a link between a Powerofficego Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customer Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"

