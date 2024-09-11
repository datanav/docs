====================================
Tidsbanken to PowerOfficeGO Dataflow
====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to PowerOfficeGO Contactperson
------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOfficeGO Contactperson must be established.

A Tidsbanken Ansatt will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Contactperson Property
   * - Epost
     - emailAddress
   * - Personnummer
     - SocialSecurityNumber

Once a link between a Tidsbanken Ansatt and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


Tidsbanken Ansatt to PowerOfficeGO Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOfficeGO Customers person must be established.

A Tidsbanken Ansatt will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Customers person Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Ansatt and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Tidsbanken Kunde to PowerOffice Customers person
------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into PowerOffice.

Once a link between a Tidsbanken Kunde and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type


Tidsbanken Ansatt to PowerOfficeGO Employees
--------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a PowerOfficeGO Employees.

If a matching PowerOfficeGO Employees already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching PowerOfficeGO Employees is found, a new PowerOfficeGO Employees will be created.

A Tidsbanken Ansatt will merge with a PowerOfficeGO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Employees Property
   * - Id
     - Number

Once a link between a Tidsbanken Ansatt and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
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


Tidsbanken Avdeling to PowerOfficeGO Departments
------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a PowerOfficeGO Departments.

If a matching PowerOfficeGO Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching PowerOfficeGO Departments is found, a new PowerOfficeGO Departments will be created.

A Tidsbanken Avdeling will merge with a PowerOfficeGO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOfficeGO Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a PowerOfficeGO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a PowerOfficeGO Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOfficeGO Departments Property
     - PowerOfficeGO Data Type
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


Tidsbanken Kunde to PowerOfficeGO Customers
-------------------------------------------
Every Tidsbanken Kunde will be synchronized with a PowerOfficeGO Customers.

If a matching PowerOfficeGO Customers already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching PowerOfficeGO Customers is found, a new PowerOfficeGO Customers will be created.

A Tidsbanken Kunde will merge with a PowerOfficeGO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOfficeGO Customers Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Kunde and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
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


Tidsbanken Prosjekt to PowerOfficeGO Projects
---------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a PowerOfficeGO Projects.

Once a link between a Tidsbanken Prosjekt and a PowerOfficeGO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a PowerOfficeGO Projects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - PowerOfficeGO Projects Property
     - PowerOfficeGO Data Type
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

