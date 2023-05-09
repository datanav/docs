=================================
Poweroffice to Tripletex Dataflow
=================================

Generated: 2023-05-07 17:16:53

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Contactperson to Tripletex Contact
----------------------------------------------
Every Poweroffice Contactperson will be synchronized with a Tripletex Contact.

Once a link between a Poweroffice Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PartyCustomerCode
     - customer.id
     - "integer"
   * - PartySupplierCode
     - customer.id
     - "integer"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


Poweroffice Customer to Tripletex Contact
-----------------------------------------
Every Poweroffice Customer will be synchronized with a Tripletex Contact.

Once a link between a Poweroffice Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Name
     - firstName
     - "string"


Poweroffice Customer to Tripletex Customer
------------------------------------------
Every Poweroffice Customer will be synchronized with a Tripletex Customer.

Once a link between a Poweroffice Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - Id
     - id
     - "integer"
   * - InvoiceEmailAddress
     - invoiceEmail
     - "string"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


Poweroffice Employee to Tripletex Employee
------------------------------------------
Every Poweroffice Employee will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Poweroffice Employee will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Poweroffice Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Poweroffice Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"


Poweroffice Product to Tripletex Product
----------------------------------------
Every Poweroffice Product will be synchronized with a Tripletex Product.

Once a link between a Poweroffice Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Poweroffice Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - AvailableStock
     - stockOfGoods
     - "integer"
   * - CostPrice
     - costExcludingVatCurrency
     - "string"
   * - Description
     - description
     - "string"
   * - Gtin
     - ean
     - "string"
   * - Name
     - name
     - "string"
   * - SalesPrice
     - priceExcludingVatCurrency
     - "float"
   * - Unit
     - productUnit.id
     - "integer"
   * - VatCode
     - vatType
     - "integer"
   * - VatCode
     - vatType.id
     - "integer"


Poweroffice Productgroup to Tripletex Productgroup
--------------------------------------------------
Every Poweroffice Productgroup will be synchronized with a Tripletex Productgroup.

Once a link between a Poweroffice Productgroup and a Tripletex Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Productgroup and a Tripletex Productgroup:

.. list-table::
   :header-rows: 1

   * - Poweroffice Productgroup Property
     - Tripletex Productgroup Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Poweroffice Salesorder to Tripletex Order
-----------------------------------------
Every Poweroffice Salesorder will be synchronized with a Tripletex Order.

Once a link between a Poweroffice Salesorder and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Salesorder and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Poweroffice Salesorder Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Currency
     - currency.id
     - "integer"
   * - DeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - DepartmentCode
     - customer.id
     - "integer"
   * - OrderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]


Poweroffice Salesorderline to Tripletex Orderline
-------------------------------------------------
Every Poweroffice Salesorderline will be synchronized with a Tripletex Orderline.

Once a link between a Poweroffice Salesorderline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Salesorderline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Poweroffice Salesorderline Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - Discount
     - discount
     - "float"
   * - Discount
     - unitCostCurrency
     - "string"
   * - ProductCode
     - unitCostCurrency
     - "string"
   * - Quantity
     - count
     - "float"
   * - SalesOrderLineUnitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VatReturnSpecification
     - vatType.id
     - "integer"


Poweroffice Supplier to Tripletex Supplier
------------------------------------------
Every Poweroffice Supplier will be synchronized with a Tripletex Supplier.

Once a link between a Poweroffice Supplier and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - Tripletex Supplier Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - Id
     - id
     - "integer"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

