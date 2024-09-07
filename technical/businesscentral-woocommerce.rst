=======================================
Businesscentral to Woocommerce Dataflow
=======================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to Woocommerce Product
--------------------------------------------
Every Businesscentral Items will be synchronized with a Woocommerce Product.

Once a link between a Businesscentral Items and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - price
     - "string"
   * - unitPrice
     - sale_price
     - "string"


Businesscentral Salesorders to Woocommerce Order
------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Woocommerce Order.

Once a link between a Businesscentral Salesorders and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Woocommerce Order Property
     - Woocommerce Data Type
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

