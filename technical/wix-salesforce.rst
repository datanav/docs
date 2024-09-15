==============================
Wix.com to Salesforce Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Salesforce Contact
--------------------------------------
Every Wix.com Contacts will be synchronized with a Salesforce Contact.

Once a link between a Wix.com Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - Email
     - "string"
   * - primaryInfo.phone
     - HomePhone
     - "string"
   * - primaryInfo.phone
     - Phone
     - "string"


Wix.com Currencies to Salesforce Currencytype
---------------------------------------------
Every Wix.com Currencies will be synchronized with a Salesforce Currencytype.

Once a link between a Wix.com Currencies and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Wix.com Orders to Salesforce Invoiceline
----------------------------------------
Every Wix.com Orders will be synchronized with a Salesforce Invoiceline.

Once a link between a Wix.com Orders and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - lineItems.name
     - Name
     - "string"
   * - lineItems.price
     - UnitPrice
     - "string"
   * - lineItems.quantity
     - Quantity
     - "string"


Wix.com Orders to Salesforce Order
----------------------------------
Every Wix.com Orders will be synchronized with a Salesforce Order.

Once a link between a Wix.com Orders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - billingInfo.paidDate
     - EndDate
     - "string"
   * - currency
     - CurrencyIsoCode
     - "string"
   * - totals.total
     - TotalAmount
     - "string"


Wix.com Orders to Salesforce Orderitem
--------------------------------------
Every Wix.com Orders will be synchronized with a Salesforce Orderitem.

Once a link between a Wix.com Orders and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - id
     - OrderId
     - "string"
   * - lineItems.price
     - TotalPrice
     - "string"
   * - lineItems.quantity
     - Quantity
     - "string"


Wix.com Orders to Salesforce Quotelineitem
------------------------------------------
Every Wix.com Orders will be synchronized with a Salesforce Quotelineitem.

Once a link between a Wix.com Orders and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - lineItems.price
     - TotalPriceWithTax
     - "string"
   * - lineItems.quantity
     - Quantity
     - "string"


Wix.com Products to Salesforce Product2
---------------------------------------
Every Wix.com Products will be synchronized with a Salesforce Product2.

Once a link between a Wix.com Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"

