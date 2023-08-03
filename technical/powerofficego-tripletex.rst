===================================
Powerofficego to Tripletex Dataflow
===================================

Generated: 2023-08-03 06:34:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to Tripletex Department
----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee that is synchronized into Tripletex.

Once a link between a Powerofficego Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Department Property
     - Tripletex Data Type


Powerofficego Contactperson to Tripletex Contact
------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - partyCustomerCode
     - customer.id
     - "integer"
   * - partyId
     - customer.id
     - "integer"
   * - partySupplierCode
     - customer.id
     - "integer"
   * - phoneNumber
     - phoneNumberWork
     - "string"


Powerofficego Customer to Tripletex Contact
-------------------------------------------
Every Powerofficego Customer will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - LastName
     - lastName
     - "string"
   * - firstName
     - firstName
     - "string"


Powerofficego Customer to Tripletex Customer
--------------------------------------------
Every Powerofficego Customer will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - InvoiceEmailAddress
     - invoiceEmail
     - "string"
   * - InvoiceEmailAddressCC
     - invoiceEmail
     - "string"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - emailAddress
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - legalName
     - name
     - "string"
   * - mailAddress.address1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.city
     - postalAddress.city
     - "string"
   * - mailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - mailAddress.zipCode
     - postalAddress.postalCode
     - "string"
   * - ourReferenceEmployeeCode
     - accountManager.id
     - "integer"
   * - phoneNumberMobile
     - phoneNumber
     - "string"
   * - streetAddresses.address1
     - physicalAddress.addressLine1
     - "string"
   * - streetAddresses.address2
     - physicalAddress.addressLine2
     - "string"
   * - streetAddresses.city
     - physicalAddress.city
     - "string"
   * - streetAddresses.countryCode
     - physicalAddress.country.id
     - "integer"
   * - streetAddresses.zipCode
     - physicalAddress.postalCode
     - "string"


Powerofficego Employee to Tripletex Employee
--------------------------------------------
Every Powerofficego Employee will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Powerofficego Employee will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Powerofficego Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
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


Powerofficego Product to Tripletex Product
------------------------------------------
Every Powerofficego Product will be synchronized with a Tripletex Product.

Once a link between a Powerofficego Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - AvailableStock
     - stockOfGoods
     - "integer"
   * - CostPrice
     - costExcludingVatCurrency
     - "integer"
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
     - vatType.id
     - "integer"


Powerofficego Productgroup to Tripletex Productgroup
----------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a Tripletex Productgroup.

Once a link between a Powerofficego Productgroup and a Tripletex Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a Tripletex Productgroup:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - Tripletex Productgroup Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Salesorder to Tripletex Order
-------------------------------------------
Every Powerofficego Salesorder will be synchronized with a Tripletex Order.

Once a link between a Powerofficego Salesorder and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
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


Powerofficego Salesorderline to Tripletex Orderline
---------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a Tripletex Orderline.

Once a link between a Powerofficego Salesorderline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
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
     - "float"
   * - SalesOrderLineUnitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VatReturnSpecification
     - vatType.id
     - "integer"


Powerofficego Supplier to Tripletex Supplier
--------------------------------------------
Every Powerofficego Supplier will be synchronized with a Tripletex Supplier.

Once a link between a Powerofficego Supplier and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
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

