=======================
Wix.com to Wix Dataflow
=======================

Generated: 2023-09-05 14:05:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wix Members
-------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wix Members must be established.

A Wix.com Contacts will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Members Property
   * - info.emails
     - loginEmail
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
Every Wix.com Members will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Wix.com Members will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Wix.com Members will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Contacts Property
   * - loginEmail
     - info.emails
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


Wix.com Products to Wix Inventory
---------------------------------
Every Wix.com Products will be synchronized with a Wix Inventory.

If a matching Wix Inventory already exists, the Wix.com Products will be merged with the existing one.
If no matching Wix Inventory is found, a new Wix Inventory will be created.

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

