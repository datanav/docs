=======================================
Business Central to Salesforce Dataflow
=======================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to Salesforce Division
-------------------------------------------------
Every Business Central Companies will be synchronized with a Salesforce Division.

Once a link between a Business Central Companies and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Salesforce Division Property
     - Salesforce Data Type


Business Central Customers company to Salesforce Division
---------------------------------------------------------
Every Business Central Customers company will be synchronized with a Salesforce Division.

Once a link between a Business Central Customers company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"


Business Central Salesorderlines to Salesforce Invoice
------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a Business Central Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Business Central Salesorders to Salesforce Invoice
--------------------------------------------------
Every Business Central Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a Business Central Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
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


Business Central Salesquotes to Salesforce Invoice
--------------------------------------------------
Every Business Central Salesquotes will be synchronized with a Salesforce Invoice.

Once a link between a Business Central Salesquotes and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Business Central Contacts person to Salesforce Contact
------------------------------------------------------
Every Business Central Contacts person will be synchronized with a Salesforce Contact.

Once a link between a Business Central Contacts person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
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


Business Central Currencies to Salesforce Currencytype
------------------------------------------------------
Every Business Central Currencies will be synchronized with a Salesforce Currencytype.

Once a link between a Business Central Currencies and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - code
     - IsoCode
     - "string"


Business Central Customers company to Salesforce Organization
-------------------------------------------------------------
Every Business Central Customers company will be synchronized with a Salesforce Organization.

Once a link between a Business Central Customers company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
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


Business Central Customers person to Salesforce Customer
--------------------------------------------------------
Every Business Central Customers person will be synchronized with a Salesforce Customer.

Once a link between a Business Central Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"


Business Central Employees to Salesforce User
---------------------------------------------
Every Business Central Employees will be synchronized with a Salesforce User.

Once a link between a Business Central Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
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


Business Central Items to Salesforce Product2
---------------------------------------------
Every Business Central Items will be synchronized with a Salesforce Product2.

Once a link between a Business Central Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - displayName
     - Name
     - "string"
   * - displayName
     - Name	
     - "string"


Business Central Salesorderlines to Salesforce Invoiceline
----------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a Business Central Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
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


Business Central Salesorderlines to Salesforce Orderitem
--------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a Business Central Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
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


Business Central Salesorderlines to Salesforce Quotelineitem
------------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a Business Central Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
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


Business Central Salesorders to Salesforce Order
------------------------------------------------
Every Business Central Salesorders will be synchronized with a Salesforce Order.

Once a link between a Business Central Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
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

