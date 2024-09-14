==================================
Salesforce to SuperOffice Dataflow
==================================

Generated: 2024-09-14 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Superoffice Quotealternative
------------------------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Salesforce Order if it is connected to a Salesforce Order, Seller, Orderitem, Invoiceline, or Quotelineitem that is synchronized into Superoffice.

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


Salesforce Contact to SuperOffice Person
----------------------------------------
Every Salesforce Contact will be synchronized with a SuperOffice Person.

Once a link between a Salesforce Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


Salesforce Customer to SuperOffice Person
-----------------------------------------
Every Salesforce Customer will be synchronized with a SuperOffice Person.

Once a link between a Salesforce Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - SuperOffice Person Property
     - SuperOffice Data Type


Salesforce Division to SuperOffice Contact
------------------------------------------
Every Salesforce Division will be synchronized with a SuperOffice Contact.

Once a link between a Salesforce Division and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


Salesforce Organization to SuperOffice Contact
----------------------------------------------
Every Salesforce Organization will be synchronized with a SuperOffice Contact.

Once a link between a Salesforce Organization and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"
   * - Name	
     - Name
     - "string"
   * - Phone
     - Phones.Value
     - "string"
   * - Phone	
     - Phones.Value
     - "string"


Salesforce Seller to SuperOffice Person
---------------------------------------
Every Salesforce Seller will be synchronized with a SuperOffice Person.

Once a link between a Salesforce Seller and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - SuperOffice Person Property
     - SuperOffice Data Type


Salesforce User to SuperOffice Person
-------------------------------------
Every Salesforce User will be synchronized with a SuperOffice Person.

Once a link between a Salesforce User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


Salesforce Invoiceline to SuperOffice Quoteline
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Invoiceline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
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


Salesforce Orderitem to SuperOffice Quoteline
---------------------------------------------
Every Salesforce Orderitem will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Orderitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - OrderId
     - QuoteAlternativeId
     - "integer"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - UnitListPrice
     - N/A


Salesforce Product2 to SuperOffice Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a SuperOffice Product.

Once a link between a Salesforce Product2 and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - Description
     - Description
     - "string"
   * - Description	
     - Description
     - "string"
   * - DisplayUrl
     - Url
     - "string"
   * - DisplayUrl	
     - Url
     - "string"
   * - Name
     - Name
     - "string"
   * - Name	
     - Name
     - "string"


Salesforce Quote to SuperOffice Quotealternative
------------------------------------------------
Every Salesforce Quote will be synchronized with a SuperOffice Quotealternative.

Once a link between a Salesforce Quote and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
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


Salesforce Quotelineitem to SuperOffice Quoteline
-------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Quotelineitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
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

