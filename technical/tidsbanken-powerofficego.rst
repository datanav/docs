=====================================
Tidsbanken to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to PowerOffice Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOffice Contactperson must be established.

A Tidsbanken Ansatt will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Contactperson Property
   * - Epost
     - emailAddress
   * - Personnummer
     - SocialSecurityNumber

Once a link between a Tidsbanken Ansatt and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Tidsbanken Ansatt to PowerOffice Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOffice Customers person must be established.

A Tidsbanken Ansatt will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Customers person Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Ansatt and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Tidsbanken Ansatt to PowerOffice Employees
------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a PowerOffice Employees.

If a matching PowerOffice Employees already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching PowerOffice Employees is found, a new PowerOffice Employees will be created.

A Tidsbanken Ansatt will merge with a PowerOffice Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Employees Property
   * - Id
     - Number

Once a link between a Tidsbanken Ansatt and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
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


Tidsbanken Avdeling to PowerOffice Departments
----------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a PowerOffice Departments.

If a matching PowerOffice Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching PowerOffice Departments is found, a new PowerOffice Departments will be created.

A Tidsbanken Avdeling will merge with a PowerOffice Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOffice Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a PowerOffice Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a PowerOffice Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOffice Departments Property
     - PowerOffice Data Type
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


Tidsbanken Kunde to PowerOffice Customers
-----------------------------------------
Every Tidsbanken Kunde will be synchronized with a PowerOffice Customers.

If a matching PowerOffice Customers already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching PowerOffice Customers is found, a new PowerOffice Customers will be created.

A Tidsbanken Kunde will merge with a PowerOffice Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice Customers Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Kunde and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
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


Tidsbanken Prosjekt to PowerOffice Projects
-------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a PowerOffice Projects.

Once a link between a Tidsbanken Prosjekt and a PowerOffice Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a PowerOffice Projects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - PowerOffice Projects Property
     - PowerOffice Data Type
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

