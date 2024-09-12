====================================
PowerOffice GO to Tripletex Dataflow
====================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Tripletex Customer person
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-outgoinginvoice, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Tripletex.

A PowerOffice GO Contactperson will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Customer person Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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
     - N/A
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - residenceCountryCode
     - address.country.id
     - "integer"
   * - zipCode
     - address.postalCode
     - "string"


PowerOffice GO Customers person to Tripletex Contact
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tripletex Contact must be established.

A PowerOffice GO Customers person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Contact Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Customers person to Tripletex Employee
-----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tripletex Employee must be established.

A PowerOffice GO Customers person will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Employee Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Projectactivity to Tripletex Projectactivity
-----------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Projectactivity and a Tripletex Projectactivity must be established.

A PowerOffice GO Projectactivity will merge with a Tripletex Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Projectactivity Property
   * - activityCode
     - activity.id

Once a link between a PowerOffice GO Projectactivity and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Projectactivity Property
     - Tripletex Data Type


Powerofficego Contactperson to Tripletex Customer
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Outgoinginvoice, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

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


PowerOffice GO Contactperson to Tripletex Contact
-------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Tripletex Contact.

If a matching Tripletex Contact already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching Tripletex Contact is found, a new Tripletex Contact will be created.

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


PowerOffice GO Customers person to Tripletex Customer person
------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Tripletex Customer person.

If a matching Tripletex Customer person already exists, the PowerOffice GO Customers person will be merged with the existing one.
If no matching Tripletex Customer person is found, a new Tripletex Customer person will be created.

A PowerOffice GO Customers person will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer person Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the PowerOffice GO Customers will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

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
     - N/A
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
     - N/A


PowerOffice GO Customers to Tripletex Customer person
-----------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer person.

Once a link between a PowerOffice GO Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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
     - N/A
   * - PhoneNumber
     - phoneNumber
     - "string"
   * - WebsiteUrl
     - website
     - "string"


PowerOffice GO Departments to Tripletex Department
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Tripletex Department.

If a matching Tripletex Department already exists, the PowerOffice GO Departments will be merged with the existing one.
If no matching Tripletex Department is found, a new Tripletex Department will be created.

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
Every PowerOffice GO Employees will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the PowerOffice GO Employees will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

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
   * - DepartmendId
     - department.id
     - N/A
   * - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - department.id (Dependant on having wd:Q2366457 in  Dependant on having wd:Q2366457 in  )
     - N/A
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - IsArchived
     - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
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
   * - dateOfBirth
     - dateOfBirth
     - N/A
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumber
     - phoneNumberMobile
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
     - isClosed
     - "string"
   * - IsInternal
     - isInternal
     - "string"
   * - Name
     - name
     - "string"
   * - ParentProjectCode
     - mainProject.id
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
   * - _sesam_hierarchy_level
     - hierarchyLevel
     - "string"
   * - sesam_hierarchyLevel
     - hierarchyLevel
     - "string"
   * - sesam_hierarchy_level
     - hierarchyLevel
     - "string"


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
     - N/A
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
   * - OrderDate
     - orderDate
     - N/A
   * - PurchaseOrderReference
     - reference
     - "string"
   * - SalesOrderDate
     - orderDate
     - N/A


PowerOffice GO Suppliers person to Tripletex Contact
----------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Tripletex Contact.

Once a link between a PowerOffice GO Suppliers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
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

