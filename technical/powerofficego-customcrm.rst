==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-09-10 13:23:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Customer
------------------------------------
Every Powerofficego Customers will be synchronized with a  Customer.

Once a link between a Powerofficego Customers and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customer Property
     -  Data Type
   * - MailAddress.AddressLine1
     - StreetAddress1
     - "string"
   * - MailAddress.AddressLine2
     - StreetAddress2
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.ZipCode
     - ZipCode
     - "string"
   * - Name
     - Name
     - "string"
   * - WebsiteUrl
     - Website
     - "string"

