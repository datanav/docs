=========================
Wix.com to Exact Dataflow
=========================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Exact Contacts
----------------------------------
Every Wix.com Contacts will be synchronized with a Exact Contacts.

Once a link between a Wix.com Contacts and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Exact Contacts Property
     - Exact Data Type
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - Email
     - "string"
   * - primaryInfo.phone
     - Phone
     - "string"


Wix.com Currencies to Exact Currencies
--------------------------------------
Every Wix.com Currencies will be synchronized with a Exact Currencies.

Once a link between a Wix.com Currencies and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Exact Currencies Property
     - Exact Data Type


Wix.com Orders to Exact Salesorderlines
---------------------------------------
Every Wix.com Orders will be synchronized with a Exact Salesorderlines.

Once a link between a Wix.com Orders and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - id
     - OrderID
     - "string"
   * - lineItems.productId
     - Item
     - "string"


Wix.com Orders to Exact Salesorders
-----------------------------------
Every Wix.com Orders will be synchronized with a Exact Salesorders.

Once a link between a Wix.com Orders and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"


Wix.com Products to Exact Items
-------------------------------
Every Wix.com Products will be synchronized with a Exact Items.

Once a link between a Wix.com Products and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Exact Items Property
     - Exact Data Type

