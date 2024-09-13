=======================================
Business Central to Tidsbanken Dataflow
=======================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers company to Tidsbanken Kunde
------------------------------------------------------
Every Business Central Customers company will be synchronized with a Tidsbanken Kunde.

Once a link between a Business Central Customers company and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - addressLine1
     - Gateadresse
     - "string"
   * - addressLine1
     - Leveringsadresse
     - "string"
   * - addressLine1
     - Postadresse
     - "string"
   * - addressLine2
     - Gateadresse
     - "string"
   * - addressLine2
     - Leveringsadresse2
     - "string"
   * - addressLine2
     - Postadresse
     - "string"
   * - city
     - LevPoststed
     - "string"
   * - city
     - Poststed
     - "string"
   * - displayName
     - Navn
     - "string"
   * - id
     - Id
     - "string"
   * - phoneNumber
     - Telefon
     - "string"
   * - postalCode
     - LevPostNr
     - "string"
   * - postalCode
     - Postnr
     - "string"
   * - website
     - Url
     - "string"


Business Central Employees to Tidsbanken Ansatt
-----------------------------------------------
Every Business Central Employees will be synchronized with a Tidsbanken Ansatt.

Once a link between a Business Central Employees and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - birthDate
     - Fodt
     - "string"
   * - displayName
     - Etternavn
     - "string"
   * - displayName
     - Fornavn
     - "string"
   * - displayName
     - Navn
     - "string"
   * - email
     - Epost
     - "string"
   * - givenName
     - Etternavn
     - "string"
   * - givenName
     - Fornavn
     - "string"
   * - givenName
     - Navn
     - "string"
   * - jobTitle
     - AvdelingId
     - "string"
   * - jobTitle
     - Tittel
     - "string"
   * - mobilePhone
     - Mobil
     - "string"
   * - surname
     - Etternavn
     - "string"
   * - surname
     - Fornavn
     - "string"
   * - surname
     - Navn
     - "string"

