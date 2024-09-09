==================================
Salesforce to Superoffice Dataflow
==================================

Generated: 2024-09-09 13:31:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Superoffice Quotealternative
------------------------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Salesforce Order if it is connected to a Salesforce Seller, Orderitem, Invoiceline, or Quotelineitem that is synchronized into Superoffice.

Once a link between a Salesforce Order and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - Description
     - Name
     - "string"
   * - TotalAmount
     - TotalPrice
     - "float"


Salesforce Contact to Superoffice Person
----------------------------------------
Every Salesforce Contact will be synchronized with a Superoffice Person.

Once a link between a Salesforce Contact and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - Birthdate
     - BirthDate
     - N/A
   * - Email
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - HomePhone
     - OfficePhones.Value
     - "string"
   * - HomePhone
     - PrivatePhones.Value
     - "string"
   * - LastName
     - Lastname
     - "string"
   * - MobilePhone
     - MobilePhones.Value
     - "string"
   * - Phone
     - OfficePhones.Value
     - "string"


Salesforce Customer to Superoffice Person
-----------------------------------------
Every Salesforce Customer will be synchronized with a Superoffice Person.

Once a link between a Salesforce Customer and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Superoffice Person Property
     - Superoffice Data Type


Salesforce Division to Superoffice Contact
------------------------------------------
Every Salesforce Division will be synchronized with a Superoffice Contact.

Once a link between a Salesforce Division and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Name
     - Name
     - "string"


Salesforce Organization to Superoffice Contact
----------------------------------------------
Every Salesforce Organization will be synchronized with a Superoffice Contact.

Once a link between a Salesforce Organization and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Name
     - Name
     - "string"
   * - Name	
     - Name
     - "string"
   * - Phone	
     - Phones.Value
     - "string"


Salesforce Seller to Superoffice Person
---------------------------------------
Every Salesforce Seller will be synchronized with a Superoffice Person.

Once a link between a Salesforce Seller and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Superoffice Person Property
     - Superoffice Data Type


Salesforce User to Superoffice Person
-------------------------------------
Every Salesforce User will be synchronized with a Superoffice Person.

Once a link between a Salesforce User and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - City
     - Address.Street.City
     - "string"
   * - Country
     - Country.CountryId
     - "integer"
   * - Division
     - Contact.ContactId
     - "integer"
   * - Email
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - ID
     - PersonId
     - "integer"
   * - LastName
     - Lastname
     - "string"
   * - MobilePhone
     - MobilePhones.Value
     - "string"
   * - PostalCode
     - Address.Street.Zipcode
     - "string"
   * - Street
     - Address.Street.Address1
     - "string"


Salesforce Invoiceline to Superoffice Quoteline
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Superoffice Quoteline.

Once a link between a Salesforce Invoiceline and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - Description
     - Description
     - "string"
   * - Name
     - Name
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - TaxRate
     - VAT
     - "integer"
   * - UnitPrice
     - UnitListPrice
     - N/A


Salesforce Orderitem to Superoffice Quoteline
---------------------------------------------
Every Salesforce Orderitem will be synchronized with a Superoffice Quoteline.

Once a link between a Salesforce Orderitem and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - OrderId
     - QuoteAlternativeId
     - "integer"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - UnitListPrice
     - N/A


Salesforce Product2 to Superoffice Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a Superoffice Product.

Once a link between a Salesforce Product2 and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - Description	
     - Description
     - "string"
   * - DisplayUrl	
     - Url
     - "string"
   * - Name	
     - Name
     - "string"


Salesforce Quote to Superoffice Quotealternative
------------------------------------------------
Every Salesforce Quote will be synchronized with a Superoffice Quotealternative.

Once a link between a Salesforce Quote and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"
   * - Tax
     - VAT
     - "integer"
   * - TotalPriceWithTax
     - TotalPrice
     - "float"


Salesforce Quotelineitem to Superoffice Quoteline
-------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Superoffice Quoteline.

Once a link between a Salesforce Quotelineitem and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - Description
     - Description
     - "string"
   * - Discount
     - ERPDiscountPercent
     - "integer"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPriceWithTax
     - UnitListPrice
     - N/A

