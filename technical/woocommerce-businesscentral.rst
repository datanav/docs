=======================================
WooCommerce to BusinessCentral Dataflow
=======================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to BusinessCentral Customers person
--------------------------------------------------------
Every WooCommerce Customer will be synchronized with a BusinessCentral Customers person.

Once a link between a WooCommerce Customer and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
   * - email
     - email
     - "string"


WooCommerce Order to BusinessCentral Salesorderlines
----------------------------------------------------
Every WooCommerce Order will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a WooCommerce Order and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


WooCommerce Order to BusinessCentral Salesorders
------------------------------------------------
Every WooCommerce Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a WooCommerce Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


WooCommerce Product to BusinessCentral Items
--------------------------------------------
Every WooCommerce Product will be synchronized with a BusinessCentral Items.

Once a link between a WooCommerce Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - name
     - displayName
     - "string"
   * - price
     - unitCost
     - N/A
   * - sale_price
     - unitPrice
     - N/A

