===================================
Tripletex to PowerOfficeGO Dataflow
===================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to PowerOfficeGOPowerOfficeGo Customers person
----------------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers person must be established.

A new PowerOfficeGOPowerOfficeGo Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGOPowerOfficeGo.

A Tripletex Contact will merge with a PowerOfficeGOPowerOfficeGo Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
   * - email
     - EmailAddress

Once a link between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
     - PowerOfficeGOPowerOfficeGo Data Type
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


Tripletex Projectactivity to PowerOfficeGO Projectactivity
----------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Projectactivity and a PowerOfficeGO Projectactivity must be established.

A Tripletex Projectactivity will merge with a PowerOfficeGO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - PowerOfficeGO Projectactivity Property
   * - activity.id
     - activityCode

Once a link between a Tripletex Projectactivity and a PowerOfficeGO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectactivity and a PowerOfficeGO Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectactivity Property
     - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Data Type


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


Tripletex Contact to PowerOfficeGOPowerOfficeGo Customers
---------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers must be established.

A new PowerOfficeGOPowerOfficeGo Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into PowerOfficeGOPowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGOPowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGOPowerOfficeGo Customers Property
     - PowerOfficeGOPowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGOPowerOfficeGo Contactperson
--------------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGOPowerOfficeGo Contactperson must be established.

A new PowerOfficeGOPowerOfficeGo Contactperson will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into PowerOfficeGOPowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGOPowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGOPowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGOPowerOfficeGo Contactperson Property
     - PowerOfficeGOPowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person
--------------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person must be established.

A new PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Project, Customer, Employee, Orderline, or Customer-person that is synchronized into PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego.

Once a link between a Tripletex Customer and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers person Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Data Type
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


Tripletex Activity to PowerOfficeGO Projectactivity
---------------------------------------------------
Every Tripletex Activity will be synchronized with a PowerOfficeGO Projectactivity.

If a matching PowerOfficeGO Projectactivity already exists, the Tripletex Activity will be merged with the existing one.
If no matching PowerOfficeGO Projectactivity is found, a new PowerOfficeGO Projectactivity will be created.

A Tripletex Activity will merge with a PowerOfficeGO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - PowerOfficeGO Projectactivity Property
   * - id
     - activityCode

Once a link between a Tripletex Activity and a PowerOfficeGO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Activity and a PowerOfficeGO Projectactivity:

.. list-table::
   :header-rows: 1

   * - Tripletex Activity Property
     - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Data Type
   * - name
     - name
     - "string"


Tripletex Contact to PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson
----------------------------------------------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson.

If a matching PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson already exists, the Tripletex Contact will be merged with the existing one.
If no matching PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson is found, a new PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson will be created.

A Tripletex Contact will merge with a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Tripletex Contact and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Contactperson Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Data Type
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


Tripletex Customer to PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers
-------------------------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers.

If a matching PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers is found, a new PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers will be created.

A Tripletex Customer will merge with a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers Property
   * - email
     - EmailAddress

Once a link between a Tripletex Customer and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Customers Property
     - PowerOfficeGOPowerOfficeGoPowerOffice GOPowerofficego Data Type
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


Tripletex Department to PowerOfficeGOPowerOffice GOPowerofficego Departments
----------------------------------------------------------------------------
Every Tripletex Department will be synchronized with a PowerOfficeGOPowerOffice GOPowerofficego Departments.

If a matching PowerOfficeGOPowerOffice GOPowerofficego Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching PowerOfficeGOPowerOffice GOPowerofficego Departments is found, a new PowerOfficeGOPowerOffice GOPowerofficego Departments will be created.

A Tripletex Department will merge with a PowerOfficeGOPowerOffice GOPowerofficego Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGOPowerOffice GOPowerofficego Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a PowerOfficeGOPowerOffice GOPowerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGOPowerOffice GOPowerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGOPowerOffice GOPowerofficego Departments Property
     - PowerOfficeGOPowerOffice GOPowerofficego Data Type
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


Tripletex Order to PowerOfficeGOPowerOfficeGo Salesorders
---------------------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGOPowerOfficeGo Salesorders.

Once a link between a Tripletex Order and a PowerOfficeGOPowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGOPowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGOPowerOfficeGo Salesorders Property
     - PowerOfficeGOPowerOfficeGo Data Type
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


Tripletex Project to PowerOfficeGOPowerOffice GOPowerofficego Projects
----------------------------------------------------------------------
Every Tripletex Project will be synchronized with a PowerOfficeGOPowerOffice GOPowerofficego Projects.

Once a link between a Tripletex Project and a PowerOfficeGOPowerOffice GOPowerofficego Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a PowerOfficeGOPowerOffice GOPowerofficego Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - PowerOfficeGOPowerOffice GOPowerofficego Projects Property
     - PowerOfficeGOPowerOffice GOPowerofficego Data Type
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

