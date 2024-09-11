==================================
Tidsbanken to ExactOnline Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to ExactOnline Contacts
-----------------------------------------
Every Tidsbanken Ansatt will be synchronized with a ExactOnline Contacts.

Once a link between a Tidsbanken Ansatt and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Tidsbanken Avdeling to ExactOnline Accounts
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a ExactOnline Accounts.

Once a link between a Tidsbanken Avdeling and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


Tidsbanken Ansatt to ExactOnline Addresses
------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a ExactOnline Addresses.

Once a link between a Tidsbanken Ansatt and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to ExactOnline Employees
------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a ExactOnline Employees.

Once a link between a Tidsbanken Ansatt and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
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


Tidsbanken Avdeling to ExactOnline Departments
----------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a ExactOnline Departments.

If a matching ExactOnline Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching ExactOnline Departments is found, a new ExactOnline Departments will be created.

A Tidsbanken Avdeling will merge with a ExactOnline Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - ExactOnline Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a ExactOnline Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a ExactOnline Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - ExactOnline Departments Property
     - ExactOnline Data Type
   * - Id
     - Code
     - "string"
   * - sesam_avdelingId
     - Code
     - "string"


Tidsbanken Kunde to ExactOnline Accounts
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a ExactOnline Accounts.

Once a link between a Tidsbanken Kunde and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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

