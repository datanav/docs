==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Ansatt
--------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Ansatt must be established.

A Powerofficego Contactperson will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Ansatt Property
   * - emailAddress
     - Epost
   * - SocialSecurityNumber
     - Personnummer

Once a link between a Powerofficego Contactperson and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Ansatt Property
     -  Data Type
   * - address1
     - Adresse
     - "string"
   * - city
     - Poststed
     - "string"
   * - dateOfBirth
     - Fodt
     - "string"
   * - firstName
     - Fornavn
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - Etternavn
     - "string"
   * - partyId
     - AvdelingId
     - "string"
   * - partyId
     - Tittel
     - "string"
   * - partyId
     - sesam_ansattId
     - "integer"
   * - zipCode
     - Postnummer
     - "string"


Powerofficego Customers person to  Ansatt
-----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Ansatt must be established.

A Powerofficego Customers person will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Ansatt Property
   * - EmailAddress
     - Epost

Once a link between a Powerofficego Customers person and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Ansatt Property
     -  Data Type
   * - Id
     - Id
     - "integer"
   * - MailAddress.AddressLine1
     - Adresse
     - "string"
   * - MailAddress.City
     - Poststed
     - "string"
   * - MailAddress.ZipCode
     - Postnummer
     - "string"


Powerofficego Customers to  Kunde
---------------------------------
Every Powerofficego Customers will be synchronized with a  Kunde.

If a matching  Kunde already exists, the Powerofficego Customers will be merged with the existing one.
If no matching  Kunde is found, a new  Kunde will be created.

A Powerofficego Customers will merge with a  Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Kunde Property
   * - EmailAddress
     - Epost

Once a link between a Powerofficego Customers and a  Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Kunde:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Kunde Property
     -  Data Type
   * - EmailAddress
     - Epost
     - "string"
   * - Id
     - Id
     - "string"
   * - MailAddress.AddressLine1
     - Gateadresse
     - "string"
   * - MailAddress.AddressLine1
     - Leveringsadresse
     - "string"
   * - MailAddress.AddressLine1
     - Postadresse
     - "string"
   * - MailAddress.AddressLine2
     - Gateadresse
     - "string"
   * - MailAddress.AddressLine2
     - Leveringsadresse2
     - "string"
   * - MailAddress.AddressLine2
     - Postadresse
     - "string"
   * - MailAddress.City
     - LevPoststed
     - "string"
   * - MailAddress.City
     - Poststed
     - "string"
   * - MailAddress.ZipCode
     - LevPostNr
     - "string"
   * - MailAddress.ZipCode
     - Postnr
     - "string"
   * - Name
     - Navn
     - "string"
   * - Number
     - sesam_kundeId
     - "string"
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCodeDependant on having wd:Q11994066 in MailAddress.CountryCodeDependant on having wd:Q11994066 in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCode)
     - Organisasjonsnummer
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - sesam_kundeId
     - "string"
   * - PhoneNumber
     - Telefon
     - "string"
   * - WebsiteUrl
     - Url
     - "string"


Powerofficego Departments to  Avdeling
--------------------------------------
Every Powerofficego Departments will be synchronized with a  Avdeling.

Once a link between a Powerofficego Departments and a  Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Avdeling:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Avdeling Property
     -  Data Type
   * - Name
     - Navn
     - "string"


Powerofficego Employees to  Ansatt
----------------------------------
Every Powerofficego Employees will be synchronized with a  Ansatt.

If a matching  Ansatt already exists, the Powerofficego Employees will be merged with the existing one.
If no matching  Ansatt is found, a new  Ansatt will be created.

A Powerofficego Employees will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Ansatt Property
   * - Number
     - Id

Once a link between a Powerofficego Employees and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Ansatt Property
     -  Data Type
   * - DateOfBirth
     - Fodt
     - "string"
   * - DepartmentId
     - AvdelingId
     - "string"
   * - DepartmentId
     - Tittel
     - "string"
   * - EmailAddress
     - Epost
     - "string"
   * - FirstName
     - Fornavn
     - "string"
   * - JobTitle
     - AvdelingId
     - "string"
   * - JobTitle
     - Tittel
     - "string"
   * - LastName
     - Etternavn
     - "string"
   * - Number
     - Id
     - "string"
   * - Number
     - sesam_ansattId
     - "integer"
   * - PhoneNumber
     - Mobil
     - "string"


Powerofficego Projects to  Prosjekt
-----------------------------------
Every Powerofficego Projects will be synchronized with a  Prosjekt.

Once a link between a Powerofficego Projects and a  Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Prosjekt:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Prosjekt Property
     -  Data Type
   * - CustomerId
     - KundeId
     - "string"
   * - DepartmentId
     - AvdelingId
     - "string"
   * - EndDate
     - AvsluttetDato
     - "string"
   * - IsActive
     - Avsluttet
     - "string"
   * - IsInternal
     - Avsluttet
     - "string"
   * - IsInternal
     - InterntProsjekt
     - "string"
   * - Name
     - Navn
     - "string"
   * - ProjectManagerEmployeeId
     - AnsvarligId
     - "integer"
   * - StartDate
     - StartDato
     - "string"

