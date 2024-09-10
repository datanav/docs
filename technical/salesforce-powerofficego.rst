====================================
Salesforce to Powerofficego Dataflow
====================================

Generated: 2024-09-10 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Powerofficego Contactperson
-------------------------------------------------
Every Salesforce Contact will be synchronized with a Powerofficego Contactperson.

Once a link between a Salesforce Contact and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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


Salesforce Customer to Powerofficego Customers person
-----------------------------------------------------
Every Salesforce Customer will be synchronized with a Powerofficego Customers person.

Once a link between a Salesforce Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type


Salesforce Invoiceline to Powerofficego Salesorderlines
-------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Salesforce Invoiceline and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - UnitPrice
     - ProductUnitPrice
     - N/A


Salesforce Order to Powerofficego Salesorders
---------------------------------------------
Every Salesforce Order will be synchronized with a Powerofficego Salesorders.

Once a link between a Salesforce Order and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - CurrencyIsoCode
     - CurrencyCode
     - "string"
   * - EffectiveDate
     - SalesOrderDate
     - "string"
   * - OrderedDate
     - SalesOrderDate
     - "string"


Salesforce Orderitem to Powerofficego Salesorderlines
-----------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Salesforce Orderitem and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - OrderId
     - sesam_SalesOrderId
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - ProductUnitPrice
     - N/A


Salesforce Product2 to Powerofficego Product
--------------------------------------------
Every Salesforce Product2 will be synchronized with a Powerofficego Product.

Once a link between a Salesforce Product2 and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Powerofficego Product Property
     - Powerofficego Data Type
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


Salesforce Quotelineitem to Powerofficego Salesorderlines
---------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - Discount
     - Allowance
     - "float"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPriceWithTax
     - ProductUnitPrice
     - N/A

