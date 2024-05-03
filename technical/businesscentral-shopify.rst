============================
Businesscentral to  Dataflow
============================

Generated: 2024-05-03 11:53:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Inventoryitem
---------------------------------------
Every Businesscentral Items will be synchronized with a  Inventoryitem.

Once a link between a Businesscentral Items and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Inventoryitem Property
     -  Data Type


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


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type

