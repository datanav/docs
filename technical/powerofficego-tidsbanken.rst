=====================================
PowerOffice GO to Tidsbanken Dataflow
=====================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Tidsbanken Ansatt
-------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tidsbanken Ansatt must be established.

A PowerOffice GO Contactperson will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tidsbanken Ansatt Property
   * - emailAddress
     - Epost
   * - SocialSecurityNumber
     - Personnummer

Once a link between a PowerOffice GO Contactperson and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
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


PowerOffice GO Customers person to Tidsbanken Ansatt
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tidsbanken Ansatt must be established.

A PowerOffice GO Customers person will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tidsbanken Ansatt Property
   * - EmailAddress
     - Epost

Once a link between a PowerOffice GO Customers person and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - DateOfBirth
     - Fodt
     - "string"
   * - FirstName
     - Fornavn
     - "string"
   * - Id
     - Id
     - "integer"
   * - LastName
     - Etternavn
     - "string"
   * - MailAddress.AddressLine1
     - Adresse
     - "string"
   * - MailAddress.City
     - Poststed
     - "string"
   * - MailAddress.ZipCode
     - Postnummer
     - "string"


PowerOffice GO Customers to Tidsbanken Kunde
--------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tidsbanken Kunde.

If a matching Tidsbanken Kunde already exists, the PowerOffice GO Customers will be merged with the existing one.
If no matching Tidsbanken Kunde is found, a new Tidsbanken Kunde will be created.

A PowerOffice GO Customers will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tidsbanken Kunde Property
   * - EmailAddress
     - Epost

Once a link between a PowerOffice GO Customers and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
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


PowerOffice GO Departments to Tidsbanken Avdeling
-------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Tidsbanken Avdeling.

If a matching Tidsbanken Avdeling already exists, the PowerOffice GO Departments will be merged with the existing one.
If no matching Tidsbanken Avdeling is found, a new Tidsbanken Avdeling will be created.

A PowerOffice GO Departments will merge with a Tidsbanken Avdeling if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tidsbanken Avdeling Property
   * - Code
     - Id

Once a link between a PowerOffice GO Departments and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type
   * - Code
     - sesam_avdelingId
     - "string"
   * - IsActive
     - Synlig
     - "string"
   * - Name
     - Navn
     - "string"


PowerOffice GO Employees to Tidsbanken Ansatt
---------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Tidsbanken Ansatt.

If a matching Tidsbanken Ansatt already exists, the PowerOffice GO Employees will be merged with the existing one.
If no matching Tidsbanken Ansatt is found, a new Tidsbanken Ansatt will be created.

A PowerOffice GO Employees will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tidsbanken Ansatt Property
   * - Number
     - Id

Once a link between a PowerOffice GO Employees and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
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
   * - IsArchived
     - Aktiv
     - "boolean"
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


PowerOffice GO Projects to Tidsbanken Prosjekt
----------------------------------------------
Every PowerOffice GO Projects will be synchronized with a Tidsbanken Prosjekt.

Once a link between a PowerOffice GO Projects and a Tidsbanken Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Tidsbanken Prosjekt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Tidsbanken Prosjekt Property
     - Tidsbanken Data Type
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

