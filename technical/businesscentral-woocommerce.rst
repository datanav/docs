=======================================
BusinessCentral to WooCommerce Dataflow
=======================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentralBusiness CentralBusinesscentral Items to WooCommerceWoocommerce Product
--------------------------------------------------------------------------------------
Every BusinessCentralBusiness CentralBusinesscentral Items will be synchronized with a WooCommerceWoocommerce Product.

Once a link between a BusinessCentralBusiness CentralBusinesscentral Items and a WooCommerceWoocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentralBusiness CentralBusinesscentral Items and a WooCommerceWoocommerce Product:

.. list-table::
   :header-rows: 1

   * - BusinessCentralBusiness CentralBusinesscentral Items Property
     - WooCommerceWoocommerce Product Property
     - WooCommerceWoocommerce Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - price
     - "string"
   * - unitPrice
     - sale_price
     - "string"


BusinessCentralBusiness CentralBusinesscentral Salesorders to WooCommerceWoocommerce Order
------------------------------------------------------------------------------------------
Every BusinessCentralBusiness CentralBusinesscentral Salesorders will be synchronized with a WooCommerceWoocommerce Order.

Once a link between a BusinessCentralBusiness CentralBusinesscentral Salesorders and a WooCommerceWoocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentralBusiness CentralBusinesscentral Salesorders and a WooCommerceWoocommerce Order:

.. list-table::
   :header-rows: 1

   * - BusinessCentralBusiness CentralBusinesscentral Salesorders Property
     - WooCommerceWoocommerce Order Property
     - WooCommerceWoocommerce Data Type
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

