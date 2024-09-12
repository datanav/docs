=======================================
Salesforce to Business Central Dataflow
=======================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to Business Central Companies
-------------------------------------------------
Every Salesforce Division will be synchronized with a Business Central Companies.

Once a link between a Salesforce Division and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Business Central Companies Property
     - Business Central Data Type


Salesforce Organization to Business Central Companies
-----------------------------------------------------
Every Salesforce Organization will be synchronized with a Business Central Companies.

Once a link between a Salesforce Organization and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Central Companies Property
     - Business Central Data Type


Salesforce Contact to Business Central Contacts person
------------------------------------------------------
Every Salesforce Contact will be synchronized with a Business Central Contacts person.

Once a link between a Salesforce Contact and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Business Central Contacts person Property
     - Business Central Data Type
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


Salesforce Currencytype to Business Central Currencies
------------------------------------------------------
Every Salesforce Currencytype will be synchronized with a Business Central Currencies.

Once a link between a Salesforce Currencytype and a Business Central Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Business Central Currencies:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Business Central Currencies Property
     - Business Central Data Type


Salesforce Customer to Business Central Customers person
--------------------------------------------------------
Every Salesforce Customer will be synchronized with a Business Central Customers person.

Once a link between a Salesforce Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - Name
     - displayName
     - "string"


Salesforce Invoiceline to Business Central Salesorderlines
----------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Invoiceline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
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


Salesforce Order to Business Central Salesorders
------------------------------------------------
Every Salesforce Order will be synchronized with a Business Central Salesorders.

Once a link between a Salesforce Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Business Central Salesorders Property
     - Business Central Data Type
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


Salesforce Orderitem to Business Central Salesorderlines
--------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Orderitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - OrderId
     - documentId
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - TotalPrice
     - unitPrice
     - "float"


Salesforce Product2 to Business Central Items
---------------------------------------------
Every Salesforce Product2 will be synchronized with a Business Central Items.

Once a link between a Salesforce Product2 and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Business Central Items Property
     - Business Central Data Type
   * - Name
     - displayName
     - "string"
   * - Name	
     - displayName
     - "string"


Salesforce Quotelineitem to Business Central Salesorderlines
------------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - Discount
     - discountPercent
     - N/A
   * - Quantity
     - quantity
     - N/A
   * - TotalPriceWithTax
     - unitPrice
     - "float"


Salesforce User to Business Central Employees
---------------------------------------------
Every Salesforce User will be synchronized with a Business Central Employees.

Once a link between a Salesforce User and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Business Central Employees Property
     - Business Central Data Type
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

