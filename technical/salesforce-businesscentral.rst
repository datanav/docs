======================================
Salesforce to BusinessCentral Dataflow
======================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to Business Companies
-----------------------------------------
Every Salesforce Division will be synchronized with a Business Companies.

Once a link between a Salesforce Division and a Business Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Business Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Business Companies Property
     - Business Data Type


Salesforce Organization to Business Companies
---------------------------------------------
Every Salesforce Organization will be synchronized with a Business Companies.

Once a link between a Salesforce Organization and a Business Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Companies Property
     - Business Data Type


Salesforce Contact to BusinessCentral Contacts person
-----------------------------------------------------
Every Salesforce Contact will be synchronized with a BusinessCentral Contacts person.

Once a link between a Salesforce Contact and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


Salesforce Customer to BusinessCentral Customers person
-------------------------------------------------------
Every Salesforce Customer will be synchronized with a BusinessCentral Customers person.

Once a link between a Salesforce Customer and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
   * - Name
     - displayName
     - "string"


Salesforce Invoiceline to BusinessCentral Salesorderlines
---------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Salesforce Invoiceline and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


Salesforce Order to BusinessCentral Salesorders
-----------------------------------------------
Every Salesforce Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a Salesforce Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


Salesforce Orderitem to BusinessCentral Salesorderlines
-------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Salesforce Orderitem and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
   * - OrderId
     - documentId
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - TotalPrice
     - unitPrice
     - "float"


Salesforce Product2 to BusinessCentral Items
--------------------------------------------
Every Salesforce Product2 will be synchronized with a BusinessCentral Items.

Once a link between a Salesforce Product2 and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - Name
     - displayName
     - "string"
   * - Name	
     - displayName
     - "string"


Salesforce Quotelineitem to BusinessCentral Salesorderlines
-----------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Salesforce Quotelineitem and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
   * - Discount
     - discountPercent
     - N/A
   * - Quantity
     - quantity
     - N/A
   * - TotalPriceWithTax
     - unitPrice
     - "float"


Salesforce User to BusinessCentral Employees
--------------------------------------------
Every Salesforce User will be synchronized with a BusinessCentral Employees.

Once a link between a Salesforce User and a BusinessCentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a BusinessCentral Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - BusinessCentral Employees Property
     - BusinessCentral Data Type
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

