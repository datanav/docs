====================================
Shopify to Business Central Dataflow
====================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Business Central Customers company
------------------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Shopify Product to Business Central Items
-----------------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Business Central Items must be established.

A new Business Central Items will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Business Central Items Property
     - Business Central Data Type


Shopify Customer to Business Central Currencies
-----------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Currencies.

Once a link between a Shopify Customer and a Business Central Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Currencies:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Currencies Property
     - Business Central Data Type


Shopify Customer to Business Central Customers person
-----------------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Customers person.

Once a link between a Shopify Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - addresses.address1
     - addressLine1
     - "string"
   * - addresses.address2
     - addressLine2
     - "string"
   * - addresses.city
     - city
     - "string"
   * - addresses.country
     - country
     - "string"
   * - addresses.zip
     - postalCode
     - "string"
   * - default_address.address1
     - addressLine1
     - "string"
   * - default_address.address2
     - addressLine2
     - "string"
   * - default_address.city
     - city
     - "string"
   * - default_address.country
     - country
     - "string"
   * - default_address.phone
     - phoneNumber
     - "string"
   * - default_address.zip
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phone
     - phoneNumber
     - "string"


Shopify Order to Business Central Salesorderlines
-------------------------------------------------
Every Shopify Order will be synchronized with a Business Central Salesorderlines.

Once a link between a Shopify Order and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - id
     - documentId
     - "string"
   * - line_items.price
     - unitPrice
     - "float"
   * - line_items.quantity
     - quantity
     - N/A
   * - line_items.title
     - description
     - "string"
   * - line_items.total_discount
     - discountPercent
     - N/A


Shopify Order to Business Central Salesorders
---------------------------------------------
Every Shopify Order will be synchronized with a Business Central Salesorders.

Once a link between a Shopify Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - billing_address.address1
     - billToAddressLine1
     - "string"
   * - billing_address.address1
     - shipToAddressLine1
     - "string"
   * - billing_address.address2
     - billToAddressLine2
     - "string"
   * - billing_address.address2
     - shipToAddressLine2
     - "string"
   * - billing_address.city
     - billToCity
     - "string"
   * - billing_address.city
     - shipToCity
     - "string"
   * - billing_address.country
     - billToCountry
     - "string"
   * - billing_address.country
     - shipToCountry
     - "string"
   * - billing_address.zip
     - billToPostCode
     - "string"
   * - billing_address.zip
     - shipToPostCode
     - "string"
   * - created_at
     - orderDate
     - N/A
   * - currency
     - currencyId
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - customer.id
     - id
     - "string"
   * - id
     - id
     - "string"
   * - shipping_address.address1
     - billToAddressLine1
     - "string"
   * - shipping_address.address1
     - shipToAddressLine1
     - "string"
   * - shipping_address.address2
     - billToAddressLine2
     - "string"
   * - shipping_address.address2
     - shipToAddressLine2
     - "string"
   * - shipping_address.city
     - billToCity
     - "string"
   * - shipping_address.city
     - shipToCity
     - "string"
   * - shipping_address.country
     - billToCountry
     - "string"
   * - shipping_address.country
     - shipToCountry
     - "string"
   * - shipping_address.zip
     - billToPostCode
     - "string"
   * - shipping_address.zip
     - shipToPostCode
     - "string"


Shopify Sesamproduct to Business Central Items
----------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Business Central Items.

Once a link between a Shopify Sesamproduct and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Business Central Items Property
     - Business Central Data Type
   * - sesam_priceExclVAT
     - unitPrice
     - N/A
   * - title
     - displayName
     - "string"
   * - variants.price
     - unitPrice
     - N/A

