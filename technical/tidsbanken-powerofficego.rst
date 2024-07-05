====================================
Tidsbanken to Powerofficego Dataflow
====================================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Powerofficego Contactperson
------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Powerofficego Contactperson must be established.

A Tidsbanken Ansatt will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Contactperson Property
   * - Epost
     - emailAddress
   * - Personnummer
     - SocialSecurityNumber

Once a link between a Tidsbanken Ansatt and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - Adresse
     - address1
     - "string"
   * - Etternavn
     - lastName
     - "string"
   * - Fodt
     - dateOfBirth
     - N/A
   * - Fornavn
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
   * - Postnummer
     - zipCode
     - "string"
   * - Poststed
     - city
     - "string"


Tidsbanken Ansatt to Powerofficego Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Powerofficego Customers person must be established.

A Tidsbanken Ansatt will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Customers person Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Ansatt and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - Adresse
     - MailAddress.AddressLine1
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - DateOfBirth
     - N/A
   * - Fornavn
     - FirstName
     - "string"
   * - Id
     - Id
     - "integer"
   * - Postnummer
     - MailAddress.ZipCode
     - "string"
   * - Poststed
     - MailAddress.City
     - "string"


Tidsbanken Kunde to Powerofficego Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into Powerofficego.

Once a link between a Tidsbanken Kunde and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type


Tidsbanken Ansatt to Powerofficego Employees
--------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Powerofficego Employees.

If a matching Powerofficego Employees already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching Powerofficego Employees is found, a new Powerofficego Employees will be created.

A Tidsbanken Ansatt will merge with a Powerofficego Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Employees Property
   * - Id
     - Number

Once a link between a Tidsbanken Ansatt and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
   * - Aktiv
     - IsArchived
     - "boolean"
   * - AvdelingId
     - DepartmentId
     - "integer"
   * - Epost
     - EmailAddress
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - DateOfBirth
     - N/A
   * - Fornavn
     - FirstName
     - "string"
   * - Mobil
     - PhoneNumber
     - "string"
   * - Tittel
     - JobTitle
     - "string"
   * - sesam_ansattId
     - Number
     - "string"


Tidsbanken Avdeling to Powerofficego Departments
------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Powerofficego Departments.

If a matching Powerofficego Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching Powerofficego Departments is found, a new Powerofficego Departments will be created.

A Tidsbanken Avdeling will merge with a Powerofficego Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Powerofficego Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a Powerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Powerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Powerofficego Departments Property
     - Powerofficego Data Type
   * - Id
     - Code
     - "string"
   * - Navn
     - Name
     - "string"
   * - Synlig
     - IsActive
     - "string"
   * - sesam_avdelingId
     - Code
     - "string"


Tidsbanken Kunde to Powerofficego Customers
-------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Powerofficego Customers.

If a matching Powerofficego Customers already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching Powerofficego Customers is found, a new Powerofficego Customers will be created.

A Tidsbanken Kunde will merge with a Powerofficego Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Powerofficego Customers Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Kunde and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - Epost
     - EmailAddress
     - "string"
   * - Gateadresse
     - MailAddress.AddressLine1
     - "string"
   * - Id
     - Id
     - "integer"
   * - LevPostNr
     - MailAddress.ZipCode
     - "string"
   * - LevPoststed
     - MailAddress.City
     - "string"
   * - Leveringsadresse
     - MailAddress.AddressLine1
     - "string"
   * - Leveringsadresse2
     - MailAddress.AddressLine2
     - "string"
   * - Navn
     - Name
     - "string"
   * - Organisasjonsnummer
     - OrganizationNumber (Dependant on having NO in MailAddress.CountryCodeDependant on having wd:Q11994066 in MailAddress.CountryCode)
     - "string"
   * - Postadresse
     - MailAddress.AddressLine2
     - "string"
   * - Postnr
     - MailAddress.ZipCode
     - "string"
   * - Poststed
     - MailAddress.City
     - "string"
   * - Telefon
     - PhoneNumber
     - "string"
   * - Url
     - WebsiteUrl
     - "string"
   * - sesam_kundeId
     - Number
     - "string"
   * - sesam_kundeId
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"


Tidsbanken Prosjekt to Powerofficego Projects
---------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Powerofficego Projects.

Once a link between a Tidsbanken Prosjekt and a Powerofficego Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Powerofficego Projects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Powerofficego Projects Property
     - Powerofficego Data Type
   * - AnsvarligId
     - ProjectManagerEmployeeId
     - "integer"
   * - AvdelingId
     - DepartmentId
     - "integer"
   * - Avsluttet
     - IsActive
     - "string"
   * - AvsluttetDato
     - EndDate
     - N/A
   * - InterntProsjekt
     - IsInternal
     - "string"
   * - KundeId
     - CustomerId
     - "integer"
   * - Navn
     - Name
     - "string"
   * - StartDato
     - StartDate
     - N/A

