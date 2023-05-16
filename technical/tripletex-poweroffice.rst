=================================
Tripletex to PowerOffice Dataflow
=================================

Generated: 2023-05-16 12:31:08

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Address to PowerOffice Address
----------------------------------------
Every Tripletex Address will be synchronized with a PowerOffice Address.

Once a link between a Tripletex Address and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Address and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Address Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - addressLine1
     - Address1
     - "string"
   * - addressLine2
     - Address2
     - "string"
   * - city
     - City
     - "string"
   * - country.id
     - CountryCode
     - "string"
   * - postalCode
     - ZipCode
     - "string"


Tripletex Contact to PowerOffice Contactperson
----------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice Contactperson.

Once a link between a Tripletex Contact and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - customer.id
     - PartyCustomerCode
     - "string"
   * - customer.id
     - PartySupplierCode
     - "string"
   * - customer.id
     - partyCustomerCode
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberWork
     - PhoneNumber
     - "string"


Tripletex Contact to PowerOffice Customer
-----------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice Customer.

Once a link between a Tripletex Contact and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - Name
     - "string"
   * - lastName
     - LastName
     - "string"


Tripletex Employee to PowerOffice Address
-----------------------------------------
Every Tripletex Employee will be synchronized with a PowerOffice Address.

Once a link between a Tripletex Employee and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - address.addressLine1
     - Address1
     - "string"
   * - address.addressLine2
     - Address2
     - "string"
   * - address.changes
     - City
     - "string"
   * - address.city
     - CountryCode
     - "string"
   * - address.id
     - ZipCode
     - "string"


Tripletex Employee to PowerOffice Employee
------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOffice Employee.

If a matching PowerOffice Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOffice Employee is found, a new PowerOffice Employee will be created.

A Tripletex Employee will merge with a PowerOffice Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employee Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employee Property
     - PowerOffice Data Type
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


Tripletex Invoice to PowerOffice Outgoinginvoice
------------------------------------------------
Every Tripletex Invoice will be synchronized with a PowerOffice Outgoinginvoice.

Once a link between a Tripletex Invoice and a PowerOffice Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a PowerOffice Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - PowerOffice Outgoinginvoice Property
     - PowerOffice Data Type
   * - amountExcludingVat
     - NetAmount
     - "string"
   * - changes.timestamp
     - CreatedDate
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - deliveryDate
     - SentDate
     - "string"
   * - orders.id
     - OrderNo
     - "string"


Tripletex Order to PowerOffice Salesorder
-----------------------------------------
Every Tripletex Order will be synchronized with a PowerOffice Salesorder.

Once a link between a Tripletex Order and a PowerOffice Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOffice Salesorder:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOffice Salesorder Property
     - PowerOffice Data Type
   * - currency.id
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to PowerOffice Salesorderline
-------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOffice Salesorderline.

Once a link between a Tripletex Orderline and a PowerOffice Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOffice Salesorderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOffice Salesorderline Property
     - PowerOffice Data Type
   * - count
     - Quantity
     - "string"
   * - description
     - Description
     - "string"
   * - discount
     - Discount
     - "string"
   * - unitCostCurrency
     - Discount
     - "string"
   * - unitCostCurrency
     - ProductCode
     - "string"
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to PowerOffice Product
----------------------------------------
Every Tripletex Product will be synchronized with a PowerOffice Product.

Once a link between a Tripletex Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - costExcludingVatCurrency
     - CostPrice
     - "string"
   * - description
     - Description
     - "string"
   * - ean
     - Gtin
     - "string"
   * - name
     - Name
     - "string"
   * - priceExcludingVatCurrency
     - SalesPrice
     - "string"
   * - productUnit.id
     - Unit
     - "string"
   * - stockOfGoods
     - AvailableStock
     - "string"
   * - vatType
     - VatCode
     - "string"
   * - vatType.id
     - VatCode
     - "string"


Tripletex Productgroup to PowerOffice Productgroup
--------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOffice Productgroup.

Once a link between a Tripletex Productgroup and a PowerOffice Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOffice Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOffice Productgroup Property
     - PowerOffice Data Type
   * - name
     - Name
     - "string"


Tripletex Supplier to PowerOffice Supplier
------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOffice Supplier.

Once a link between a Tripletex Supplier and a PowerOffice Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOffice Supplier:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice Supplier Property
     - PowerOffice Data Type
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - LegalName
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"

