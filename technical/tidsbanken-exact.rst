===================================
Tidsbanken to Exact Online Dataflow
===================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Exact Online Contacts
------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Online Contacts.

Once a link between a Tidsbanken Ansatt and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - Epost
     - BusinessEmail
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - BirthDate
     - "string"
   * - Fornavn
     - FirstName
     - "string"
   * - Mobil
     - Mobile
     - "string"
   * - Navn
     - FullName
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Avdeling to Exact Online Accounts
--------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Exact Online Accounts.

Once a link between a Tidsbanken Avdeling and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Navn
     - Name
     - "string"
   * - Postnr
     - Postcode
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to Exact Online Addresses
-------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Online Addresses.

Once a link between a Tidsbanken Ansatt and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to Exact Online Employees
-------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Online Employees.

Once a link between a Tidsbanken Ansatt and a Exact Online Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Online Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Online Employees Property
     - Exact Online Data Type
   * - Adresse
     - AddressStreet
     - "string"
   * - Epost
     - BusinessEmail
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - BirthDate
     - "string"
   * - Fornavn
     - FirstName
     - "string"
   * - Id
     - ID
     - "string"
   * - Mobil
     - BusinessMobile
     - "string"
   * - Postnummer
     - Postcode
     - "string"
   * - Poststed
     - City
     - "string"
   * - TlfPrivat
     - Mobile
     - "string"


Tidsbanken Avdeling to Exact Online Departments
-----------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Exact Online Departments.

If a matching Exact Online Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching Exact Online Departments is found, a new Exact Online Departments will be created.

A Tidsbanken Avdeling will merge with a Exact Online Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Online Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a Exact Online Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Exact Online Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Online Departments Property
     - Exact Online Data Type
   * - Id
     - Code
     - "string"
   * - sesam_avdelingId
     - Code
     - "string"


Tidsbanken Kunde to Exact Online Accounts
-----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Exact Online Accounts.

Once a link between a Tidsbanken Kunde and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - Gateadresse
     - AddressLine1
     - "string"
   * - LevPostNr
     - Postcode
     - "string"
   * - LevPoststed
     - City
     - "string"
   * - Leveringsadresse
     - AddressLine1
     - "string"
   * - Leveringsadresse2
     - AddressLine2
     - "string"
   * - Navn
     - Name
     - "string"
   * - Postadresse
     - AddressLine2
     - "string"
   * - Postnr
     - Postcode
     - "string"
   * - Poststed
     - City
     - "string"
   * - Telefon
     - Phone
     - "string"
   * - Url
     - Website
     - "string"

