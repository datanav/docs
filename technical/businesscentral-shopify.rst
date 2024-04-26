============================
Businesscentral to  Dataflow
============================

Generated: 2024-04-26 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Customer
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Customer.

Once a link between a Businesscentral Contacts person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Customer Property
     -  Data Type
   * - addressLine1
     - addresses.address1
     - "string"
   * - addressLine2
     - addresses.address2
     - "string"
   * - city
     - addresses.city
     - "string"
   * - country
     - addresses.country
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - addresses.zip
     - "string"


Businesscentral Employees to  Customer
--------------------------------------
Every Businesscentral Employees will be synchronized with a  Customer.

Once a link between a Businesscentral Employees and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Customer Property
     -  Data Type
   * - personalEmail
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"


Businesscentral Customers person to  Customer
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customer.

Once a link between a Businesscentral Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customer Property
     -  Data Type
   * - addressLine1
     - addresses.address1
     - "string"
   * - addressLine2
     - addresses.address2
     - "string"
   * - city
     - addresses.city
     - "string"
   * - country
     - addresses.country
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - addresses.zip
     - "string"

