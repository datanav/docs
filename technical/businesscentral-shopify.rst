===================================
Businesscentral to Shopify Dataflow
===================================

Generated: 2024-07-02 11:43:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to Shopify Inventoryitem
----------------------------------------------
Every Businesscentral Items will be synchronized with a Shopify Inventoryitem.

Once a link between a Businesscentral Items and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - unitCost
     - cost
     - "string"


Businesscentral Customers person to Shopify Customer
----------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Shopify Customer.

Once a link between a Businesscentral Customers person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - addressLine1
     - addresses.address1
     - "string"
   * - addressLine1
     - default_address.address1
     - "string"
   * - addressLine2
     - addresses.address2
     - "string"
   * - city
     - addresses.city
     - "string"
   * - country
     - addresses.country
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - addresses.zip
     - "string"


Businesscentral Items to Shopify Product
----------------------------------------
Every Businesscentral Items will be synchronized with a Shopify Product.

Once a link between a Businesscentral Items and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Shopify Product Property
     - Shopify Data Type
   * - displayName
     - variants.title
     - "string"
   * - unitPrice
     - variants.price
     - "string"


Businesscentral Salesorders to Shopify Order
--------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Shopify Order.

Once a link between a Businesscentral Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Shopify Order Property
     - Shopify Data Type
   * - billToAddressLine1
     - billing_address.address1
     - "string"
   * - billToAddressLine1
     - shipping_address.address1
     - "string"
   * - billToAddressLine2
     - billing_address.address2
     - "string"
   * - billToAddressLine2
     - shipping_address.address2
     - "string"
   * - billToCity
     - billing_address.city
     - "string"
   * - billToCity
     - shipping_address.city
     - "string"
   * - billToCountry
     - billing_address.country
     - "string"
   * - billToCountry
     - billing_address.country_code
     - "string"
   * - billToCountry
     - shipping_address.country
     - "string"
   * - billToCountry
     - shipping_address.country_code
     - "string"
   * - billToPostCode
     - billing_address.zip
     - "string"
   * - billToPostCode
     - shipping_address.zip
     - "string"
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer.id
     - "string"
   * - shipToAddressLine1
     - billing_address.address1
     - "string"
   * - shipToAddressLine1
     - shipping_address.address1
     - "string"
   * - shipToAddressLine2
     - billing_address.address2
     - "string"
   * - shipToAddressLine2
     - shipping_address.address2
     - "string"
   * - shipToCity
     - billing_address.city
     - "string"
   * - shipToCity
     - shipping_address.city
     - "string"
   * - shipToCountry
     - billing_address.country
     - "string"
   * - shipToCountry
     - billing_address.country_code
     - "string"
   * - shipToCountry
     - shipping_address.country
     - "string"
   * - shipToCountry
     - shipping_address.country_code
     - "string"
   * - shipToPostCode
     - billing_address.zip
     - "string"
   * - shipToPostCode
     - shipping_address.zip
     - "string"
   * - totalAmountExcludingTax
     - current_total_price
     - "string"
   * - totalAmountExcludingTax
     - total_price
     - "string"

