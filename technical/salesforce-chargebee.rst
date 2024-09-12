================================
Salesforce to Chargebee Dataflow
================================

Generated: 2024-09-12 00:00:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Chargebee Customer
----------------------------------------
Every Salesforce Contact will be synchronized with a Chargebee Customer.

Once a link between a Salesforce Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Email
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MailingCountry
     - billing_address.country
     - "string"


Salesforce Currencytype to Chargebee Currency
---------------------------------------------
Every Salesforce Currencytype will be synchronized with a Chargebee Currency.

Once a link between a Salesforce Currencytype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Chargebee Currency Property
     - Chargebee Data Type


Salesforce Division to Chargebee Business_entity
------------------------------------------------
Every Salesforce Division will be synchronized with a Chargebee Business_entity.

Once a link between a Salesforce Division and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


Salesforce Invoice to Chargebee Order
-------------------------------------
Every Salesforce Invoice will be synchronized with a Chargebee Order.

Once a link between a Salesforce Invoice and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"


Salesforce Invoiceline to Chargebee Order
-----------------------------------------
Every Salesforce Invoiceline will be synchronized with a Chargebee Order.

Once a link between a Salesforce Invoiceline and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"
   * - Description
     - order_line_items.description
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - TaxRate
     - order_line_items.tax_amount
     - "string"
   * - UnitPrice
     - order_line_items.unit_price
     - "string"


Salesforce Orderitem to Chargebee Order
---------------------------------------
Every Salesforce Orderitem will be synchronized with a Chargebee Order.

Once a link between a Salesforce Orderitem and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - TotalPrice
     - order_line_items.unit_price
     - "string"


Salesforce Quote to Chargebee Order
-----------------------------------
Every Salesforce Quote will be synchronized with a Chargebee Order.

Once a link between a Salesforce Quote and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"


Salesforce Quotelineitem to Chargebee Order
-------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Chargebee Order.

Once a link between a Salesforce Quotelineitem and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"
   * - Description
     - order_line_items.description
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - TotalPriceWithTax
     - order_line_items.unit_price
     - "string"


Salesforce Seller to Chargebee Customer
---------------------------------------
Every Salesforce Seller will be synchronized with a Chargebee Customer.

Once a link between a Salesforce Seller and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Chargebee Customer Property
     - Chargebee Data Type


Salesforce User to Chargebee Customer
-------------------------------------
Every Salesforce User will be synchronized with a Chargebee Customer.

Once a link between a Salesforce User and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Country
     - billing_address.country
     - "string"
   * - Email
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Salesforce Customer to Chargebee Customer
-----------------------------------------
Every Salesforce Customer will be synchronized with a Chargebee Customer.

Once a link between a Salesforce Customer and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Chargebee Customer Property
     - Chargebee Data Type


Salesforce Order to Chargebee Order
-----------------------------------
Every Salesforce Order will be synchronized with a Chargebee Order.

Once a link between a Salesforce Order and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyIsoCode
     - currency_code
     - "string"


Salesforce Organization to Chargebee Business_entity
----------------------------------------------------
Every Salesforce Organization will be synchronized with a Chargebee Business_entity.

Once a link between a Salesforce Organization and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Product2 to Chargebee Item
-------------------------------------
Every Salesforce Product2 will be synchronized with a Chargebee Item.

Once a link between a Salesforce Product2 and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - Name	
     - name
     - "string"

