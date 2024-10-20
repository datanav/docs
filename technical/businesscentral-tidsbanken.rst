=======================================
Business Central to Tidsbanken Dataflow
=======================================

Generated: 2024-10-20 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers (organisation data) to Tidsbanken Kunde
------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Tidsbanken Kunde.

Once a link between a Business Central Customers (organisation data) and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - addressLine1
     - Gateadresse
     - "string"
   * - addressLine1
     - Leveringsadresse
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


Business Central Customers (organisation data) to Tidsbanken Kunde
------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Tidsbanken Kunde.

Once a link between a Business Central Customers (organisation data) and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type


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
     - Navn
     - "string"
   * - email
     - Epost
     - "string"
   * - givenName
     - Fornavn
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

