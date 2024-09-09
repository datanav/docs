============================
Tidsbanken to Exact Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Exact Contacts
-----------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Contacts.

Once a link between a Tidsbanken Ansatt and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Contacts Property
     - Exact Data Type
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


Tidsbanken Avdeling to Exact Accounts
-------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Exact Accounts.

Once a link between a Tidsbanken Avdeling and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Accounts Property
     - Exact Data Type
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


Tidsbanken Ansatt to Exact Addresses
------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Addresses.

Once a link between a Tidsbanken Ansatt and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Addresses Property
     - Exact Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to Exact Employees
------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Exact Employees.

Once a link between a Tidsbanken Ansatt and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Exact Employees Property
     - Exact Data Type
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


Tidsbanken Avdeling to Exact Departments
----------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Exact Departments.

If a matching Exact Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching Exact Departments is found, a new Exact Departments will be created.

A Tidsbanken Avdeling will merge with a Exact Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a Exact Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Exact Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Exact Departments Property
     - Exact Data Type
   * - Id
     - Code
     - "string"
   * - sesam_avdelingId
     - Code
     - "string"


Tidsbanken Kunde to Exact Accounts
----------------------------------
Every Tidsbanken Kunde will be synchronized with a Exact Accounts.

Once a link between a Tidsbanken Kunde and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Exact Accounts Property
     - Exact Data Type
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

