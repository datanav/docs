=====================================
Salesforce to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to PowerOffice Contactperson
-----------------------------------------------
Every Salesforce Contact will be synchronized with a PowerOffice Contactperson.

Once a link between a Salesforce Contact and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - Birthdate
     - dateOfBirth
     - N/A
   * - Email
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - HomePhone
     - phoneNumber
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Phone
     - phoneNumber
     - "string"


Salesforce Customer to PowerOffice Customers person
---------------------------------------------------
Every Salesforce Customer will be synchronized with a PowerOffice Customers person.

Once a link between a Salesforce Customer and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type


Salesforce Invoiceline to PowerOffice Salesorderlines
-----------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Salesforce Invoiceline and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - UnitPrice
     - ProductUnitPrice
     - N/A


Salesforce Order to PowerOffice Salesorders
-------------------------------------------
Every Salesforce Order will be synchronized with a PowerOffice Salesorders.

Once a link between a Salesforce Order and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - CurrencyIsoCode
     - CurrencyCode
     - "string"
   * - EffectiveDate
     - SalesOrderDate
     - "string"
   * - OrderedDate
     - SalesOrderDate
     - "string"


Salesforce Orderitem to PowerOffice Salesorderlines
---------------------------------------------------
Every Salesforce Orderitem will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Salesforce Orderitem and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - OrderId
     - sesam_SalesOrderId
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - ProductUnitPrice
     - N/A


Salesforce Product2 to PowerOffice Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a PowerOffice Product.

Once a link between a Salesforce Product2 and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - Description
     - description
     - "string"
   * - Description	
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Quotelineitem to PowerOffice Salesorderlines
-------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Salesforce Quotelineitem and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - Discount
     - Allowance
     - "float"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPriceWithTax
     - ProductUnitPrice
     - N/A


Salesforce User to PowerOffice Employees
----------------------------------------
Every Salesforce User will be synchronized with a PowerOffice Employees.

Once a link between a Salesforce User and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
   * - EmployeeNumber
     - Number
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MobilePhone
     - PhoneNumber
     - "string"
   * - Title
     - JobTitle
     - "string"

