=====================================
PowerOffice GO to Salesforce Dataflow
=====================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Salesforce Division
-----------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Salesforce Division.

Once a link between a PowerOffice GO Customers and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


PowerOffice GO Departments to Salesforce Division
-------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Salesforce Division.

Once a link between a PowerOffice GO Departments and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - IsActive
     - IsActive
     - "string"
   * - Name
     - Name
     - "string"


PowerOffice GO Projectactivity to Salesforce Task
-------------------------------------------------
Every PowerOffice GO Projectactivity will be synchronized with a Salesforce Task.

Once a link between a PowerOffice GO Projectactivity and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - name
     - Subject
     - "string"


PowerOffice GO Projects to Salesforce Task
------------------------------------------
Every PowerOffice GO Projects will be synchronized with a Salesforce Task.

Once a link between a PowerOffice GO Projects and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
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


PowerOffice GO Salesorderlines to Salesforce Invoice
----------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a PowerOffice GO Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalAmount
     - "string"


PowerOffice GO Salesorders to Salesforce Invoice
------------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a PowerOffice GO Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
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


PowerOffice GO Timetrackingactivity to Salesforce Task
------------------------------------------------------
Every PowerOffice GO Timetrackingactivity will be synchronized with a Salesforce Task.

Once a link between a PowerOffice GO Timetrackingactivity and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - name
     - Subject
     - "string"


PowerOffice GO Contactperson to Salesforce Contact
--------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Salesforce Contact.

Once a link between a PowerOffice GO Contactperson and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Currency to Salesforce Currencytype
--------------------------------------------------
Every PowerOffice GO Currency will be synchronized with a Salesforce Currencytype.

Once a link between a PowerOffice GO Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


PowerOffice GO Customers person to Salesforce Customer
------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Salesforce Customer.

Once a link between a PowerOffice GO Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type


PowerOffice GO Employees to Salesforce User
-------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Salesforce User.

Once a link between a PowerOffice GO Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
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


PowerOffice GO Product to Salesforce Product2
---------------------------------------------
Every PowerOffice GO Product will be synchronized with a Salesforce Product2.

Once a link between a PowerOffice GO Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
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


PowerOffice GO Quote to Salesforce Quote
----------------------------------------
Every PowerOffice GO Quote will be synchronized with a Salesforce Quote.

Once a link between a PowerOffice GO Quote and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Quote and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Quote Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - TotalAmount
     - TotalPriceWithTax
     - "string"


PowerOffice GO Salesorderlines to Salesforce Invoiceline
--------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a PowerOffice GO Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
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


PowerOffice GO Salesorderlines to Salesforce Orderitem
------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a PowerOffice GO Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
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


PowerOffice GO Salesorderlines to Salesforce Quotelineitem
----------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a PowerOffice GO Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
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


PowerOffice GO Salesorders to Salesforce Order
----------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Salesforce Order.

Once a link between a PowerOffice GO Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
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


PowerOffice GO Suppliers person to Salesforce Contact
-----------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Salesforce Contact.

Once a link between a PowerOffice GO Suppliers person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
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

