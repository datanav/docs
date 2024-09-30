=============================================
Business Central to Business Central Dataflow
=============================================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts to Business Central Contacts
------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts and a Business Central Contacts must be established.

A Business Central Contacts will merge with a Business Central Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts Property
     - Business Central Contacts Property
   * - id
     - id

Once a link between a Business Central Contacts and a Business Central Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts and a Business Central Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts Property
     - Business Central Contacts Property
     - Business Central Data Type


Business Central Contactsinformation to Business Central Contacts
-----------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contactsinformation and a Business Central Contacts must be established.

A Business Central Contactsinformation will merge with a Business Central Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation Property
     - Business Central Contacts Property
   * - contactId
     - id

Once a link between a Business Central Contactsinformation and a Business Central Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contactsinformation and a Business Central Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contactsinformation Property
     - Business Central Contacts Property
     - Business Central Data Type
   * - contactName
     - displayName
     - "string"


Business Central Items to Business Central Items
------------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Business Central Items must be established.

A Business Central Items will merge with a Business Central Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Business Central Items Property
   * - gtin
     - gtin

Once a link between a Business Central Items and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Business Central Items Property
     - Business Central Data Type


Business Central Customers (organisation data) to Business Central Companies
----------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Business Central Companies.

Once a link between a Business Central Customers (organisation data) and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Business Central Companies Property
     - Business Central Data Type


Business Central Contacts (classification data) to Business Central Customers (classification data)
---------------------------------------------------------------------------------------------------
Every Business Central Contacts (classification data) will be synchronized with a Business Central Customers (classification data).

Once a link between a Business Central Contacts (classification data) and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (classification data) and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (classification data) Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type
   * - addressLine1
     - addressLine1
     - "string"
   * - addressLine2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - displayName
     - displayName
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - type
     - type
     - "string"


Business Central Customers (human data) to Business Central Customers (human data)
----------------------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Business Central Customers (human data).

Once a link between a Business Central Customers (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Business Central Customers (human data) Property
     - Business Central Data Type


Business Central Customers (classification data) to Business Central Contacts (classification data)
---------------------------------------------------------------------------------------------------
Every Business Central Customers (classification data) will be synchronized with a Business Central Contacts (classification data).

Once a link between a Business Central Customers (classification data) and a Business Central Contacts (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (classification data) and a Business Central Contacts (classification data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (classification data) Property
     - Business Central Contacts (classification data) Property
     - Business Central Data Type
   * - addressLine1
     - addressLine1
     - "string"
   * - addressLine2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - displayName
     - displayName
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - type
     - type
     - "string"


Business Central Customers (organisation data) to Business Central Customers (organisation data)
------------------------------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Business Central Customers (organisation data).

Once a link between a Business Central Customers (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type

