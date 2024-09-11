===============================
Shopify to ExactOnline Dataflow
===============================

Generated: 2024-09-11 08:39:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to ExactOnline Items
------------------------------------
Every Shopify Product will be synchronized with a ExactOnline Items.

Once a link between a Shopify Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type


Shopify Customer to Exact Contacts
----------------------------------
Every Shopify Customer will be synchronized with a Exact Contacts.

Once a link between a Shopify Customer and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Exact Contacts Property
     - Exact Data Type
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


Shopify Inventoryitem to Exact Items
------------------------------------
Every Shopify Inventoryitem will be synchronized with a Exact Items.

Once a link between a Shopify Inventoryitem and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Exact Items Property
     - Exact Data Type


Shopify Order to Exact Quotations
---------------------------------
Every Shopify Order will be synchronized with a Exact Quotations.

Once a link between a Shopify Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - customer.id
     - DeliveryAddress
     - "string"
   * - id
     - DeliveryAddress
     - "string"


Shopify Customer to ExactOnline Currencies
------------------------------------------
Every Shopify Customer will be synchronized with a ExactOnline Currencies.

Once a link between a Shopify Customer and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - default_address.country_name
     - Description
     - "string"


Shopify Order to ExactOnline Salesorderlines
--------------------------------------------
Every Shopify Order will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Shopify Order and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - id
     - OrderID
     - "string"


Shopify Order to ExactOnline Salesorders
----------------------------------------
Every Shopify Order will be synchronized with a ExactOnline Salesorders.

Once a link between a Shopify Order and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - created_at
     - OrderDate
     - "string"
   * - currency
     - Currency
     - "string"


Shopify Sesamproduct to ExactOnline Items
-----------------------------------------
Every Shopify Sesamproduct will be synchronized with a ExactOnline Items.

Once a link between a Shopify Sesamproduct and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - ExactOnline Items Property
     - ExactOnline Data Type

