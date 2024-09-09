==================================
Woocommerce to Salesforce Dataflow
==================================

Generated: 2024-09-09 08:21:53

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Salesforce Invoice
---------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Invoice.

Once a link between a Woocommerce Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"


Woocommerce Customer to Salesforce Customer
-------------------------------------------
Every Woocommerce Customer will be synchronized with a Salesforce Customer.

Once a link between a Woocommerce Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


Woocommerce Order to Salesforce Currencytype
--------------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Currencytype.

Once a link between a Woocommerce Order and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Woocommerce Order to Salesforce Invoiceline
-------------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Invoiceline.

Once a link between a Woocommerce Order and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
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


Woocommerce Order to Salesforce Order
-------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Order.

Once a link between a Woocommerce Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
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


Woocommerce Order to Salesforce Orderitem
-----------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Orderitem.

Once a link between a Woocommerce Order and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
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


Woocommerce Product to Salesforce Product2
------------------------------------------
Every Woocommerce Product will be synchronized with a Salesforce Product2.

Once a link between a Woocommerce Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"

