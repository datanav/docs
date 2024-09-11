=======================================
Salesforce to Business Central Dataflow
=======================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Salesforce Contact to Business Contacts person
----------------------------------------------
Every Salesforce Contact will be synchronized with a Business Contacts person.

Once a link between a Salesforce Contact and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Business Contacts person Property
     - Business Data Type
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


Salesforce Customer to Business Customers person
------------------------------------------------
Every Salesforce Customer will be synchronized with a Business Customers person.

Once a link between a Salesforce Customer and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Business Customers person Property
     - Business Data Type
   * - Name
     - displayName
     - "string"


Salesforce Invoiceline to Business Salesorderlines
--------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Business Salesorderlines.

Once a link between a Salesforce Invoiceline and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Business Salesorderlines Property
     - Business Data Type
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


Salesforce Order to Business Salesorders
----------------------------------------
Every Salesforce Order will be synchronized with a Business Salesorders.

Once a link between a Salesforce Order and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Business Salesorders Property
     - Business Data Type
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


Salesforce Orderitem to Business Salesorderlines
------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Business Salesorderlines.

Once a link between a Salesforce Orderitem and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Business Salesorderlines Property
     - Business Data Type
   * - OrderId
     - documentId
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - TotalPrice
     - unitPrice
     - "float"


Salesforce Product2 to Business Items
-------------------------------------
Every Salesforce Product2 will be synchronized with a Business Items.

Once a link between a Salesforce Product2 and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Business Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Business Items Property
     - Business Data Type
   * - Name
     - displayName
     - "string"
   * - Name	
     - displayName
     - "string"


Salesforce Quotelineitem to Business Salesorderlines
----------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Business Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Business Salesorderlines Property
     - Business Data Type
   * - Discount
     - discountPercent
     - N/A
   * - Quantity
     - quantity
     - N/A
   * - TotalPriceWithTax
     - unitPrice
     - "float"


Salesforce User to Business Employees
-------------------------------------
Every Salesforce User will be synchronized with a Business Employees.

Once a link between a Salesforce User and a Business Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Business Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Business Employees Property
     - Business Data Type
   * - City
     - city
     - "string"
   * - Country
     - country
     - "string"
   * - Email
     - personalEmail
     - "string"
   * - FirstName
     - givenName
     - "string"
   * - ID
     - id
     - "string"
   * - LastName
     - surname
     - "string"
   * - MobilePhone
     - mobilePhone
     - "string"
   * - Name
     - displayName
     - "string"
   * - PostalCode
     - postalCode
     - "string"
   * - Street
     - addressLine1
     - "string"
   * - Title
     - jobTitle
     - "string"

