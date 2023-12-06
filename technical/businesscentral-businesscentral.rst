============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-06 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Items
-------------------------------
Before any synchronization can take place, a link between a Businesscentral Items and a  Items must be established.

A Businesscentral Items will merge with a  Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Items Property
   * - gtin
     - gtin

Once a link between a Businesscentral Items and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Items:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Items Property
     -  Data Type
   * - itemCategoryId
     - taxGroupId
     - "string"
   * - taxGroupId
     - itemCategoryId
     - "string"


Businesscentral Contacts company to  Companies
----------------------------------------------
Every Businesscentral Contacts company will be synchronized with a  Companies.

Once a link between a Businesscentral Contacts company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts company Property
     -  Companies Property
     -  Data Type


Businesscentral Customers to  Companies
---------------------------------------
Every Businesscentral Customers will be synchronized with a  Companies.

Once a link between a Businesscentral Customers and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Companies Property
     -  Data Type


Businesscentral Customers company to  Companies
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Companies.

Once a link between a Businesscentral Customers company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Companies Property
     -  Data Type

