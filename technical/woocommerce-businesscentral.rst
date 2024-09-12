========================================
WooCommerce to Business Central Dataflow
========================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Business Central Customers person
---------------------------------------------------------
Every WooCommerce Customer will be synchronized with a Business Central Customers person.

Once a link between a WooCommerce Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - email
     - email
     - "string"


WooCommerce Order to Business Central Currencies
------------------------------------------------
Every WooCommerce Order will be synchronized with a Business Central Currencies.

If a matching Business Central Currencies already exists, the WooCommerce Order will be merged with the existing one.
If no matching Business Central Currencies is found, a new Business Central Currencies will be created.

A WooCommerce Order will merge with a Business Central Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Currencies Property
   * - currency
     - code

Once a link between a WooCommerce Order and a Business Central Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Central Currencies:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Currencies Property
     - Business Central Data Type


WooCommerce Order to Business Central Salesorderlines
-----------------------------------------------------
Every WooCommerce Order will be synchronized with a Business Central Salesorderlines.

Once a link between a WooCommerce Order and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - id
     - documentId
     - "string"
   * - line_items.name
     - description
     - "string"
   * - line_items.price
     - unitPrice
     - "float"
   * - line_items.quantity
     - quantity
     - N/A


WooCommerce Order to Business Central Salesorders
-------------------------------------------------
Every WooCommerce Order will be synchronized with a Business Central Salesorders.

Once a link between a WooCommerce Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - billing.address_1
     - billToAddressLine1
     - "string"
   * - billing.address_1
     - shipToAddressLine1
     - "string"
   * - billing.address_2
     - billToAddressLine2
     - "string"
   * - billing.address_2
     - shipToAddressLine2
     - "string"
   * - billing.city
     - billToCity
     - "string"
   * - billing.city
     - shipToCity
     - "string"
   * - billing.country
     - billToCountry
     - "string"
   * - billing.country
     - shipToCountry
     - "string"
   * - billing.postcode
     - billToPostCode
     - "string"
   * - billing.postcode
     - shipToPostCode
     - "string"
   * - currency
     - currencyId
     - "string"
   * - customer_id
     - customerId
     - "string"
   * - id
     - id
     - "string"
   * - shipping.address_1
     - billToAddressLine1
     - "string"
   * - shipping.address_1
     - shipToAddressLine1
     - "string"
   * - shipping.address_2
     - billToAddressLine2
     - "string"
   * - shipping.address_2
     - shipToAddressLine2
     - "string"
   * - shipping.city
     - billToCity
     - "string"
   * - shipping.city
     - shipToCity
     - "string"
   * - shipping.country
     - billToCountry
     - "string"
   * - shipping.country
     - shipToCountry
     - "string"
   * - shipping.postcode
     - billToPostCode
     - "string"
   * - shipping.postcode
     - shipToPostCode
     - "string"


WooCommerce Product to Business Central Items
---------------------------------------------
Every WooCommerce Product will be synchronized with a Business Central Items.

Once a link between a WooCommerce Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"
   * - price
     - unitCost
     - N/A
   * - sale_price
     - unitPrice
     - N/A

