====================================
Tripletex to PowerOffice GO Dataflow
====================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOffice Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOffice.

A Tripletex Contact will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Contact and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Tripletex Customer person to PowerOffice Contactperson
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a PowerOffice Contactperson must be established.

A Tripletex Customer person will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Customer person and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Tripletex Employee to PowerOffice Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice Contactperson must be established.

A Tripletex Employee will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Tripletex Employee to PowerOffice Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice Customers person must be established.

A Tripletex Employee will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Employee and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Tripletex Supplier to PowerOffice Customers
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a PowerOffice Customers must be established.

A Tripletex Supplier will merge with a PowerOffice Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Supplier and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice Customers Property
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


Tripletex Contact to Powerofficego Customers
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into Powerofficego.

Once a link between a Tripletex Contact and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Tripletex Customer to Powerofficego Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into Powerofficego.

Once a link between a Tripletex Customer and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


Tripletex Customer to Powerofficego Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into Powerofficego.

Once a link between a Tripletex Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
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


Tripletex Contact to PowerOffice Contactperson
----------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice Contactperson.

If a matching PowerOffice Contactperson already exists, the Tripletex Contact will be merged with the existing one.
If no matching PowerOffice Contactperson is found, a new PowerOffice Contactperson will be created.

A Tripletex Contact will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Contact and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Tripletex Customer person to PowerOffice Customers
--------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOffice Customers.

Once a link between a Tripletex Customer person and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice Customers Property
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


Tripletex Customer person to PowerOffice Customers person
---------------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOffice Customers person.

If a matching PowerOffice Customers person already exists, the Tripletex Customer person will be merged with the existing one.
If no matching PowerOffice Customers person is found, a new PowerOffice Customers person will be created.

A Tripletex Customer person will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
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


Tripletex Customer to PowerOffice Customers
-------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOffice Customers.

If a matching PowerOffice Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOffice Customers is found, a new PowerOffice Customers will be created.

A Tripletex Customer will merge with a PowerOffice Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
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


Tripletex Department to PowerOffice Departments
-----------------------------------------------
Every Tripletex Department will be synchronized with a PowerOffice Departments.

If a matching PowerOffice Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching PowerOffice Departments is found, a new PowerOffice Departments will be created.

A Tripletex Department will merge with a PowerOffice Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOffice Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a PowerOffice Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOffice Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOffice Departments Property
     - PowerOffice Data Type
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


Tripletex Employee to PowerOffice Employees
-------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOffice Employees.

If a matching PowerOffice Employees already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOffice Employees is found, a new PowerOffice Employees will be created.

A Tripletex Employee will merge with a PowerOffice Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employees Property
   * - employeeNumber
     - Number

Once a link between a Tripletex Employee and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
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


Tripletex Order to PowerOffice Salesorders
------------------------------------------
Every Tripletex Order will be synchronized with a PowerOffice Salesorders.

Once a link between a Tripletex Order and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
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


Tripletex Orderline to PowerOffice Salesorderlines
--------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Tripletex Orderline and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
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


Tripletex Product to PowerOffice Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a PowerOffice Product.

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


Tripletex Project to PowerOffice Projects
-----------------------------------------
Every Tripletex Project will be synchronized with a PowerOffice Projects.

Once a link between a Tripletex Project and a PowerOffice Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a PowerOffice Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - PowerOffice Projects Property
     - PowerOffice Data Type
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

