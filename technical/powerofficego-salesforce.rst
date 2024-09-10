====================================
Powerofficego to Salesforce Dataflow
====================================

Generated: 2024-09-10 07:19:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Salesforce Division
----------------------------------------------
Every Powerofficego Customers will be synchronized with a Salesforce Division.

Once a link between a Powerofficego Customers and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


Powerofficego Departments to Salesforce Division
------------------------------------------------
Every Powerofficego Departments will be synchronized with a Salesforce Division.

Once a link between a Powerofficego Departments and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - IsActive
     - IsActive
     - "string"
   * - Name
     - Name
     - "string"


Powerofficego Projects to Salesforce Task
-----------------------------------------
Every Powerofficego Projects will be synchronized with a Salesforce Task.

Once a link between a Powerofficego Projects and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - IsActive
     - IsClosed
     - "string"
   * - Name
     - Subject
     - "string"
   * - ProjectManagerEmployeeId
     - OwnerId
     - "string"


Powerofficego Salesorderlines to Salesforce Invoice
---------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a Powerofficego Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalAmount
     - "string"


Powerofficego Salesorders to Salesforce Invoice
-----------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a Powerofficego Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyCode
     - CurrencyIsoCode
     - "string"
   * - NetAmount
     - TotalAmount
     - "string"
   * - RelatedInvoiceNo
     - InvoiceNumber
     - "string"


Powerofficego Contactperson to Salesforce Contact
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Contactperson and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - city
     - MailingCity
     - "string"
   * - dateOfBirth
     - Birthdate
     - "string"
   * - emailAddress
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumber
     - HomePhone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - zipCode
     - MailingPostalCode
     - "string"


Powerofficego Currency to Salesforce Currencytype
-------------------------------------------------
Every Powerofficego Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Powerofficego Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Powerofficego Customers person to Salesforce Customer
-----------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Salesforce Customer.

Once a link between a Powerofficego Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type


Powerofficego Employees to Salesforce User
------------------------------------------
Every Powerofficego Employees will be synchronized with a Salesforce User.

Once a link between a Powerofficego Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Salesforce User Property
     - Salesforce Data Type


Powerofficego Product to Salesforce Product2
--------------------------------------------
Every Powerofficego Product will be synchronized with a Salesforce Product2.

Once a link between a Powerofficego Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description
     - "string"
   * - description
     - Description	
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"


Powerofficego Quote to Salesforce Quote
---------------------------------------
Every Powerofficego Quote will be synchronized with a Salesforce Quote.

Once a link between a Powerofficego Quote and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalPriceWithTax
     - "string"


Powerofficego Salesorderlines to Salesforce Invoiceline
-------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a Powerofficego Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - Description
     - Name
     - "string"
   * - ProductUnitPrice
     - UnitPrice
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - VatRate
     - TaxRate
     - "string"


Powerofficego Salesorderlines to Salesforce Orderitem
-----------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a Powerofficego Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - ProductUnitPrice
     - TotalPrice
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - sesam_SalesOrderId
     - OrderId
     - "string"


Powerofficego Salesorderlines to Salesforce Quotelineitem
---------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a Powerofficego Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - Allowance
     - Discount
     - "string"
   * - ProductUnitPrice
     - TotalPriceWithTax
     - "string"
   * - Quantity
     - Quantity
     - "string"


Powerofficego Salesorders to Salesforce Order
---------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Salesforce Order.

Once a link between a Powerofficego Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - CurrencyCode
     - CurrencyIsoCode
     - "string"
   * - NetAmount
     - TotalAmount
     - "string"
   * - SalesOrderDate
     - EffectiveDate
     - "string"
   * - SalesOrderDate
     - OrderedDate
     - "string"


Powerofficego Suppliers person to Salesforce Contact
----------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Suppliers person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - DateOfBirth
     - Birthdate
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - MailingCity
     - "string"
   * - MailAddress.CountryCode
     - MailingCountryCode
     - "string"
   * - MailAddress.ZipCode
     - MailingPostalCode
     - "string"
   * - PhoneNumber
     - HomePhone
     - "string"
   * - PhoneNumber
     - Phone
     - "string"

