=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-15 08:52:57

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


Powerofficego Suppliers to PowerOfficeGov1 Address
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGov1 Address must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGov1 Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGov1 Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGov1 Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Address Property
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


Powerofficego Customers to PowerOfficeGov1 Contactperson
--------------------------------------------------------
Every Powerofficego Customers will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Powerofficego Customers and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
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


Powerofficego Salesorders to PowerOfficeGov1 Salesorder
-------------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Powerofficego Salesorders and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type


Powerofficego Suppliers to PowerOfficeGov1 Supplier
---------------------------------------------------
Every Powerofficego Suppliers will be synchronized with a PowerOfficeGov1 Supplier.

If a matching PowerOfficeGov1 Supplier already exists, the Powerofficego Suppliers will be merged with the existing one.
If no matching PowerOfficeGov1 Supplier is found, a new PowerOfficeGov1 Supplier will be created.

A Powerofficego Suppliers will merge with a PowerOfficeGov1 Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Supplier Property
   * - Id
     - Id

Once a link between a Powerofficego Suppliers and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - EmailAddress
     - EmailAddress
     - "string"
   * - Id
     - Id
     - "string"
   * - InternationalIdCountryCode
     - InternationalIdCountryCode
     - "string"
   * - InternationalIdNumber (Dependant on having poweroffice-supplier in poweroffice-customer:InternationalIdType)
     - Id
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LegalName
     - LegalName
     - "string"
   * - PhoneNumber
     - PhoneNumber
     - "string"
   * - WebsiteUrl
     - WebsiteUrl
     - "string"


Powerofficego Vatcodes to PowerOfficeGov1 Vatcode
-------------------------------------------------
Every Powerofficego Vatcodes will be synchronized with a PowerOfficeGov1 Vatcode.

If a matching PowerOfficeGov1 Vatcode already exists, the Powerofficego Vatcodes will be merged with the existing one.
If no matching PowerOfficeGov1 Vatcode is found, a new PowerOfficeGov1 Vatcode will be created.

A Powerofficego Vatcodes will merge with a PowerOfficeGov1 Vatcode if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcodes Property
     - PowerOfficeGov1 Vatcode Property
   * - id
     - id

Once a link between a Powerofficego Vatcodes and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcodes and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcodes Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - rate
     - rate
     - "string"

