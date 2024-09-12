================================
Shopify to Exact Online Dataflow
================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to Exact Online Items
-------------------------------------
Every Shopify Product will be synchronized with a Exact Online Items.

Once a link between a Shopify Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Exact Online Items Property
     - Exact Online Data Type


Shopify Customer to Exact Online Contacts
-----------------------------------------
Every Shopify Customer will be synchronized with a Exact Online Contacts.

Once a link between a Shopify Customer and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Shopify Inventoryitem to Exact Online Items
-------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Exact Online Items.

Once a link between a Shopify Inventoryitem and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Exact Online Items Property
     - Exact Online Data Type


Shopify Order to Exact Online Quotations
----------------------------------------
Every Shopify Order will be synchronized with a Exact Online Quotations.

Once a link between a Shopify Order and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency
     - Currency
     - "string"
   * - customer.id
     - DeliveryAddress
     - "string"
   * - id
     - DeliveryAddress
     - "string"


Shopify Customer to Exact Online Currencies
-------------------------------------------
Every Shopify Customer will be synchronized with a Exact Online Currencies.

Once a link between a Shopify Customer and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - default_address.country_name
     - Description
     - "string"


Shopify Order to Exact Online Salesorderlines
---------------------------------------------
Every Shopify Order will be synchronized with a Exact Online Salesorderlines.

Once a link between a Shopify Order and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - id
     - OrderID
     - "string"


Shopify Order to Exact Online Salesorders
-----------------------------------------
Every Shopify Order will be synchronized with a Exact Online Salesorders.

Once a link between a Shopify Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - created_at
     - OrderDate
     - "string"
   * - currency
     - Currency
     - "string"


Shopify Sesamproduct to Exact Online Items
------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Exact Online Items.

Once a link between a Shopify Sesamproduct and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Exact Online Items Property
     - Exact Online Data Type

