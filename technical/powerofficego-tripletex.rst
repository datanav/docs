==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Employee
----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Employee must be established.

A Powerofficego Contactperson will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Employee Property
   * - emailAddress
     - email
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Contactperson and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Employee Property
     -  Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - partyId
     - department.id (Dependant on having wd:Q703534 in  )
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - residenceCountryCode
     - address.country.id
     - "integer"
   * - zipCode
     - address.postalCode
     - "string"


Powerofficego Customers person to  Contact
------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Contact must be established.

A Powerofficego Customers person will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contact Property
   * - EmailAddress
     - email

Once a link between a Powerofficego Customers person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contact Property
     -  Data Type


Powerofficego Customers person to  Employee
-------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Employee must be established.

A Powerofficego Customers person will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Employee Property
   * - EmailAddress
     - email

Once a link between a Powerofficego Customers person and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Employee Property
     -  Data Type
   * - Id
     - id
     - "integer"
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.id
     - "integer"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"


Powerofficego Contactperson to Tripletex Customer person
--------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Contactperson and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - address1
     - deliveryAddress.addressLine1
     - "string"
   * - address1
     - physicalAddress.addressLine1
     - "string"
   * - address1
     - postalAddress.addressLine1
     - "string"
   * - address2
     - deliveryAddress.addressLine2
     - "string"
   * - address2
     - physicalAddress.addressLine2
     - "string"
   * - address2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - residenceCountryCode
     - deliveryAddress.country.id
     - "string"
   * - residenceCountryCode
     - physicalAddress.country.id
     - "integer"
   * - residenceCountryCode
     - postalAddress.country.id
     - "integer"
   * - zipCode
     - deliveryAddress.postalCode
     - "string"
   * - zipCode
     - physicalAddress.postalCode
     - "string"
   * - zipCode
     - postalAddress.postalCode
     - "string"


Powerofficego Contactperson to Tripletex Customer
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Contactperson and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - residenceCountryCode
     - invoiceSendMethod
     - "string"


Powerofficego Customers to Tripletex Contact
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Powerofficego Contactperson to Tripletex Contact
------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Tripletex Contact.

If a matching Tripletex Contact already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching Tripletex Contact is found, a new Tripletex Contact will be created.

A Powerofficego Contactperson will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Contact Property
   * - emailAddress
     - email

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


Powerofficego Customers person to  Customer person
--------------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customer person.

Once a link between a Powerofficego Customers person and a  Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customer person Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - Id
     - id
     - "integer"
   * - InvoiceEmailAddress
     - invoiceEmail
     - "string"
   * - IsPerson
     - isPrivateIndividual
     - "boolean"
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


Powerofficego Customers to Tripletex Customer
---------------------------------------------
Every Powerofficego Customers will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the Powerofficego Customers will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

A Powerofficego Customers will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Customer Property
   * - EmailAddress
     - email

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
   * - IsPerson
     - isPrivateIndividual
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
     - invoiceSendMethod
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
     - customerNumber
     - "string"
   * - Number
     - phoneNumber
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - customerNumber
     - "string"
   * - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - url
     - "string"
   * - WebsiteUrl
     - website
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


Powerofficego Customers to Tripletex Customer person
----------------------------------------------------
Every Powerofficego Customers will be synchronized with a Tripletex Customer person.

Once a link between a Powerofficego Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Customer person Property
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
   * - Name
     - name
     - "string"
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - organizationNumber
     - "replace"," ","", "string"]
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - website
     - "string"


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


Powerofficego Employees to  Employee
------------------------------------
Every Powerofficego Employees will be synchronized with a  Employee.

If a matching  Employee already exists, the Powerofficego Employees will be merged with the existing one.
If no matching  Employee is found, a new  Employee will be created.

A Powerofficego Employees will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Employee Property
   * - Number
     - employeeNumber

Once a link between a Powerofficego Employees and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Employee Property
     -  Data Type
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - DepartmendId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - department.id (Dependant on having wd:Q2366457 in  Dependant on having wd:Q2366457 in  )
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Number
     - employeeNumber
     - "string"
   * - PhoneNumber
     - phoneNumberMobile
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
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


Powerofficego Projects to  Project
----------------------------------
Every Powerofficego Projects will be synchronized with a  Project.

Once a link between a Powerofficego Projects and a  Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Project:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Project Property
     -  Data Type
   * - ContactPersonId
     - contact.id
     - "integer"
   * - CustomerId
     - customer.id
     - "integer"
   * - DepartmentId
     - department.id
     - "string"
   * - EndDate
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - IsActive
     - isClosed
     - "string"
   * - IsInternal
     - isClosed
     - "string"
   * - IsInternal
     - isInternal
     - "string"
   * - Name
     - name
     - "string"
   * - ProjectManagerEmployeeId
     - projectManager.id
     - "integer"
   * - StartDate
     - startDate
     - "datetime-format","%Y-%m-%d","_."]


Powerofficego Salesorderlines to  Orderline
-------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Orderline.

Once a link between a Powerofficego Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Orderline Property
     -  Data Type
   * - Allowance
     - discount
     - "float"
   * - Description
     - description
     - "string"
   * - Discount
     - discount
     - "float"
   * - ProductCode
     - product.id
     - "integer"
   * - ProductId
     - product.id
     - "integer"
   * - ProductUnitCost
     - unitCostCurrency
     - "float"
   * - ProductUnitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - Quantity
     - count
     - "integer", "decimal"]
   * - SalesOrderLineUnitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VatId
     - vatType.id
     - "integer"
   * - VatRate
     - vatType.id
     - "integer"
   * - VatReturnSpecification
     - vatType.id
     - "integer"
   * - sesam_SalesOrderId
     - order.id
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
   * - CustomerId
     - contact.id
     - "integer"
   * - CustomerId
     - customer.id
     - "integer"
   * - CustomerReferenceContactPersonId
     - contact.id
     - "integer"
   * - CustomerReferenceContactPersonId
     - customer.id
     - "integer"
   * - OrderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - PurchaseOrderReference
     - reference
     - "string"
   * - SalesOrderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]


Powerofficego Suppliers person to  Contact
------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Contact.

Once a link between a Powerofficego Suppliers person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Contact Property
     -  Data Type
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

