================================
Wix.com to Exact Online Dataflow
================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Exact Online Contacts
-----------------------------------------
Every Wix.com Contacts will be synchronized with a Exact Online Contacts.

Once a link between a Wix.com Contacts and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Wix.com Currencies to Exact Online Currencies
---------------------------------------------
Every Wix.com Currencies will be synchronized with a Exact Online Currencies.

Once a link between a Wix.com Currencies and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Exact Online Currencies Property
     - Exact Online Data Type


Wix.com Orders to Exact Online Salesorderlines
----------------------------------------------
Every Wix.com Orders will be synchronized with a Exact Online Salesorderlines.

Once a link between a Wix.com Orders and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - id
     - OrderID
     - "string"
   * - lineItems.productId
     - Item
     - "string"


Wix.com Orders to Exact Online Salesorders
------------------------------------------
Every Wix.com Orders will be synchronized with a Exact Online Salesorders.

Once a link between a Wix.com Orders and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currency
     - Currency
     - "string"


Wix.com Products to Exact Online Items
--------------------------------------
Every Wix.com Products will be synchronized with a Exact Online Items.

Once a link between a Wix.com Products and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Exact Online Items Property
     - Exact Online Data Type

