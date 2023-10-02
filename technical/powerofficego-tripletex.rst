===================================
Powerofficego to Tripletex Dataflow
===================================

Generated: 2023-10-02 14:43:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Employee to Tripletex Employee
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employee and a Tripletex Employee must be established.

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


Powerofficego Customer to Tripletex Customer
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Powerofficego Customer if it is connected to a Powerofficego Customer, Customers, or Contactperson that is synchronized into Tripletex.

Once a link between a Powerofficego Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type


Powerofficego Customer to Tripletex Department
----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee, or Employees that is synchronized into Tripletex.

Once a link between a Powerofficego Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Department Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Contact
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, or Salesorders that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Department
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Customers if it is connected to a Powerofficego Employee, or Employees that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Tripletex Customer
-----------------------------------------------
Every Powerofficego Departments will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Departments and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Salesorder to Tripletex Order
-------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorder and a Tripletex Order must be established.

A new Tripletex Order will be created from a Powerofficego Salesorder if it is connected to a Powerofficego Salesorderline that is synchronized into Tripletex.

Once a link between a Powerofficego Salesorder and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - Tripletex Order Property
     - Tripletex Data Type


Powerofficego Suppliers to Tripletex Customer
---------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Suppliers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Tripletex Customer Property
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
   * - MailAddress.AddressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - physicalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - postalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - physicalAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - postalAddress.addressLine2
     - "string"
   * - MailAddress.City
     - deliveryAddress.city
     - "string"
   * - MailAddress.City
     - physicalAddress.city
     - "string"
   * - MailAddress.City
     - postalAddress.city
     - "string"
   * - MailAddress.CountryCode
     - deliveryAddress.country.id
     - "string"
   * - MailAddress.CountryCode
     - physicalAddress.country.id
     - "integer"
   * - MailAddress.CountryCode
     - postalAddress.country.id
     - "integer"
   * - MailAddress.ZipCode
     - deliveryAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - physicalAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalAddress.postalCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


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
   * - emailAddress
     - email
     - "string"
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


Powerofficego Customers person to Tripletex Contact
---------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Customers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


Powerofficego Customers to Tripletex Customer
---------------------------------------------
Every Powerofficego Customers will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
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
   * - InvoiceEmailAddressCC
     - invoiceEmail
     - "string"
   * - MailAddress
     - email
     - "string"
   * - MailAddress.AddressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - physicalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - postalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - physicalAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - postalAddress.addressLine2
     - "string"
   * - MailAddress.City
     - deliveryAddress.city
     - "string"
   * - MailAddress.City
     - physicalAddress.city
     - "string"
   * - MailAddress.City
     - postalAddress.city
     - "string"
   * - MailAddress.CountryCode
     - deliveryAddress.country.id
     - "string"
   * - MailAddress.CountryCode
     - physicalAddress.country.id
     - "integer"
   * - MailAddress.CountryCode
     - postalAddress.country.id
     - "integer"
   * - MailAddress.ZipCode
     - deliveryAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - physicalAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalAddress.postalCode
     - "string"
   * - MailAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - MailAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - MailAddress.city
     - postalAddress.city
     - "string"
   * - MailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - MailAddress.zipCode
     - postalAddress.postalCode
     - "string"
   * - Name
     - name
     - "string"
   * - Number
     - phoneNumber
     - "string"
   * - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]
   * - PhoneNumber
     - phoneNumber
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
   * - mailAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.addressLine2
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
   * - name
     - name
     - "string"
   * - ourReferenceEmployeeCode
     - accountManager.id
     - "integer"
   * - phoneNumber
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
   * - vatNumber (Dependant on having NO in mailAddress.countryCodeDependant on having NO in mailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]


Powerofficego Departments to Tripletex Department
-------------------------------------------------
Every Powerofficego Departments will be synchronized with a Tripletex Department.

Once a link between a Powerofficego Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Employees to Tripletex Employee
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Powerofficego Employees will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Powerofficego Employees will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - DepartmendId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - DepartmentId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PhoneNumber
     - phoneNumberMobile
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumber
     - phoneNumberMobile
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
   * - availableStock
     - stockOfGoods
     - "integer"
   * - costPrice
     - costExcludingVatCurrency
     - "integer"
   * - description
     - description
     - "string"
   * - gtin
     - ean
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - priceExcludingVatCurrency
     - "float"
   * - unit
     - productUnit.id
     - "integer"
   * - unitOfMeasureCode
     - productUnit.id
     - "integer"
   * - vatCode
     - vatType.id
     - "integer"


Powerofficego Product to Tripletex Productunit
----------------------------------------------
Every Powerofficego Product will be synchronized with a Tripletex Productunit.

If a matching Tripletex Productunit already exists, the Powerofficego Product will be merged with the existing one.
If no matching Tripletex Productunit is found, a new Tripletex Productunit will be created.

A Powerofficego Product will merge with a Tripletex Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Productunit Property
   * - unitOfMeasureCode
     - name

Once a link between a Powerofficego Product and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Productunit Property
     - Tripletex Data Type
   * - unitOfMeasureCode
     - commonCode
     - "string"
   * - unitOfMeasureCode
     - name
     - "string"


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


Powerofficego Salesorderlines to Tripletex Orderline
----------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Powerofficego Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - Discount
     - discount
     - "float"
   * - ProductUnitCost
     - unitCostCurrency
     - "float"
   * - ProductUnitPrice
     - unitPriceExcludingVatCurrency
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
   * - sesam_SalesOrdersId
     - order.id
     - "integer"


Powerofficego Salesorders to Tripletex Order
--------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Tripletex Order.

Once a link between a Powerofficego Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - CurrencyCode
     - currency.id
     - "integer"
   * - OrderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - PurchaseOrderReference
     - reference
     - "string"


Powerofficego Suppliers person to Tripletex Contact
---------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Suppliers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - FirstName
     - firstName
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


Powerofficego Suppliers to Tripletex Supplier
---------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Tripletex Supplier.

Once a link between a Powerofficego Suppliers and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
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
   * - MailAddress.AddressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - physicalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - postalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - physicalAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - postalAddress.addressLine2
     - "string"
   * - MailAddress.City
     - deliveryAddress.changes
     - "string"
   * - MailAddress.City
     - physicalAddress.city
     - "string"
   * - MailAddress.City
     - postalAddress.city
     - "string"
   * - MailAddress.CountryCode
     - deliveryAddress.city
     - "string"
   * - MailAddress.CountryCode
     - physicalAddress.country.id
     - "integer"
   * - MailAddress.CountryCode
     - postalAddress.country.id
     - "integer"
   * - MailAddress.ZipCode
     - deliveryAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - physicalAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalAddress.postalCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

