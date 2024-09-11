======================================
BusinessCentral to Salesforce Dataflow
======================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Salesforce Division
------------------------------------------------
Every Businesscentral Companies will be synchronized with a Salesforce Division.

Once a link between a Businesscentral Companies and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Salesforce Division Property
     - Salesforce Data Type


Businesscentral Customers company to Salesforce Division
--------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Salesforce Division.

Once a link between a Businesscentral Customers company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"


Businesscentral Salesorderlines to Salesforce Invoice
-----------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a Businesscentral Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Businesscentral Salesorders to Salesforce Invoice
-------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a Businesscentral Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currencyId
     - CurrencyIsoCode
     - "string"
   * - requestedDeliveryDate
     - FullSettlementDate
     - "string"
   * - totalAmountExcludingTax
     - TotalAmount
     - "string"


Businesscentral Salesquotes to Salesforce Invoice
-------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Salesforce Invoice.

Once a link between a Businesscentral Salesquotes and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Salesforce Invoice Property
     - Salesforce Data Type


BusinessCentral Contacts person to Salesforce Contact
-----------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a Salesforce Contact.

Once a link between a BusinessCentral Contacts person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - city
     - MailingCity
     - "string"
   * - email
     - Email
     - "string"
   * - id
     - Id
     - "string"
   * - mobilePhoneNumber
     - MobilePhone
     - "string"
   * - phoneNumber
     - HomePhone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - postalCode
     - MailingPostalCode
     - "string"


BusinessCentral Currencies to Salesforce Currencytype
-----------------------------------------------------
Every BusinessCentral Currencies will be synchronized with a Salesforce Currencytype.

Once a link between a BusinessCentral Currencies and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Currencies and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Currencies Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - code
     - IsoCode
     - "string"


BusinessCentral Customers company to Salesforce Organization
------------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Salesforce Organization.

Once a link between a BusinessCentral Customers company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - Name
     - "string"
   * - displayName
     - Name	
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - phoneNumber
     - Phone	
     - "string"
   * - postalCode
     - PostalCode	
     - "string"


BusinessCentral Customers person to Salesforce Customer
-------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Salesforce Customer.

Once a link between a BusinessCentral Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"


BusinessCentral Employees to Salesforce User
--------------------------------------------
Every BusinessCentral Employees will be synchronized with a Salesforce User.

Once a link between a BusinessCentral Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - Salesforce User Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"
   * - givenName
     - FirstName
     - "string"
   * - jobTitle
     - Title
     - "string"
   * - mobilePhone
     - MobilePhone
     - "string"
   * - personalEmail
     - Email
     - "string"
   * - surname
     - LastName
     - "string"


BusinessCentral Items to Salesforce Product2
--------------------------------------------
Every BusinessCentral Items will be synchronized with a Salesforce Product2.

Once a link between a BusinessCentral Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"
   * - displayName
     - Name	
     - "string"


BusinessCentral Salesorderlines to Salesforce Invoiceline
---------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a BusinessCentral Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - description
     - Name
     - "string"
   * - quantity
     - Quantity
     - "string"
   * - taxPercent
     - TaxRate
     - "string"
   * - unitPrice
     - UnitPrice
     - "string"


BusinessCentral Salesorderlines to Salesforce Orderitem
-------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a BusinessCentral Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - documentId
     - OrderId
     - "string"
   * - quantity
     - Quantity
     - "string"
   * - unitPrice
     - TotalPrice
     - "string"


BusinessCentral Salesorderlines to Salesforce Quotelineitem
-----------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a BusinessCentral Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - discountPercent
     - Discount
     - "string"
   * - quantity
     - Quantity
     - "string"
   * - unitPrice
     - TotalPriceWithTax
     - "string"


BusinessCentral Salesorders to Salesforce Order
-----------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a Salesforce Order.

Once a link between a BusinessCentral Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - billToAddressLine1
     - BillingStreet
     - "string"
   * - billToCity
     - BillingCity
     - "string"
   * - billToCity
     - ShippingCity
     - "string"
   * - billToCountry
     - BillingCountry
     - "string"
   * - billToCountry
     - BillingCountryCode
     - "string"
   * - billToCountry
     - ShippingCountry
     - "string"
   * - billToCountry
     - ShippingCountryCode
     - "string"
   * - billToPostCode
     - BillingPostalCode
     - "string"
   * - billToPostCode
     - ShippingStateCode
     - "string"
   * - currencyId
     - CurrencyIsoCode
     - "string"
   * - id
     - ID
     - "string"
   * - orderDate
     - EffectiveDate
     - "string"
   * - orderDate
     - OrderedDate
     - "string"
   * - requestedDeliveryDate
     - EffectiveDate
     - "string"
   * - requestedDeliveryDate
     - EndDate
     - "string"
   * - shipToAddressLine1
     - BillingStreet
     - "string"
   * - shipToCity
     - BillingCity
     - "string"
   * - shipToCity
     - ShippingCity
     - "string"
   * - shipToCountry
     - BillingCountry
     - "string"
   * - shipToCountry
     - BillingCountryCode
     - "string"
   * - shipToCountry
     - ShippingCountry
     - "string"
   * - shipToCountry
     - ShippingCountryCode
     - "string"
   * - shipToPostCode
     - BillingPostalCode
     - "string"
   * - shipToPostCode
     - ShippingStateCode
     - "string"
   * - totalAmountExcludingTax
     - TotalAmount
     - "string"

