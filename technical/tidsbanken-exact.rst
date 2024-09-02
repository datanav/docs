=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-09-02 10:42:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to  Contacts
------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Contacts.

Once a link between a Tidsbanken Ansatt and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Contacts Property
     -  Data Type
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


Tidsbanken Avdeling to  Accounts
--------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Accounts.

Once a link between a Tidsbanken Avdeling and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Accounts Property
     -  Data Type
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


Tidsbanken Ansatt to  Addresses
-------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Addresses.

Once a link between a Tidsbanken Ansatt and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Addresses Property
     -  Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to  Employees
-------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Employees.

Once a link between a Tidsbanken Ansatt and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Employees Property
     -  Data Type
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


Tidsbanken Avdeling to  Departments
-----------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Departments.

If a matching  Departments already exists, the Tidsbanken Avdeling will be merged with the existing one.
If no matching  Departments is found, a new  Departments will be created.

A Tidsbanken Avdeling will merge with a  Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Departments Property
     -  Data Type
   * - Id
     - Code
     - "string"
   * - sesam_avdelingId
     - Code
     - "string"


Tidsbanken Kunde to  Accounts
-----------------------------
Every Tidsbanken Kunde will be synchronized with a  Accounts.

Once a link between a Tidsbanken Kunde and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Accounts Property
     -  Data Type
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

