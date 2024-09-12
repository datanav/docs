================================
Salesforce to Tripletex Dataflow
================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Tripletex Contact
---------------------------------------
Every Salesforce Contact will be synchronized with a Tripletex Contact.

Once a link between a Salesforce Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Email
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - HomePhone
     - phoneNumberWork
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MobilePhone
     - phoneNumberMobile
     - N/A
   * - Phone
     - phoneNumberWork
     - "string"


Salesforce Customer to Tripletex Customer person
------------------------------------------------
Every Salesforce Customer will be synchronized with a Tripletex Customer person.

Once a link between a Salesforce Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Salesforce Invoiceline to Tripletex Orderline
---------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Tripletex Orderline.

Once a link between a Salesforce Invoiceline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - Quantity
     - count
     - N/A
   * - TaxRate
     - vatType.id
     - "integer"
   * - UnitPrice
     - unitPriceExcludingVatCurrency
     - "float"


Salesforce Order to Tripletex Order
-----------------------------------
Every Salesforce Order will be synchronized with a Tripletex Order.

Once a link between a Salesforce Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - CurrencyIsoCode
     - currency.id
     - "integer"
   * - EffectiveDate
     - deliveryDate
     - N/A
   * - EffectiveDate
     - orderDate
     - N/A
   * - EndDate
     - deliveryDate
     - N/A
   * - OrderedDate
     - orderDate
     - N/A


Salesforce Orderitem to Tripletex Orderline
-------------------------------------------
Every Salesforce Orderitem will be synchronized with a Tripletex Orderline.

Once a link between a Salesforce Orderitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - OrderId
     - order.id
     - "integer"
   * - Quantity
     - count
     - N/A
   * - TotalPrice
     - unitPriceExcludingVatCurrency
     - "float"


Salesforce Product2 to Tripletex Product
----------------------------------------
Every Salesforce Product2 will be synchronized with a Tripletex Product.

Once a link between a Salesforce Product2 and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Tripletex Product Property
     - Tripletex Data Type
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


Salesforce Quotelineitem to Tripletex Orderline
-----------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Tripletex Orderline.

Once a link between a Salesforce Quotelineitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - Discount
     - discount
     - "float"
   * - Quantity
     - count
     - N/A
   * - TotalPriceWithTax
     - unitPriceExcludingVatCurrency
     - "float"


Salesforce User to Tripletex Employee
-------------------------------------
Every Salesforce User will be synchronized with a Tripletex Employee.

Once a link between a Salesforce User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - City
     - address.city
     - "string"
   * - Country
     - address.country.id
     - "integer"
   * - EmployeeNumber
     - employeeNumber
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - ID
     - id
     - "integer"
   * - LastName
     - lastName
     - "string"
   * - MobilePhone
     - phoneNumberMobile
     - N/A
   * - PostalCode
     - address.postalCode
     - "string"
   * - Street
     - address.addressLine1
     - "string"

