============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-28 07:51:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Customers company
-------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customers company.

Once a link between a Businesscentral Customers company and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customers company Property
     -  Data Type


Businesscentral Customers person to  Customers person
-----------------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customers person.

Once a link between a Businesscentral Customers person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customers person Property
     -  Data Type
   * - addressLine1
     - address1
     - "string"
   * - addressLine2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - postalCode
     - postal_code
     - "string"

