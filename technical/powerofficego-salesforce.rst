====================================
PowerOfficeGO to Salesforce Dataflow
====================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Customers to Salesforce Division
----------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a Salesforce Division.

Once a link between a PowerOfficeGO Customers and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


PowerOfficeGO Departments to Salesforce Division
------------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a Salesforce Division.

Once a link between a PowerOfficeGO Departments and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - IsActive
     - IsActive
     - "string"
   * - Name
     - Name
     - "string"


PowerOfficeGO Projectactivity to Salesforce Task
------------------------------------------------
Every PowerOfficeGO Projectactivity will be synchronized with a Salesforce Task.

Once a link between a PowerOfficeGO Projectactivity and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projectactivity and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projectactivity Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - name
     - Subject
     - "string"


PowerOfficeGO Projects to Salesforce Task
-----------------------------------------
Every PowerOfficeGO Projects will be synchronized with a Salesforce Task.

Once a link between a PowerOfficeGO Projects and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projects and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projects Property
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


PowerOfficeGO Salesorderlines to Salesforce Invoice
---------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a PowerOfficeGO Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalAmount
     - "string"


PowerOfficeGO Salesorders to Salesforce Invoice
-----------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a PowerOfficeGO Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
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


PowerOfficeGO Contactperson to Salesforce Contact
-------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a Salesforce Contact.

Once a link between a PowerOfficeGO Contactperson and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
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


PowerOfficeGO Currency to Salesforce Currencytype
-------------------------------------------------
Every PowerOfficeGO Currency will be synchronized with a Salesforce Currencytype.

Once a link between a PowerOfficeGO Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


PowerOfficeGO Customers person to Salesforce Customer
-----------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a Salesforce Customer.

Once a link between a PowerOfficeGO Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type


PowerOfficeGO Employees to Salesforce User
------------------------------------------
Every PowerOfficeGO Employees will be synchronized with a Salesforce User.

Once a link between a PowerOfficeGO Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - Salesforce User Property
     - Salesforce Data Type
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - JobTitle
     - Title
     - "string"
   * - LastName
     - LastName
     - "string"
   * - Number
     - EmployeeNumber
     - "string"
   * - PhoneNumber
     - MobilePhone
     - "string"


PowerOfficeGOPowerofficego Product to Salesforce Product2
---------------------------------------------------------
Every PowerOfficeGOPowerofficego Product will be synchronized with a Salesforce Product2.

Once a link between a PowerOfficeGOPowerofficego Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficego Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficego Product Property
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


PowerOfficeGO Quote to Salesforce Quote
---------------------------------------
Every PowerOfficeGO Quote will be synchronized with a Salesforce Quote.

Once a link between a PowerOfficeGO Quote and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Quote and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Quote Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalPriceWithTax
     - "string"


PowerOfficeGO Salesorderlines to Salesforce Invoiceline
-------------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a PowerOfficeGO Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
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


PowerOfficeGO Salesorderlines to Salesforce Orderitem
-----------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a PowerOfficeGO Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
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


PowerOfficeGO Salesorderlines to Salesforce Quotelineitem
---------------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a PowerOfficeGO Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
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


PowerOfficeGOPowerofficego Salesorders to Salesforce Order
----------------------------------------------------------
Every PowerOfficeGOPowerofficego Salesorders will be synchronized with a Salesforce Order.

Once a link between a PowerOfficeGOPowerofficego Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficego Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficego Salesorders Property
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


PowerOfficeGO Suppliers person to Salesforce Contact
----------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a Salesforce Contact.

Once a link between a PowerOfficeGO Suppliers person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
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

