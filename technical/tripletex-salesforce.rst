================================
Tripletex to Salesforce Dataflow
================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Salesforce Division
-----------------------------------------
Every Tripletex Customer will be synchronized with a Salesforce Division.

Once a link between a Tripletex Customer and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Tripletex Department to Salesforce Division
-------------------------------------------
Every Tripletex Department will be synchronized with a Salesforce Division.

Once a link between a Tripletex Department and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - isInactive
     - IsActive
     - "string"
   * - name
     - Name
     - "string"


Tripletex Order to Salesforce Invoice
-------------------------------------
Every Tripletex Order will be synchronized with a Salesforce Invoice.

Once a link between a Tripletex Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - deliveryDate
     - FullSettlementDate
     - "string"


Tripletex Orderline to Salesforce Invoice
-----------------------------------------
Every Tripletex Orderline will be synchronized with a Salesforce Invoice.

Once a link between a Tripletex Orderline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency.id
     - CurrencyIsoCode
     - "string"


Tripletex Project to Salesforce Task
------------------------------------
Every Tripletex Project will be synchronized with a Salesforce Task.

Once a link between a Tripletex Project and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - isClosed
     - IsClosed
     - "string"
   * - name
     - Subject
     - "string"
   * - projectManager.id
     - OwnerId
     - "string"


Tripletex Projectactivity to Salesforce Task
--------------------------------------------
Every Tripletex Projectactivity will be synchronized with a Salesforce Task.

Once a link between a Tripletex Projectactivity and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - Salesforce Task Property
     - Salesforce Data Type


Tripletex Contact to Salesforce Contact
---------------------------------------
Every Tripletex Contact will be synchronized with a Salesforce Contact.

Once a link between a Tripletex Contact and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - MobilePhone
     - "string"
   * - phoneNumberWork
     - HomePhone
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Currency to Salesforce Currencytype
---------------------------------------------
Every Tripletex Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Tripletex Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Tripletex Customer person to Salesforce Customer
------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Salesforce Customer.

Once a link between a Tripletex Customer person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Tripletex Employee to Salesforce User
-------------------------------------
Every Tripletex Employee will be synchronized with a Salesforce User.

Once a link between a Tripletex Employee and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Salesforce User Property
     - Salesforce Data Type
   * - address.addressLine1
     - Street
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.id
     - Country
     - "string"
   * - address.postalCode
     - PostalCode
     - "string"
   * - employeeNumber
     - EmployeeNumber
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - ID
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - MobilePhone
     - "string"


Tripletex Invoice to Salesforce Invoice
---------------------------------------
Every Tripletex Invoice will be synchronized with a Salesforce Invoice.

Once a link between a Tripletex Invoice and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - amountExcludingVat
     - TotalAmount
     - "string"
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - deliveryDate
     - FullSettlementDate
     - "string"
   * - invoiceDate
     - InvoiceDate
     - "string"
   * - invoiceDate
     - PostedDate
     - "string"
   * - invoiceDueDate
     - DueDate
     - "string"
   * - invoiceNumber
     - InvoiceNumber
     - "string"


Tripletex Order to Salesforce Order
-----------------------------------
Every Tripletex Order will be synchronized with a Salesforce Order.

Once a link between a Tripletex Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - deliveryDate
     - EffectiveDate
     - "string"
   * - deliveryDate
     - EndDate
     - "string"
   * - orderDate
     - EffectiveDate
     - "string"
   * - orderDate
     - OrderedDate
     - "string"


Tripletex Orderline to Salesforce Invoiceline
---------------------------------------------
Every Tripletex Orderline will be synchronized with a Salesforce Invoiceline.

Once a link between a Tripletex Orderline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - count
     - Quantity
     - "string"
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - description
     - Description
     - "string"
   * - unitPriceExcludingVatCurrency
     - UnitPrice
     - "string"
   * - vatType.id
     - TaxRate
     - "string"


Tripletex Orderline to Salesforce Orderitem
-------------------------------------------
Every Tripletex Orderline will be synchronized with a Salesforce Orderitem.

Once a link between a Tripletex Orderline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - count
     - Quantity
     - "string"
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - order.id
     - OrderId
     - "string"
   * - unitPriceExcludingVatCurrency
     - TotalPrice
     - "string"


Tripletex Orderline to Salesforce Quotelineitem
-----------------------------------------------
Every Tripletex Orderline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Tripletex Orderline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - count
     - Quantity
     - "string"
   * - currency.id
     - CurrencyIsoCode
     - "string"
   * - description
     - Description
     - "string"
   * - discount
     - Discount
     - "string"
   * - unitPriceExcludingVatCurrency
     - TotalPriceWithTax
     - "string"


Tripletex Product to Salesforce Product2
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Salesforce Product2.

Once a link between a Tripletex Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
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

