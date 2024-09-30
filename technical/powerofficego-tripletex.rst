====================================
PowerOffice GO to Tripletex Dataflow
====================================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Tripletex Contact
-------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-projects, Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Tripletex.

A PowerOffice GO Contactperson will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Contact Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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
   * - partyId
     - customer.id
     - "integer"
   * - phoneNumber
     - phoneNumberWork
     - "string"


PowerOffice GO Contactperson to Tripletex Customer
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-outgoinginvoice, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Tripletex.

A PowerOffice GO Contactperson will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Customer Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Customer Property
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


PowerOffice GO Contactperson to Tripletex Employee
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Employee must be established.

A PowerOffice GO Contactperson will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Employee Property
   * - emailAddress
     - email
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a PowerOffice GO Contactperson and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Employee Property
     - Tripletex Data Type
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
     - N/A
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - residenceCountryCode
     - address.country.id
     - "integer"
   * - zipCode
     - address.postalCode
     - "string"


PowerOffice GO Customers to Tripletex Contact
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Contact must be established.

A PowerOffice GO Customers will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Contact Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Customer must be established.

A PowerOffice GO Customers will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Customers to Tripletex Employee
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Employee must be established.

A PowerOffice GO Customers will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Employee Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - N/A
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
   * - LastName
     - lastName
     - "string"
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
   * - PhoneNumber
     - phoneNumberWork
     - "string"


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-customer, Powerofficego-projects, Powerofficego-customers, Powerofficego-suppliers, Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-contactperson, Powerofficego-outgoinginvoice, Powerofficego-salesorderlines, Powerofficego-customers-person, Powerofficego-outgoinginvoices, or Powerofficego-suppliers-person that is synchronized into Tripletex.

A PowerOffice GO Customers will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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
   * - Number
     - customerNumber
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCode)
     - customerNumber
     - "string"
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - organizationNumber
     - N/A
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - website
     - "string"


PowerOffice GO Departments to Tripletex Department
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Departments and a Tripletex Department must be established.

A new Tripletex Department will be created from a PowerOffice GO Departments if it is connected to a PowerOffice GO Powerofficego-employee, Powerofficego-projects, Powerofficego-employees, Powerofficego-contactperson, or Powerofficego-customers-person that is synchronized into Tripletex.

A PowerOffice GO Departments will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
   * - Code
     - departmentNumber

Once a link between a PowerOffice GO Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Code
     - departmentNumber
     - "string"
   * - IsActive
     - isInactive
     - "string"
   * - Name
     - name
     - "string"


PowerOffice GO Employees to Tripletex Employee
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Employees and a Tripletex Employee must be established.

A PowerOffice GO Employees will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
   * - Number
     - employeeNumber

Once a link between a PowerOffice GO Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - N/A
   * - DepartmentId
     - department.id (Dependant on having wd:Q2366457 in  )
     - N/A
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - IsArchived
     - department.id (Dependant on having wd:Q29415492 in  )
     - N/A
   * - IsArchived
     - sesam_employment_status
     - "boolean"
   * - LastName
     - lastName
     - "string"
   * - Number
     - employeeNumber
     - "string"
   * - PhoneNumber
     - phoneNumberMobile
     - N/A


PowerOffice GO Contactperson to Tripletex Contact
-------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Tripletex Contact.

Once a link between a PowerOffice GO Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type


PowerOffice GO Customers (organisation data) to Tripletex Customer
------------------------------------------------------------------
Every PowerOffice GO Customers (organisation data) will be synchronized with a Tripletex Customer.

Once a link between a PowerOffice GO Customers (organisation data) and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (organisation data) and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (organisation data) Property
     - Tripletex Customer Property
     - Tripletex Data Type


PowerOffice GO Customers (classification data) to Tripletex Customer (classification data)
------------------------------------------------------------------------------------------
Every PowerOffice GO Customers (classification data) will be synchronized with a Tripletex Customer (classification data).

Once a link between a PowerOffice GO Customers (classification data) and a Tripletex Customer (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (classification data) and a Tripletex Customer (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (classification data) Property
     - Tripletex Customer (classification data) Property
     - Tripletex Data Type


PowerOffice GO Customers (human data) to Tripletex Customer (human data)
------------------------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a Tripletex Customer (human data).

Once a link between a PowerOffice GO Customers (human data) and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer.

Once a link between a PowerOffice GO Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer (classification data)
--------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer (classification data).

Once a link between a PowerOffice GO Customers and a Tripletex Customer (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer (classification data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer (classification data) Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer (human data)
-----------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer (human data).

Once a link between a PowerOffice GO Customers and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type


PowerOffice GO Departments to Tripletex Department
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Tripletex Department.

Once a link between a PowerOffice GO Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
     - Tripletex Data Type


PowerOffice GO Employees to Tripletex Employee
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Tripletex Employee.

Once a link between a PowerOffice GO Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"


PowerOffice GO Product to Tripletex Product
-------------------------------------------
Every PowerOffice GO Product will be synchronized with a Tripletex Product.

Once a link between a PowerOffice GO Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - availableStock
     - stockOfGoods
     - "integer"
   * - costPrice
     - costExcludingVatCurrency
     - "float"
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
   * - vatCode
     - vatType.id
     - "integer"


PowerOffice GO Projectactivity to Tripletex Projectactivity
-----------------------------------------------------------
Every PowerOffice GO Projectactivity will be synchronized with a Tripletex Projectactivity.

Once a link between a PowerOffice GO Projectactivity and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Projectactivity Property
     - Tripletex Data Type
   * - name
     - activity.name
     - "string"


PowerOffice GO Projects to Tripletex Project
--------------------------------------------
Every PowerOffice GO Projects will be synchronized with a Tripletex Project.

Once a link between a PowerOffice GO Projects and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - ContactPersonId
     - contact.id
     - "integer"
   * - CustomerId
     - customer.id
     - "integer"
   * - DepartmentId
     - department.id
     - "integer"
   * - EndDate
     - endDate
     - N/A
   * - IsActive
     - isClosed
     - "string"
   * - IsInternal
     - isInternal
     - "string"
   * - Name
     - name
     - "string"
   * - ParentProjectId
     - mainProject.id
     - "integer"
   * - ProjectManagerEmployeeId
     - projectManager.id
     - "integer"
   * - StartDate
     - startDate
     - N/A


PowerOffice GO Salesorderlines to Tripletex Orderline
-----------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a PowerOffice GO Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Allowance
     - discount
     - "float"
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
     - N/A
   * - VatRate
     - vatType.id
     - "integer"
   * - sesam_SalesOrderId
     - order.id
     - "integer"


PowerOffice GO Salesorders to Tripletex Order
---------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Tripletex Order.

Once a link between a PowerOffice GO Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
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
   * - PurchaseOrderReference
     - reference
     - "string"
   * - SalesOrderDate
     - orderDate
     - N/A


PowerOffice GO Suppliers (human data) to Tripletex Contact
----------------------------------------------------------
Every PowerOffice GO Suppliers (human data) will be synchronized with a Tripletex Contact.

Once a link between a PowerOffice GO Suppliers (human data) and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers (human data) and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers (human data) Property
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


PowerOffice GO Timetrackingactivity to Tripletex Activity
---------------------------------------------------------
Every PowerOffice GO Timetrackingactivity will be synchronized with a Tripletex Activity.

Once a link between a PowerOffice GO Timetrackingactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type
   * - code
     - number
     - "string"
   * - name
     - name
     - "string"
   * - requireProject
     - isProjectActivity
     - "string"

