=====================================
PowerOffice GO to Tidsbanken Dataflow
=====================================

Generated: 2024-09-24 00:00:01

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
   * - zipCode
     - Postnummer
     - "string"


PowerOffice GO Customers to Tidsbanken Ansatt
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tidsbanken Ansatt must be established.

A PowerOffice GO Customers will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tidsbanken Ansatt Property
   * - EmailAddress
     - Epost

Once a link between a PowerOffice GO Customers and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tidsbanken Kunde must be established.

A new Tidsbanken Kunde will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-projects that is synchronized into Tidsbanken.

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
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - Organisasjonsnummer
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCode)
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
Before any synchronization can take place, a link between a PowerOffice GO Departments and a Tidsbanken Avdeling must be established.

A new Tidsbanken Avdeling will be created from a PowerOffice GO Departments if it is connected to a PowerOffice GO Powerofficego-projects, Powerofficego-employees, Powerofficego-contactperson, or Powerofficego-customers-person that is synchronized into Tidsbanken.

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
Before any synchronization can take place, a link between a PowerOffice GO Employees and a Tidsbanken Ansatt must be established.

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
     - Tittel
     - "string"
   * - LastName
     - Etternavn
     - "string"
   * - Number
     - sesam_ansattId
     - "integer"
   * - PhoneNumber
     - Mobil
     - "string"


PowerOffice GO Customers (organisation data) to Tidsbanken Kunde
----------------------------------------------------------------
Every PowerOffice GO Customers (organisation data) will be synchronized with a Tidsbanken Kunde.

Once a link between a PowerOffice GO Customers (organisation data) and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (organisation data) and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (organisation data) Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type


PowerOffice GO Customers to Tidsbanken Kunde
--------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tidsbanken Kunde.

Once a link between a PowerOffice GO Customers and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type


PowerOffice GO Departments to Tidsbanken Avdeling
-------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Tidsbanken Avdeling.

Once a link between a PowerOffice GO Departments and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type


PowerOffice GO Employees to Tidsbanken Ansatt
---------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Tidsbanken Ansatt.

Once a link between a PowerOffice GO Employees and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - EmailAddress
     - Epost
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
     - N/A
   * - IsActive
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
     - N/A

