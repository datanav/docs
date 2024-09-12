====================================
Tripletex to PowerOffice GO Dataflow
====================================

Generated: 2024-09-12 12:58:47

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOffice GO Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOffice GO.

A Tripletex Contact will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Contact and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Customers person Property
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


Tripletex Customer person to PowerOffice GO Contactperson
---------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a PowerOffice GO Contactperson must be established.

A Tripletex Customer person will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Customer person and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
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


Tripletex Employee to PowerOffice GO Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOffice GO Customers person must be established.

A Tripletex Employee will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Employee and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOffice GO Customers person Property
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


Tripletex Projectactivity to PowerOffice GO Projectactivity
-----------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Projectactivity and a PowerOffice GO Projectactivity must be established.

A Tripletex Projectactivity will merge with a PowerOffice GO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - PowerOffice GO Projectactivity Property
   * - activity.id
     - activityCode

Once a link between a Tripletex Projectactivity and a PowerOffice GO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a PowerOffice GO Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - PowerOffice GO Projectactivity Property
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


Tripletex Contact to PowerOfficeGo Customers
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOffice GO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into PowerOffice GO.

Once a link between a Tripletex Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Tripletex Customer to PowerOfficeGo Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
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


Tripletex Activity to PowerOffice GO Projectactivity
----------------------------------------------------
Every Tripletex Activity will be synchronized with a PowerOffice GO Projectactivity.

If a matching PowerOffice GO Projectactivity already exists, the Tripletex Activity will be merged with the existing one.
If no matching PowerOffice GO Projectactivity is found, a new PowerOffice GO Projectactivity will be created.

A Tripletex Activity will merge with a PowerOffice GO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - PowerOffice GO Projectactivity Property
   * - id
     - activityCode

Once a link between a Tripletex Activity and a PowerOffice GO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a PowerOffice GO Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - PowerOffice GO Projectactivity Property
     - PowerOffice GO Data Type
   * - name
     - name
     - "string"


Tripletex Contact to PowerOffice GO Contactperson
-------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice GO Contactperson.

If a matching PowerOffice GO Contactperson already exists, the Tripletex Contact will be merged with the existing one.
If no matching PowerOffice GO Contactperson is found, a new PowerOffice GO Contactperson will be created.

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


Tripletex Contact to PowerOffice GO Suppliers person
----------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOffice GO Suppliers person.

Once a link between a Tripletex Contact and a PowerOffice GO Suppliers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOffice GO Suppliers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOffice GO Suppliers person Property
     - PowerOffice GO Data Type


Tripletex Currency to PowerOffice GO Currency
---------------------------------------------
Every Tripletex Currency will be synchronized with a PowerOffice GO Currency.

If a matching PowerOffice GO Currency already exists, the Tripletex Currency will be merged with the existing one.
If no matching PowerOffice GO Currency is found, a new PowerOffice GO Currency will be created.

A Tripletex Currency will merge with a PowerOffice GO Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOffice GO Currency Property
   * - code
     - code

Once a link between a Tripletex Currency and a PowerOffice GO Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a PowerOffice GO Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOffice GO Currency Property
     - PowerOffice GO Data Type


Tripletex Customer person to PowerOffice GO Customers
-----------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOffice GO Customers.

Once a link between a Tripletex Customer person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
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
   * - website
     - WebsiteUrl
     - "string"


Tripletex Customer person to PowerOffice GO Customers person
------------------------------------------------------------
Every Tripletex Customer person will be synchronized with a PowerOffice GO Customers person.

If a matching PowerOffice GO Customers person already exists, the Tripletex Customer person will be merged with the existing one.
If no matching PowerOffice GO Customers person is found, a new PowerOffice GO Customers person will be created.

A Tripletex Customer person will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice GO Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - PowerOffice GO Customers person Property
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

If a matching PowerOffice GO Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOffice GO Customers is found, a new PowerOffice GO Customers will be created.

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


Tripletex Department to PowerOffice GO Departments
--------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOffice GO Departments.

If a matching PowerOffice GO Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching PowerOffice GO Departments is found, a new PowerOffice GO Departments will be created.

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


Tripletex Employee to PowerOffice GO Employees
----------------------------------------------
Every Tripletex Employee will be synchronized with a PowerOffice GO Employees.

If a matching PowerOffice GO Employees already exists, the Tripletex Employee will be merged with the existing one.
If no matching PowerOffice GO Employees is found, a new PowerOffice GO Employees will be created.

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


Tripletex Productgroup to PowerOffice GO Productgroup
-----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a PowerOffice GO Productgroup.

Once a link between a Tripletex Productgroup and a PowerOffice GO Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOffice GO Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOffice GO Productgroup Property
     - PowerOffice GO Data Type
   * - name
     - Name
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


Tripletex Supplier to PowerOffice GO Suppliers
----------------------------------------------
Every Tripletex Supplier will be synchronized with a PowerOffice GO Suppliers.

Once a link between a Tripletex Supplier and a PowerOffice GO Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a PowerOffice GO Suppliers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - PowerOffice GO Suppliers Property
     - PowerOffice GO Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.changes
     - MailAddress.City
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.city
     - MailAddress.CountryCode
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
     - "string"
   * - name
     - LegalName
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


Tripletex Vattype to PowerOffice GO Vatcodes
--------------------------------------------
Every Tripletex Vattype will be synchronized with a PowerOffice GO Vatcodes.

Once a link between a Tripletex Vattype and a PowerOffice GO Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a PowerOffice GO Vatcodes:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - PowerOffice GO Vatcodes Property
     - PowerOffice GO Data Type
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - percentage
     - Rate
     - "string"
   * - percentage
     - rate
     - "string"

