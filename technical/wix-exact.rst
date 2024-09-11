===============================
Wix.com to ExactOnline Dataflow
===============================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to ExactOnline Contacts
----------------------------------------
Every Wix.com Contacts will be synchronized with a ExactOnline Contacts.

Once a link between a Wix.com Contacts and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Wix.com Currencies to ExactOnline Currencies
--------------------------------------------
Every Wix.com Currencies will be synchronized with a ExactOnline Currencies.

Once a link between a Wix.com Currencies and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type


Wix.com Orders to ExactOnline Salesorderlines
---------------------------------------------
Every Wix.com Orders will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Wix.com Orders and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - id
     - OrderID
     - "string"
   * - lineItems.productId
     - Item
     - "string"


Wix.com Orders to ExactOnline Salesorders
-----------------------------------------
Every Wix.com Orders will be synchronized with a ExactOnline Salesorders.

Once a link between a Wix.com Orders and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - currency
     - Currency
     - "string"


Wix.com Products to ExactOnline Items
-------------------------------------
Every Wix.com Products will be synchronized with a ExactOnline Items.

Once a link between a Wix.com Products and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - ExactOnline Items Property
     - ExactOnline Data Type

