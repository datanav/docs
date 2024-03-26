====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Contacts
-----------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Contacts must be established.

A Wix.com Contacts will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contacts Property
   * - primaryInfo.email
     - primaryInfo.email

Once a link between a Wix.com Contacts and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contacts Property
     -  Data Type
   * - info.name.first
     - info.name.last
     - "string"
   * - info.name.last
     - info.name.first
     - "string"


Wix.com Inventory to  Products
------------------------------
Before any synchronization can take place, a link between a Wix.com Inventory and a  Products must be established.

A Wix.com Inventory will merge with a  Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     -  Products Property
   * - productId
     - id
   * - id
     - inventoryItemId

Once a link between a Wix.com Inventory and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a  Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     -  Products Property
     -  Data Type
   * - id
     - inventoryItemId
     - "string"


Wix.com Members to  Contacts
----------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Contacts must be established.

A Wix.com Members will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contacts Property
   * - loginEmail
     - primaryInfo.email

Once a link between a Wix.com Members and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contacts Property
     -  Data Type
   * - loginEmail
     - info.emails
     - "string"
   * - loginEmail
     - primaryInfo.email
     - "string"


Wix.com Products to  Products
-----------------------------
Before any synchronization can take place, a link between a Wix.com Products and a  Products must be established.

A Wix.com Products will merge with a  Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Products Property
   * - id
     - id
   * - inventoryItemId
     - inventoryItemId

Once a link between a Wix.com Products and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Products Property
     -  Data Type
   * - costRange.maxValue
     - costAndProfitData.itemCost
     - "decimal"

