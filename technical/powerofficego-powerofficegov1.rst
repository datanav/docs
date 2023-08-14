=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-14 10:12:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to PowerOfficeGov1 Customer
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Customer must be established.

A new PowerOfficeGov1 Customer will be created from a Powerofficego Customer if it is connected to a Powerofficego Customer, Supplier, Customers, or Contactperson that is synchronized into PowerOfficeGov1.

A Powerofficego Customer will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
   * - id
     - id

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


Powerofficego Customer to PowerOfficeGov1 Department
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee that is synchronized into PowerOfficeGov1.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


Powerofficego Supplier to PowerOfficeGov1 Contact
-------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Contact.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Contact Property
     - PowerOfficeGov1 Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - InternationalIdNumber (Dependant on having superoffice-contactid in poweroffice-customer:InternationalIdType)
     - ContactId
     - "string"
   * - LegalName
     - Name
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Domains
     - "list"
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Contactperson to PowerOfficeGov1 Customer
-------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGov1 Customer.

Once a link between a Powerofficego Contactperson and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"


Powerofficego Customers to PowerOfficeGov1 Customer
---------------------------------------------------
Every Powerofficego Customers will be synchronized with a PowerOfficeGov1 Customer.

If a matching PowerOfficeGov1 Customer already exists, the Powerofficego Customers will be merged with the existing one.
If no matching PowerOfficeGov1 Customer is found, a new PowerOfficeGov1 Customer will be created.

A Powerofficego Customers will merge with a PowerOfficeGov1 Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGov1 Customer Property
   * - id
     - id

Once a link between a Powerofficego Customers and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - InternationalIdCountryCode
     - InternationalIdCountryCode
     - "string"
   * - InvoiceEmailAddressCC
     - InvoiceEmailAddressCC
     - "string"
   * - InvoiceEmailAddressCC
     - invoiceEmail
     - "string"
   * - LastName
     - LastName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - email
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - invoiceEmailAddress
     - invoiceEmailAddress
     - "string"
   * - invoiceEmailAddressCC
     - invoiceEmailAddressCC
     - "string"
   * - lastChanged
     - lastChanged
     - "string"
   * - legalName
     - legalName
     - "string"
   * - legalName
     - name
     - "string"
   * - mailAddress.address1
     - mailAddress.address1
     - "string"
   * - mailAddress.address1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - mailAddress.address2
     - "string"
   * - mailAddress.address2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.address3
     - mailAddress.address3
     - "string"
   * - mailAddress.city
     - mailAddress.city
     - "string"
   * - mailAddress.city
     - postalAddress.city
     - "string"
   * - mailAddress.countryCode
     - mailAddress.countryCode
     - "string"
   * - mailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - mailAddress.countryCode
     - streetAddresses.countryCode
     - "string"
   * - mailAddress.lastChanged
     - mailAddress.lastChanged
     - "string"
   * - mailAddress.zipCode
     - mailAddress.zipCode
     - "string"
   * - mailAddress.zipCode
     - postalAddress.postalCode
     - "string"
   * - ourReferenceEmployeeCode
     - accountManager.id
     - "integer"
   * - ourReferenceEmployeeCode
     - ourReferenceEmployeeCode
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - streetAddresses.address1
     - address.addressLine1
     - "string"
   * - streetAddresses.address1
     - physicalAddress.addressLine1
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - address.addressLine2
     - "string"
   * - streetAddresses.address2
     - physicalAddress.addressLine2
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - address.city
     - "string"
   * - streetAddresses.city
     - physicalAddress.city
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - address.country.code
     - "string"
   * - streetAddresses.countryCode
     - mailAddress.countryCode
     - "string"
   * - streetAddresses.countryCode
     - physicalAddress.country.id
     - "integer"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - address.postalCode
     - "string"
   * - streetAddresses.zipCode
     - physicalAddress.postalCode
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"
   * - vatNumber (Dependant on having wd:Q906278 in mailAddress.countryCodeDependant on having wd:Q906278 in mailAddress.countryCode)
     - mailAddress.countryCode
     - "string"
   * - vatNumber (Dependant on having NO in mailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]
   * - vatNumber
     - vatNumber (Dependant on having  in mailAddress.countryCodeDependant on having  in mailAddress.countryCode)
     - "string"
   * - websiteUrl
     - website
     - "string"
   * - websiteUrl
     - websiteUrl
     - "string"


Powerofficego Employees to PowerOfficeGov1 Employee
---------------------------------------------------
Every Powerofficego Employees will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Powerofficego Employees will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Powerofficego Employees will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGov1 Employee Property
   * - Id
     - Id
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a Powerofficego Employees and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - EmailAddress
     - EmailAddress
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - JobTitle
     - JobTitle
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.Address1
     - MailAddress.Address1
     - "string"
   * - MailAddress.Address2
     - MailAddress.Address2
     - "string"
   * - MailAddress.Address3
     - MailAddress.Address3
     - "string"
   * - MailAddress.City
     - MailAddress.City
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.LastChanged
     - MailAddress.LastChanged
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.ZipCode
     - "string"
   * - PhoneNumber
     - PhoneNumber
     - "string"
   * - id
     - id
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"

