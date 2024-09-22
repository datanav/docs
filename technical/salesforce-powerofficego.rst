=====================================
Salesforce to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-22 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to PowerOffice GO Contactperson
--------------------------------------------------
Every Salesforce Contact will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Salesforce Contact and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - Birthdate
     - dateOfBirth
     - N/A
   * - Email
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Phone
     - phoneNumber
     - "string"


Salesforce Customer to PowerOffice GO Customers
-----------------------------------------------
Every Salesforce Customer will be synchronized with a PowerOffice GO Customers.

Once a link between a Salesforce Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Salesforce Customer to PowerOffice GO Customers (human data)
------------------------------------------------------------
Every Salesforce Customer will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Salesforce Customer and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type


Salesforce Invoiceline to PowerOffice GO Salesorderlines
--------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Salesforce Invoiceline and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Salesforce Order to PowerOffice GO Salesorders
----------------------------------------------
Every Salesforce Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Salesforce Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type


Salesforce Orderitem to PowerOffice GO Salesorderlines
------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Salesforce Orderitem and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Salesforce Product2 to PowerOffice GO Product
---------------------------------------------
Every Salesforce Product2 will be synchronized with a PowerOffice GO Product.

Once a link between a Salesforce Product2 and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"


Salesforce Quotelineitem to PowerOffice GO Salesorderlines
----------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Salesforce Quotelineitem and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Salesforce User to PowerOffice GO Employees
-------------------------------------------
Every Salesforce User will be synchronized with a PowerOffice GO Employees.

Once a link between a Salesforce User and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - Email
     - EmailAddress
     - "string"
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

