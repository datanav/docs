====================================
Tripletex to PowerOffice GO Dataflow
====================================

Generated: 2024-09-24 13:20:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOffice GO Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Project that is synchronized into PowerOffice GO.

A Tripletex Contact will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Contact and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Tripletex Contact to PowerOffice GO Customers
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOffice GO.

A Tripletex Contact will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Contact and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - email
     - EmailAddress
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


Tripletex Customer to PowerOffice GO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice GO Contactperson must be established.

A Tripletex Customer will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - deliveryAddress.addressLine1
     - address1
     - "string"
   * - deliveryAddress.addressLine2
     - address2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - residenceCountryCode
     - "string"
   * - deliveryAddress.postalCode
     - zipCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - address1
     - "string"
   * - physicalAddress.addressLine2
     - address2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - residenceCountryCode
     - "string"
   * - physicalAddress.postalCode
     - zipCode
     - "string"
   * - postalAddress.addressLine1
     - address1
     - "string"
   * - postalAddress.addressLine2
     - address2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - residenceCountryCode
     - "string"
   * - postalAddress.postalCode
     - zipCode
     - "string"


Tripletex Customer to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice GO Customers must be established.

A Tripletex Customer will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Tripletex Customer to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into PowerOffice GO.

A Tripletex Customer will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Tripletex Department to PowerOffice GO Departments
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOffice GO Departments must be established.

A new PowerOffice GO Departments will be created from a Tripletex Department if it is connected to a Tripletex Project, or Employee that is synchronized into PowerOffice GO.

A Tripletex Department will merge with a PowerOffice GO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOffice GO Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type


Tripletex Employee to PowerOffice GO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice GO Contactperson must be established.

A Tripletex Employee will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.id
     - residenceCountryCode
     - "string"
   * - address.postalCode
     - zipCode
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
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Employee to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice GO Customers must be established.

A Tripletex Employee will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Employee and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country.id
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - N/A
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberWork
     - PhoneNumber
     - "string"


Tripletex Employee to PowerOffice GO Employees
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice GO Employees must be established.

A Tripletex Employee will merge with a PowerOffice GO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Employees Property
   * - employeeNumber
     - Number

Once a link between a Tripletex Employee and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type


Tripletex Supplier to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOffice GO Customers must be established.

A Tripletex Supplier will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Supplier and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - url
     - WebsiteUrl
     - "string"


Tripletex Activity to PowerOffice GO Timetrackingactivity
---------------------------------------------------------
Every Tripletex Activity will be synchronized with a PowerOffice GO Timetrackingactivity.

Once a link between a Tripletex Activity and a PowerOffice GO Timetrackingactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a PowerOffice GO Timetrackingactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - PowerOffice GO Timetrackingactivity Property
     - PowerOffice GO Data Type
   * - isProjectActivity
     - requireProject
     - "string"
   * - name
     - name
     - "string"
   * - number
     - code
     - "string"


Tripletex Contact to PowerOffice GO Contactperson
-------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Tripletex Contact and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - customer.id
     - partyId
     - "integer"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer (classification data) to PowerOffice GO Customers
--------------------------------------------------------------------
Every Tripletex Customer (classification data) will be synchronized with a PowerOffice GO Customers.

Once a link between a Tripletex Customer (classification data) and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (classification data) and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (classification data) Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Tripletex Customer (organisation data) to PowerOffice GO Customers
------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOffice GO Customers.

Once a link between a Tripletex Customer (organisation data) and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (organisation data) and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (organisation data) Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - id
     - Id
     - "integer"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"


Tripletex Customer (classification data) to PowerOffice GO Customers (classification data)
------------------------------------------------------------------------------------------
Every Tripletex Customer (classification data) will be synchronized with a PowerOffice GO Customers (classification data).

Once a link between a Tripletex Customer (classification data) and a PowerOffice GO Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (classification data) and a PowerOffice GO Customers (classification data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (classification data) Property
     - PowerOffice GO Customers (classification data) Property
     - PowerOffice GO Data Type


Tripletex Customer (human data) to PowerOffice GO Customers (human data)
------------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Tripletex Customer (human data) and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - isPrivateIndividual
     - IsPerson
     - N/A
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"


Tripletex Customer to PowerOffice GO Customers
----------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOffice GO Customers.

Once a link between a Tripletex Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - customerNumber
     - Number
     - "string"
   * - customerNumber
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Tripletex Customer to PowerOffice GO Customers (human data)
-----------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Tripletex Customer and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type


Tripletex Department to PowerOffice GO Departments
--------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOffice GO Departments.

Once a link between a Tripletex Department and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type
   * - departmentNumber
     - Code
     - "string"
   * - isInactive
     - IsActive
     - "string"
   * - name
     - Name
     - "string"


Tripletex Employee to PowerOffice GO Employees
----------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOffice GO Employees.

Once a link between a Tripletex Employee and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - dateOfBirth
     - DateOfBirth
     - N/A
   * - department.id (Dependant on having wd:Q2366457 in  )
     - DepartmentId
     - "integer"
   * - department.id (Dependant on having wd:Q29415492 in  )
     - IsArchived
     - "boolean"
   * - email
     - EmailAddress
     - "string"
   * - employeeNumber
     - Number
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - PhoneNumber
     - "string"
   * - sesam_employment_status
     - IsArchived
     - "boolean"


Tripletex Order to PowerOffice GO Salesorders
---------------------------------------------
Every Tripletex Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Tripletex Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type


Tripletex Orderline to PowerOffice GO Salesorderlines
-----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Tripletex Orderline and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Tripletex Product to PowerOffice GO Product
-------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a PowerOffice GO Product.

Once a link between a Tripletex Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - costExcludingVatCurrency
     - costPrice
     - N/A
   * - description
     - description
     - "string"
   * - ean
     - gtin
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - salesPrice
     - N/A
   * - stockOfGoods
     - availableStock
     - "integer"
   * - vatType.id
     - vatCode
     - "string"


Tripletex Project to PowerOffice GO Projects
--------------------------------------------
Every Tripletex Project will be synchronized with a PowerOffice GO Projects.

Once a link between a Tripletex Project and a PowerOffice GO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a PowerOffice GO Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - PowerOffice GO Projects Property
     - PowerOffice GO Data Type
   * - startDate
     - StartDate
     - N/A


Tripletex Projectactivity to PowerOffice GO Projectactivity
-----------------------------------------------------------
Every Tripletex Projectactivity will be synchronized with a PowerOffice GO Projectactivity.

Once a link between a Tripletex Projectactivity and a PowerOffice GO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a PowerOffice GO Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - PowerOffice GO Projectactivity Property
     - PowerOffice GO Data Type
   * - activity.name
     - name
     - "string"

