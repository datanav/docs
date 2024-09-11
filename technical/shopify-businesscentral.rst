===================================
Shopify to BusinessCentral Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Business Customers company
----------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Business Customers company must be established.

A new Business Customers company will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Business.

Once a link between a Shopify Customer and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Customers company Property
     - Business Data Type


Shopify Product to Business Items
---------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Business Items must be established.

A new Business Items will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into Business.

Once a link between a Shopify Product and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Business Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Business Items Property
     - Business Data Type


Shopify Customer to BusinessCentral Customers person
----------------------------------------------------
Every Shopify Customer will be synchronized with a BusinessCentral Customers person.

Once a link between a Shopify Customer and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


Shopify Order to BusinessCentral Salesorderlines
------------------------------------------------
Every Shopify Order will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Shopify Order and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


Shopify Order to BusinessCentral Salesorders
--------------------------------------------
Every Shopify Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a Shopify Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


Shopify Sesamproduct to BusinessCentral Items
---------------------------------------------
Every Shopify Sesamproduct will be synchronized with a BusinessCentral Items.

Once a link between a Shopify Sesamproduct and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - sesam_priceExclVAT
     - unitPrice
     - N/A
   * - title
     - displayName
     - "string"
   * - variants.price
     - unitPrice
     - N/A

