============================
Businesscentral to  Dataflow
============================

Generated: 2024-09-10 14:00:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Customer
--------------------------------------
Every Businesscentral Companies will be synchronized with a  Customer.

Once a link between a Businesscentral Companies and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Customer Property
     -  Data Type


Businesscentral Customers company to  Customer
----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customer.

Once a link between a Businesscentral Customers company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customer Property
     -  Data Type
   * - addressLine1
     - StreetAddress1
     - "string"
   * - addressLine2
     - StreetAddress2
     - "string"
   * - city
     - City
     - "string"
   * - displayName
     - Name
     - "string"
   * - email
     - Email
     - "string"
   * - postalCode
     - ZipCode
     - "string"
   * - website
     - Website
     - "string"

