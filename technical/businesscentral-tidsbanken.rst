============================
Businesscentral to  Dataflow
============================

Generated: 2024-03-26 00:00:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Kunde
-------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Kunde.

Once a link between a Businesscentral Customers company and a  Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Kunde:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Kunde Property
     -  Data Type
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


Businesscentral Employees to  Ansatt
------------------------------------
Every Businesscentral Employees will be synchronized with a  Ansatt.

Once a link between a Businesscentral Employees and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Ansatt Property
     -  Data Type
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

