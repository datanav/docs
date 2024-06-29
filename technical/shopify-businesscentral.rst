===================================
Shopify to Businesscentral Dataflow
===================================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Businesscentral Customers person
----------------------------------------------------
Every Shopify Customer will be synchronized with a Businesscentral Customers person.

Once a link between a Shopify Customer and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phone
     - phoneNumber
     - "string"


Shopify Order to Businesscentral Salesorders
--------------------------------------------
Every Shopify Order will be synchronized with a Businesscentral Salesorders.

Once a link between a Shopify Order and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
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


Shopify Product to Businesscentral Items
----------------------------------------
Every Shopify Product will be synchronized with a Businesscentral Items.

Once a link between a Shopify Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - variants.price
     - unitPrice
     - N/A
   * - variants.title
     - displayName
     - "string"

