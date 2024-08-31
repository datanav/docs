====================
Shopify to  Dataflow
====================

Generated: 2024-08-31 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Contacts
-----------------------------
Every Shopify Customer will be synchronized with a  Contacts.

Once a link between a Shopify Customer and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Contacts Property
     -  Data Type
   * - default_address.city
     - City
     - "string"
   * - default_address.country
     - Country
     - "string"
   * - default_address.phone
     - Phone
     - "string"
   * - email
     - Email
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"
   * - phone
     - Mobile
     - "string"


Shopify Order to  Quotations
----------------------------
Every Shopify Order will be synchronized with a  Quotations.

Once a link between a Shopify Order and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Quotations Property
     -  Data Type
   * - currency
     - Currency
     - "string"
   * - customer.id
     - DeliveryAddress
     - "string"
   * - id
     - DeliveryAddress
     - "string"


Shopify Customer to  Currencies
-------------------------------
Every Shopify Customer will be synchronized with a  Currencies.

Once a link between a Shopify Customer and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Currencies Property
     -  Data Type
   * - default_address.country_name
     - Description
     - "string"


Shopify Order to  Salesorderlines
---------------------------------
Every Shopify Order will be synchronized with a  Salesorderlines.

Once a link between a Shopify Order and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - OrderID
     - "string"


Shopify Order to  Salesorders
-----------------------------
Every Shopify Order will be synchronized with a  Salesorders.

Once a link between a Shopify Order and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Salesorders Property
     -  Data Type
   * - created_at
     - OrderDate
     - "string"
   * - currency
     - Currency
     - "string"

