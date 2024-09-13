==================================
WooCommerce to Salesforce Dataflow
==================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Salesforce Invoice
---------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Invoice.

Once a link between a WooCommerce Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"


WooCommerce Customer to Salesforce Customer
-------------------------------------------
Every WooCommerce Customer will be synchronized with a Salesforce Customer.

Once a link between a WooCommerce Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


WooCommerce Order to Salesforce Currencytype
--------------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Currencytype.

Once a link between a WooCommerce Order and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


WooCommerce Order to Salesforce Invoiceline
-------------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Invoiceline.

Once a link between a WooCommerce Order and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - line_items.name
     - Name
     - "string"
   * - line_items.price
     - UnitPrice
     - "string"
   * - line_items.quantity
     - Quantity
     - "string"
   * - line_items.sku
     - Description
     - "string"


WooCommerce Order to Salesforce Order
-------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Order.

Once a link between a WooCommerce Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - billing.address_1
     - BillingStreet
     - "string"
   * - billing.city
     - BillingCity
     - "string"
   * - billing.city
     - ShippingCity
     - "string"
   * - billing.country
     - BillingCountry
     - "string"
   * - billing.country
     - ShippingCountry
     - "string"
   * - billing.postcode
     - BillingPostalCode
     - "string"
   * - billing.postcode
     - ShippingStateCode
     - "string"
   * - currency
     - CurrencyIsoCode
     - "string"
   * - id
     - ID
     - "string"
   * - shipping.address_1
     - BillingStreet
     - "string"
   * - shipping.city
     - BillingCity
     - "string"
   * - shipping.city
     - ShippingCity
     - "string"
   * - shipping.country
     - BillingCountry
     - "string"
   * - shipping.country
     - ShippingCountry
     - "string"
   * - shipping.postcode
     - BillingPostalCode
     - "string"
   * - shipping.postcode
     - ShippingStateCode
     - "string"


WooCommerce Order to Salesforce Orderitem
-----------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Orderitem.

Once a link between a WooCommerce Order and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
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
   * - line_items.sku
     - Quantity
     - "string"
   * - line_items.sku
     - UnitPrice
     - "string"


WooCommerce Order to Salesforce Quotelineitem
---------------------------------------------
Every WooCommerce Order will be synchronized with a Salesforce Quotelineitem.

Once a link between a WooCommerce Order and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
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


WooCommerce Product to Salesforce Product2
------------------------------------------
Every WooCommerce Product will be synchronized with a Salesforce Product2.

Once a link between a WooCommerce Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"
   * - status
     - ProductCode
     - "string"

