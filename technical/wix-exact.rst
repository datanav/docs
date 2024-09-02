====================
Wix.com to  Dataflow
====================

Generated: 2024-09-02 11:48:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Contacts
-----------------------------
Every Wix.com Contacts will be synchronized with a  Contacts.

Once a link between a Wix.com Contacts and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contacts Property
     -  Data Type
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


Wix.com Currencies to  Currencies
---------------------------------
Every Wix.com Currencies will be synchronized with a  Currencies.

Once a link between a Wix.com Currencies and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     -  Currencies Property
     -  Data Type


Wix.com Orders to  Salesorderlines
----------------------------------
Every Wix.com Orders will be synchronized with a  Salesorderlines.

Once a link between a Wix.com Orders and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - OrderID
     - "string"
   * - lineItems.productId
     - Item
     - "string"


Wix.com Orders to  Salesorders
------------------------------
Every Wix.com Orders will be synchronized with a  Salesorders.

Once a link between a Wix.com Orders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorders Property
     -  Data Type
   * - currency
     - Currency
     - "string"


Wix.com Products to  Items
--------------------------
Every Wix.com Products will be synchronized with a  Items.

Once a link between a Wix.com Products and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Items Property
     -  Data Type

