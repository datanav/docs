======================================
Salesforce to Businesscentral Dataflow
======================================

Generated: 2024-09-10 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to Businesscentral Companies
------------------------------------------------
Every Salesforce Division will be synchronized with a Businesscentral Companies.

Once a link between a Salesforce Division and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Salesforce Organization to Businesscentral Companies
----------------------------------------------------
Every Salesforce Organization will be synchronized with a Businesscentral Companies.

Once a link between a Salesforce Organization and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Salesforce Contact to Businesscentral Contacts person
-----------------------------------------------------
Every Salesforce Contact will be synchronized with a Businesscentral Contacts person.

Once a link between a Salesforce Contact and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - Email
     - email
     - "string"
   * - HomePhone
     - phoneNumber
     - "string"
   * - MobilePhone
     - mobilePhoneNumber
     - "string"
   * - Phone
     - phoneNumber
     - "string"


Salesforce Customer to Businesscentral Customers person
-------------------------------------------------------
Every Salesforce Customer will be synchronized with a Businesscentral Customers person.

Once a link between a Salesforce Customer and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
   * - Name
     - displayName
     - "string"


Salesforce Invoiceline to Businesscentral Salesorderlines
---------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Salesforce Invoiceline and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - Name
     - description
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - TaxRate
     - taxPercent
     - N/A
   * - UnitPrice
     - unitPrice
     - "float"


Salesforce Order to Businesscentral Salesorders
-----------------------------------------------
Every Salesforce Order will be synchronized with a Businesscentral Salesorders.

Once a link between a Salesforce Order and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
   * - BillingCity
     - billToCity
     - "string"
   * - BillingCity
     - shipToCity
     - "string"
   * - BillingCountry
     - billToCountry
     - "string"
   * - BillingCountry
     - shipToCountry
     - "string"
   * - BillingPostalCode
     - billToPostCode
     - "string"
   * - BillingPostalCode
     - shipToPostCode
     - "string"
   * - BillingStreet
     - billToAddressLine1
     - "string"
   * - BillingStreet
     - shipToAddressLine1
     - "string"
   * - CurrencyIsoCode
     - currencyId
     - "string"
   * - EffectiveDate
     - orderDate
     - N/A
   * - EffectiveDate
     - requestedDeliveryDate
     - N/A
   * - EndDate
     - requestedDeliveryDate
     - N/A
   * - ID
     - id
     - "string"
   * - OrderedDate
     - orderDate
     - N/A
   * - ShippingCity
     - billToCity
     - "string"
   * - ShippingCity
     - shipToCity
     - "string"
   * - ShippingCountry
     - billToCountry
     - "string"
   * - ShippingCountry
     - shipToCountry
     - "string"
   * - ShippingStateCode
     - billToPostCode
     - "string"
   * - ShippingStateCode
     - shipToPostCode
     - "string"


Salesforce Orderitem to Businesscentral Salesorderlines
-------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Salesforce Orderitem and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - OrderId
     - documentId
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - TotalPrice
     - unitPrice
     - "float"


Salesforce Product2 to Businesscentral Items
--------------------------------------------
Every Salesforce Product2 will be synchronized with a Businesscentral Items.

Once a link between a Salesforce Product2 and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - Name
     - displayName
     - "string"
   * - Name	
     - displayName
     - "string"


Salesforce Quotelineitem to Businesscentral Salesorderlines
-----------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - Discount
     - discountPercent
     - N/A
   * - Quantity
     - quantity
     - N/A
   * - TotalPriceWithTax
     - unitPrice
     - "float"

