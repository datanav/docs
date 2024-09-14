==============================
Shopify to Salesforce Dataflow
==============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to Salesforce Product2
--------------------------------------
Every Shopify Product will be synchronized with a Salesforce Product2.

Once a link between a Shopify Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Shopify Inventoryitem to Salesforce Product2
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Salesforce Product2.

Once a link between a Shopify Inventoryitem and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Shopify Order to Salesforce Invoice
-----------------------------------
Every Shopify Order will be synchronized with a Salesforce Invoice.

Once a link between a Shopify Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - current_total_price
     - TotalAmount
     - "string"
   * - total_price
     - TotalAmount
     - "string"


Shopify Customer to Salesforce Currencytype
-------------------------------------------
Every Shopify Customer will be synchronized with a Salesforce Currencytype.

Once a link between a Shopify Customer and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Shopify Customer to Salesforce Customer
---------------------------------------
Every Shopify Customer will be synchronized with a Salesforce Customer.

Once a link between a Shopify Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


Shopify Order to Salesforce Invoiceline
---------------------------------------
Every Shopify Order will be synchronized with a Salesforce Invoiceline.

Once a link between a Shopify Order and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - line_items.price
     - UnitPrice
     - "string"
   * - line_items.quantity
     - Quantity
     - "string"
   * - line_items.title
     - Name
     - "string"


Shopify Order to Salesforce Order
---------------------------------
Every Shopify Order will be synchronized with a Salesforce Order.

Once a link between a Shopify Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - billing_address.address1
     - BillingStreet
     - "string"
   * - billing_address.city
     - BillingCity
     - "string"
   * - billing_address.city
     - ShippingCity
     - "string"
   * - billing_address.country
     - BillingCountry
     - "string"
   * - billing_address.country
     - ShippingCountry
     - "string"
   * - billing_address.country_code
     - BillingCountryCode
     - "string"
   * - billing_address.country_code
     - ShippingCountryCode
     - "string"
   * - billing_address.zip
     - BillingPostalCode
     - "string"
   * - billing_address.zip
     - ShippingStateCode
     - "string"
   * - created_at
     - EffectiveDate
     - "string"
   * - created_at
     - OrderedDate
     - "string"
   * - currency
     - CurrencyIsoCode
     - "string"
   * - current_total_price
     - TotalAmount
     - "string"
   * - customer.id
     - ID
     - "string"
   * - id
     - ID
     - "string"
   * - name
     - Name
     - "string"
   * - shipping_address.address1
     - BillingStreet
     - "string"
   * - shipping_address.city
     - BillingCity
     - "string"
   * - shipping_address.city
     - ShippingCity
     - "string"
   * - shipping_address.country
     - BillingCountry
     - "string"
   * - shipping_address.country
     - ShippingCountry
     - "string"
   * - shipping_address.country_code
     - BillingCountryCode
     - "string"
   * - shipping_address.country_code
     - ShippingCountryCode
     - "string"
   * - shipping_address.zip
     - BillingPostalCode
     - "string"
   * - shipping_address.zip
     - ShippingStateCode
     - "string"
   * - total_price
     - TotalAmount
     - "string"


Shopify Order to Salesforce Orderitem
-------------------------------------
Every Shopify Order will be synchronized with a Salesforce Orderitem.

Once a link between a Shopify Order and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - id
     - OrderId
     - "string"
   * - line_items.price
     - TotalPrice
     - "string"
   * - line_items.product_id
     - Product2Id
     - "string"
   * - line_items.quantity
     - Quantity
     - "string"


Shopify Order to Salesforce Quotelineitem
-----------------------------------------
Every Shopify Order will be synchronized with a Salesforce Quotelineitem.

Once a link between a Shopify Order and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - line_items.price
     - TotalPriceWithTax
     - "string"
   * - line_items.quantity
     - Quantity
     - "string"
   * - line_items.total_discount
     - Discount
     - "string"


Shopify Sesamproduct to Salesforce Product2
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Salesforce Product2.

Once a link between a Shopify Sesamproduct and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - title
     - Name
     - "string"
   * - title
     - Name	
     - "string"
   * - variants.title
     - Description
     - "string"
   * - variants.title
     - Description	
     - "string"

