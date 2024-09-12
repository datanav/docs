====================================
PowerOffice GO to Tripletex Dataflow
====================================

Generated: 2024-09-12 12:58:47

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


PowerOffice GO Customers to Tripletex Supplier
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Supplier must be established.

A PowerOffice GO Customers will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Supplier Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Supplier Property
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
     - "integer"
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
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCodeDependant on having wd:Q11994066 in MailAddress.CountryCode)
     - organizationNumber
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


PowerOffice GO Employees to Tripletex Country
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Employees and a Tripletex Country must be established.

A PowerOffice GO Employees will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Country Property
   * - MailAddress.CountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Employees and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Country Property
     - Tripletex Data Type


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


PowerOffice GO Contactperson to Tripletex Country
-------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Contactperson will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Country Property
   * - residenceCountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Contactperson and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Country Property
     - Tripletex Data Type


PowerOffice GO Currency to Tripletex Currency
---------------------------------------------
Every PowerOffice GO Currency will be synchronized with a Tripletex Currency.

If a matching Tripletex Currency already exists, the PowerOffice GO Currency will be merged with the existing one.
If no matching Tripletex Currency is found, a new Tripletex Currency will be created.

A PowerOffice GO Currency will merge with a Tripletex Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Tripletex Currency Property
   * - code
     - code

Once a link between a PowerOffice GO Currency and a Tripletex Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Currency and a Tripletex Currency:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Tripletex Currency Property
     - Tripletex Data Type


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


PowerOffice GO Customers to Tripletex Country
---------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Customers will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Customers will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Country Property
   * - MailAddress.CountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Customers and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Country Property
     - Tripletex Data Type


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


PowerOffice GO Location to Tripletex Country
--------------------------------------------
Every PowerOffice GO Location will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Location will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Location will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Location Property
     - Tripletex Country Property
   * - countryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Location and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Location and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Location Property
     - Tripletex Country Property
     - Tripletex Data Type


PowerOffice GO Outgoinginvoices to Tripletex Country
----------------------------------------------------
Every PowerOffice GO Outgoinginvoices will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Outgoinginvoices will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Outgoinginvoices will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Outgoinginvoices Property
     - Tripletex Country Property
   * - DeliveryAddressCountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Outgoinginvoices and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Outgoinginvoices and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Outgoinginvoices Property
     - Tripletex Country Property
     - Tripletex Data Type


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


PowerOffice GO Product to Tripletex Productunit
-----------------------------------------------
Every PowerOffice GO Product will be synchronized with a Tripletex Productunit.

If a matching Tripletex Productunit already exists, the PowerOffice GO Product will be merged with the existing one.
If no matching Tripletex Productunit is found, a new Tripletex Productunit will be created.

A PowerOffice GO Product will merge with a Tripletex Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Tripletex Productunit Property
   * - unit
     - name

Once a link between a PowerOffice GO Product and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Tripletex Productunit Property
     - Tripletex Data Type
   * - unitOfMeasureCode
     - commonCode
     - "string"
   * - unitOfMeasureCode
     - name
     - "string"


PowerOffice GO Productgroup to Tripletex Productgroup
-----------------------------------------------------
Every PowerOffice GO Productgroup will be synchronized with a Tripletex Productgroup.

Once a link between a PowerOffice GO Productgroup and a Tripletex Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Productgroup and a Tripletex Productgroup:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Productgroup Property
     - Tripletex Productgroup Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Projectactivity to Tripletex Activity
----------------------------------------------------
Every PowerOffice GO Projectactivity will be synchronized with a Tripletex Activity.

If a matching Tripletex Activity already exists, the PowerOffice GO Projectactivity will be merged with the existing one.
If no matching Tripletex Activity is found, a new Tripletex Activity will be created.

A PowerOffice GO Projectactivity will merge with a Tripletex Activity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Activity Property
   * - activityCode
     - id

Once a link between a PowerOffice GO Projectactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type


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


PowerOffice GO Suppliers person to Tripletex Country
----------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Suppliers person will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Suppliers person will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Tripletex Country Property
   * - MailAddress.CountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Suppliers person and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Tripletex Country Property
     - Tripletex Data Type


PowerOffice GO Suppliers to Tripletex Country
---------------------------------------------
Every PowerOffice GO Suppliers will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the PowerOffice GO Suppliers will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A PowerOffice GO Suppliers will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
     - Tripletex Country Property
   * - MailAddress.CountryCode
     - isoAlpha2Code

Once a link between a PowerOffice GO Suppliers and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
     - Tripletex Country Property
     - Tripletex Data Type


PowerOffice GO Suppliers to Tripletex Supplier
----------------------------------------------
Every PowerOffice GO Suppliers will be synchronized with a Tripletex Supplier.

Once a link between a PowerOffice GO Suppliers and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
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
     - deliveryAddress.city
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
     - deliveryAddress.country.id
     - "integer"
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


PowerOffice GO Vatcodes to Tripletex Vattype
--------------------------------------------
Every PowerOffice GO Vatcodes will be synchronized with a Tripletex Vattype.

Once a link between a PowerOffice GO Vatcodes and a Tripletex Vattype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Vatcodes and a Tripletex Vattype:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Vatcodes Property
     - Tripletex Vattype Property
     - Tripletex Data Type

