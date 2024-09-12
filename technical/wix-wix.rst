=======================
Wix.com to Wix Dataflow
=======================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wix Contacts must be established.

A Wix.com Contacts will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Contacts Property
   * - primaryInfo.email
     - primaryInfo.email

Once a link between a Wix.com Contacts and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Contacts Property
     - Wix Data Type
   * - info.name.first
     - info.name.last
     - "string"
   * - info.name.last
     - info.name.first
     - "string"


Wix.com Contacts to Wix Members
-------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wix Members must be established.

A Wix.com Contacts will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Members Property
   * - primaryInfo.email
     - loginEmail

Once a link between a Wix.com Contacts and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Members Property
     - Wix Data Type
   * - info.emails
     - loginEmail
     - "string"
   * - primaryInfo.email
     - loginEmail
     - "string"


Wix.com Currencies to Wix Currencies
------------------------------------
Before any synchronization can take place, a link between a Wix.com Currencies and a Wix Currencies must be established.

A Wix.com Currencies will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Wix Currencies Property
   * - code
     - code

Once a link between a Wix.com Currencies and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Wix Currencies Property
     - Wix Data Type


Wix.com Inventory to Wix Inventory
----------------------------------
Before any synchronization can take place, a link between a Wix.com Inventory and a Wix Inventory must be established.

A Wix.com Inventory will merge with a Wix Inventory if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wix Inventory Property
   * - id
     - id
   * - productId
     - productId

Once a link between a Wix.com Inventory and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wix Inventory Property
     - Wix Data Type


Wix.com Inventory to Wix Products
---------------------------------
Before any synchronization can take place, a link between a Wix.com Inventory and a Wix Products must be established.

A Wix.com Inventory will merge with a Wix Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wix Products Property
   * - productId
     - id
   * - id
     - inventoryItemId

Once a link between a Wix.com Inventory and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wix Products Property
     - Wix Data Type
   * - id
     - inventoryItemId
     - "string"


Wix.com Members to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wix Contacts must be established.

A Wix.com Members will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Contacts Property
   * - loginEmail
     - primaryInfo.email

Once a link between a Wix.com Members and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Contacts Property
     - Wix Data Type
   * - loginEmail
     - info.emails
     - "string"
   * - loginEmail
     - primaryInfo.email
     - "string"


Wix.com Members to Wix Members
------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wix Members must be established.

A Wix.com Members will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Members Property
   * - loginEmail
     - loginEmail

Once a link between a Wix.com Members and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Members Property
     - Wix Data Type


Wix.com Products to Wix Inventory
---------------------------------
Before any synchronization can take place, a link between a Wix.com Products and a Wix Inventory must be established.

A Wix.com Products will merge with a Wix Inventory if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wix Inventory Property
   * - id
     - productId
   * - inventoryItemId
     - id

Once a link between a Wix.com Products and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wix Inventory Property
     - Wix Data Type


Wix.com Products to Wix Products
--------------------------------
Before any synchronization can take place, a link between a Wix.com Products and a Wix Products must be established.

A Wix.com Products will merge with a Wix Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wix Products Property
   * - id
     - id
   * - inventoryItemId
     - inventoryItemId

Once a link between a Wix.com Products and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wix Products Property
     - Wix Data Type
   * - costRange.maxValue
     - costAndProfitData.itemCost
     - N/A

