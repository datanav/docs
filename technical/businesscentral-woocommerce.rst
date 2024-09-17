========================================
Business Central to WooCommerce Dataflow
========================================

Generated: 2024-09-17 07:28:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Items to WooCommerce Product
---------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a WooCommerce Product must be established.

A new WooCommerce Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorders that is synchronized into WooCommerce.

Once a link between a Business Central Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - price
     - "string"
   * - unitPrice
     - sale_price
     - "string"


Business Central Salesorders to WooCommerce Order
-------------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a WooCommerce Order must be established.

A new WooCommerce Order will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorders that is synchronized into WooCommerce.

Once a link between a Business Central Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - billToAddressLine1
     - billing.address_1
     - "string"
   * - billToAddressLine1
     - shipping.address_1
     - "string"
   * - billToAddressLine2
     - billing.address_2
     - "string"
   * - billToAddressLine2
     - shipping.address_2
     - "string"
   * - billToCity
     - billing.city
     - "string"
   * - billToCity
     - shipping.city
     - "string"
   * - billToCountry
     - billing.country
     - "string"
   * - billToCountry
     - shipping.country
     - "string"
   * - billToPostCode
     - billing.postcode
     - "string"
   * - billToPostCode
     - shipping.postcode
     - "string"
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer_id
     - "string"
   * - id
     - id
     - "string"
   * - shipToAddressLine1
     - billing.address_1
     - "string"
   * - shipToAddressLine1
     - shipping.address_1
     - "string"
   * - shipToAddressLine2
     - billing.address_2
     - "string"
   * - shipToAddressLine2
     - shipping.address_2
     - "string"
   * - shipToCity
     - billing.city
     - "string"
   * - shipToCity
     - shipping.city
     - "string"
   * - shipToCountry
     - billing.country
     - "string"
   * - shipToCountry
     - shipping.country
     - "string"
   * - shipToPostCode
     - billing.postcode
     - "string"
   * - shipToPostCode
     - shipping.postcode
     - "string"


Business Central Items to WooCommerce Product
---------------------------------------------
Every Business Central Items will be synchronized with a WooCommerce Product.

Once a link between a Business Central Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type


Business Central Salesorders to WooCommerce Order
-------------------------------------------------
Every Business Central Salesorders will be synchronized with a WooCommerce Order.

Once a link between a Business Central Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type

