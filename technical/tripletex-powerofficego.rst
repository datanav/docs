===================================
Tripletex to PowerOfficeGO Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOfficeGO Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGO Customers person must be established.

A new PowerOfficeGO Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGO.

A Tripletex Contact will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Contact and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Tripletex Customer person to PowerOfficeGO Contactperson
--------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a PowerOfficeGO Contactperson must be established.

A Tripletex Customer person will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Customer person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


Tripletex Employee to PowerOfficeGO Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOfficeGO Contactperson must be established.

A Tripletex Employee will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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
   * - department.id (Dependant on having wd:Q703534 in  )
     - partyId
     - "integer"
   * - email
     - emailAddress
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
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Employee to PowerOfficeGO Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOfficeGO Customers person must be established.

A Tripletex Employee will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Employee and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Tripletex Supplier to PowerOfficeGO Customers
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOfficeGO Customers must be established.

A Tripletex Supplier will merge with a PowerOfficeGO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Supplier and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
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
   * - email
     - PaymentReminderEmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - invoiceEmail
     - PaymentReminderEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCode)
     - "string"
   * - overdueNoticeEmail
     - PaymentReminderEmailAddress
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


Tripletex Contact to PowerOffice Customers
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOffice Customers must be established.

A new PowerOffice Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOffice.

Once a link between a Tripletex Contact and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Customers Property
     - PowerOffice Data Type


Tripletex Customer to PowerOffice Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice Contactperson must be established.

A new PowerOffice Contactperson will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into PowerOffice.

Once a link between a Tripletex Customer and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type


Tripletex Customer to PowerOffice Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into PowerOffice.

Once a link between a Tripletex Customer and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Tripletex Contact to PowerOfficeGO Contactperson
------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGO Contactperson.

If a matching PowerOfficeGO Contactperson already exists, the Tripletex Contact will be merged with the existing one.
If no matching PowerOfficeGO Contactperson is found, a new PowerOfficeGO Contactperson will be created.

A Tripletex Contact will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Contact and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - customer.id
     - partyCustomerCode
     - "string"
   * - customer.id
     - partyId
     - "string"
   * - customer.id
     - partySupplierCode
     - "string"
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


Tripletex Customer person to PowerOfficeGO Customers
----------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOfficeGO Customers.

Once a link between a Tripletex Customer person and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
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


Tripletex Customer person to PowerOfficeGO Customers person
-----------------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOfficeGO Customers person.

If a matching PowerOfficeGO Customers person already exists, the Tripletex Customer person will be merged with the existing one.
If no matching PowerOfficeGO Customers person is found, a new PowerOfficeGO Customers person will be created.

A Tripletex Customer person will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOfficeGO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Tripletex Customer to PowerOfficeGO Customers
---------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOfficeGO Customers.

If a matching PowerOfficeGO Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGO Customers is found, a new PowerOfficeGO Customers will be created.

A Tripletex Customer will merge with a PowerOfficeGO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGO Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
   * - customerNumber
     - Number
     - "string"
   * - customerNumber
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
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
   * - email
     - PaymentReminderEmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - invoiceEmail
     - PaymentReminderEmailAddress
     - "string"
   * - isPrivateIndividual
     - IsPerson
     - "boolean"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
     - "string"
   * - overdueNoticeEmail
     - PaymentReminderEmailAddress
     - "string"
   * - phoneNumber
     - Number
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
   * - postalAddress.addressLine1
     - MailAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.addressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.city
     - MailAddress.city
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.country.id
     - MailAddress.countryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.zipCode
     - "string"
   * - url
     - WebsiteUrl
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Tripletex Department to PowerOfficeGO Departments
-------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGO Departments.

If a matching PowerOfficeGO Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching PowerOfficeGO Departments is found, a new PowerOfficeGO Departments will be created.

A Tripletex Department will merge with a PowerOfficeGO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGO Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a PowerOfficeGO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGO Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGO Departments Property
     - PowerOfficeGO Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - departmentNumber
     - Code
     - "string"
   * - isInactive
     - IsActive
     - "string"
   * - name
     - Name
     - "string"


Tripletex Employee to PowerOfficeGO Employees
---------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOfficeGO Employees.

If a matching PowerOfficeGO Employees already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOfficeGO Employees is found, a new PowerOfficeGO Employees will be created.

A Tripletex Employee will merge with a PowerOfficeGO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Employees Property
   * - employeeNumber
     - Number

Once a link between a Tripletex Employee and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
   * - changes.timestamp
     - EmployeeCreatedDateTimeOffset
     - "string"
   * - changes.timestamp
     - employeeCreatedDateTimeOffset
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - N/A
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - department.id
     - DepartmendId
     - "string"
   * - department.id (Dependant on having wd:Q2366457 in  Dependant on having wd:Q2366457 in  )
     - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - "string"
   * - department.id (Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415466 in  Dependant on having wd:Q29415492 in  )
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
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberMobile
     - PhoneNumber
     - "string"
   * - phoneNumberMobile
     - phoneNumber
     - "string"
   * - sesam_employment_status
     - IsArchived
     - "boolean"
   * - userType
     - MailAddress.CountryCode
     - "string"
   * - userType
     - MailAddress.countryCode
     - "string"


Tripletex Order to PowerOfficeGO Salesorders
--------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a Tripletex Order and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - contact.id
     - CustomerId
     - "integer"
   * - contact.id
     - CustomerReferenceContactPersonId
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - customer.id
     - CustomerId
     - "integer"
   * - customer.id
     - CustomerReferenceContactPersonId
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - orderDate
     - SalesOrderDate
     - "string"
   * - reference
     - PurchaseOrderReference
     - "string"


Tripletex Orderline to PowerOfficeGO Salesorderlines
----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Tripletex Orderline and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - count
     - Quantity
     - N/A
   * - description
     - Description
     - "string"
   * - discount
     - Allowance
     - "float"
   * - discount
     - Discount
     - "string"
   * - order.id
     - sesam_SalesOrderId
     - "string"
   * - order.id
     - sesam_SalesOrdersId
     - "string"
   * - product.id
     - ProductCode
     - "string"
   * - product.id
     - ProductId
     - "integer"
   * - unitCostCurrency
     - ProductUnitCost
     - N/A
   * - unitPriceExcludingVatCurrency
     - ProductUnitPrice
     - N/A
   * - unitPriceExcludingVatCurrency
     - SalesOrderLineUnitPrice
     - "string"
   * - vatType.id
     - VatId
     - "string"
   * - vatType.id
     - VatReturnSpecification
     - "string"


Tripletex Product to PowerOfficeGO Product
------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a PowerOfficeGO Product.

Once a link between a Tripletex Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - costExcludingVatCurrency
     - CostPrice
     - "string"
   * - costExcludingVatCurrency
     - costPrice
     - "string"
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - ean
     - Gtin
     - "string"
   * - ean
     - gtin
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - SalesPrice
     - "string"
   * - priceExcludingVatCurrency
     - salesPrice
     - "string"
   * - productUnit.id
     - Unit
     - "string"
   * - productUnit.id
     - unit
     - "string"
   * - productUnit.id
     - unitOfMeasureCode
     - "string"
   * - stockOfGoods
     - AvailableStock
     - "string"
   * - stockOfGoods
     - availableStock
     - "integer"
   * - vatType.id
     - VatCode
     - "string"
   * - vatType.id
     - vatCode
     - "string"


Tripletex Project to PowerOfficeGO Projects
-------------------------------------------
Every Tripletex Project will be synchronized with a PowerOfficeGO Projects.

Once a link between a Tripletex Project and a PowerOfficeGO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a PowerOfficeGO Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - PowerOfficeGO Projects Property
     - PowerOfficeGO Data Type
   * - contact.id
     - ContactPersonId
     - "integer"
   * - customer.id
     - CustomerId
     - "integer"
   * - department.id
     - DepartmentId
     - "integer"
   * - endDate
     - EndDate
     - "string"
   * - hierarchyLevel
     - _sesam_hierarchy_level
     - "integer"
   * - hierarchyLevel
     - sesam_hierarchy_level
     - "integer"
   * - isClosed
     - IsActive
     - "string"
   * - isClosed
     - IsInternal
     - "string"
   * - isInternal
     - IsActive
     - "string"
   * - isInternal
     - IsInternal
     - "string"
   * - mainProject.id
     - ParentProjectId
     - "integer"
   * - name
     - Name
     - "string"
   * - projectManager.id
     - ProjectManagerEmployeeId
     - "integer"
   * - startDate
     - StartDate
     - "string"

