=======================================
Tidsbanken to Business Central Dataflow
=======================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Business Central Companies
-------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Business Central Companies.

Once a link between a Tidsbanken Avdeling and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Business Central Companies Property
     - Business Central Data Type


Tidsbanken Kunde to Business Central Companies
----------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Business Central Companies.

Once a link between a Tidsbanken Kunde and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Business Central Companies Property
     - Business Central Data Type


Tidsbanken Ansatt to Business Central Employees
-----------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Business Central Employees.

Once a link between a Tidsbanken Ansatt and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Business Central Employees Property
     - Business Central Data Type
   * - Adresse
     - addressLine1
     - "string"
   * - Epost
     - email
     - "string"
   * - Etternavn
     - surname
     - "string"
   * - Fodt
     - birthDate
     - "string"
   * - Fornavn
     - givenName
     - "string"
   * - Id
     - id
     - "string"
   * - Mobil
     - mobilePhone
     - "string"
   * - Navn
     - displayName
     - "string"
   * - Postnummer
     - postalCode
     - "string"
   * - Poststed
     - city
     - "string"
   * - Tittel
     - jobTitle
     - "string"


Tidsbanken Kunde to Business Central Customers company
------------------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Business Central Customers company.

Once a link between a Tidsbanken Kunde and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Business Central Customers company Property
     - Business Central Data Type
   * - Gateadresse
     - addressLine1
     - "string"
   * - Id
     - id
     - "string"
   * - LevPostNr
     - postalCode
     - "string"
   * - LevPoststed
     - city
     - "string"
   * - Leveringsadresse
     - addressLine1
     - "string"
   * - Leveringsadresse2
     - addressLine2
     - "string"
   * - Navn
     - displayName
     - "string"
   * - Postadresse
     - addressLine2
     - "string"
   * - Postnr
     - postalCode
     - "string"
   * - Poststed
     - city
     - "string"
   * - Telefon
     - phoneNumber
     - "string"
   * - Url
     - website
     - "string"

