====================================
Salesforce to PowerOfficeGO Dataflow
====================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to PowerOfficeGO Contactperson
-------------------------------------------------
Every Salesforce Contact will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a Salesforce Contact and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


Salesforce Customer to PowerOfficeGO Customers person
-----------------------------------------------------
Every Salesforce Customer will be synchronized with a PowerOfficeGO Customers person.

Once a link between a Salesforce Customer and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type


Salesforce Invoiceline to PowerOfficeGO Salesorderlines
-------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Salesforce Invoiceline and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - UnitPrice
     - ProductUnitPrice
     - N/A


Salesforce Order to PowerOfficeGOPowerofficego Salesorders
----------------------------------------------------------
Every Salesforce Order will be synchronized with a PowerOfficeGOPowerofficego Salesorders.

Once a link between a Salesforce Order and a PowerOfficeGOPowerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a PowerOfficeGOPowerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - PowerOfficeGOPowerofficego Salesorders Property
     - PowerOfficeGOPowerofficego Data Type
   * - CurrencyIsoCode
     - CurrencyCode
     - "string"
   * - EffectiveDate
     - SalesOrderDate
     - "string"
   * - OrderedDate
     - SalesOrderDate
     - "string"


Salesforce Orderitem to PowerOfficeGO Salesorderlines
-----------------------------------------------------
Every Salesforce Orderitem will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Salesforce Orderitem and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - OrderId
     - sesam_SalesOrderId
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - ProductUnitPrice
     - N/A


Salesforce Product2 to PowerOfficeGOPowerofficego Product
---------------------------------------------------------
Every Salesforce Product2 will be synchronized with a PowerOfficeGOPowerofficego Product.

Once a link between a Salesforce Product2 and a PowerOfficeGOPowerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a PowerOfficeGOPowerofficego Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - PowerOfficeGOPowerofficego Product Property
     - PowerOfficeGOPowerofficego Data Type
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


Salesforce Quotelineitem to PowerOfficeGO Salesorderlines
---------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Salesforce Quotelineitem and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - Discount
     - Allowance
     - "float"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPriceWithTax
     - ProductUnitPrice
     - N/A


Salesforce User to PowerOfficeGO Employees
------------------------------------------
Every Salesforce User will be synchronized with a PowerOfficeGO Employees.

Once a link between a Salesforce User and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
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

