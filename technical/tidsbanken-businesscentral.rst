======================================
Tidsbanken to Businesscentral Dataflow
======================================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Businesscentral Companies
------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Businesscentral Companies.

Once a link between a Tidsbanken Avdeling and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Tidsbanken Kunde to Businesscentral Companies
---------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Businesscentral Companies.

Once a link between a Tidsbanken Kunde and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Tidsbanken Ansatt to Businesscentral Employees
----------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Businesscentral Employees.

Once a link between a Tidsbanken Ansatt and a Businesscentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Businesscentral Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Businesscentral Employees Property
     - Businesscentral Data Type
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


Tidsbanken Kunde to Businesscentral Customers company
-----------------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Businesscentral Customers company.

Once a link between a Tidsbanken Kunde and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
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

