======================================
Tidsbanken to BusinessCentral Dataflow
======================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to BusinessCentral Companies
------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a BusinessCentral Companies.

Once a link between a Tidsbanken Avdeling and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Tidsbanken Kunde to BusinessCentral Companies
---------------------------------------------
Every Tidsbanken Kunde will be synchronized with a BusinessCentral Companies.

Once a link between a Tidsbanken Kunde and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Tidsbanken Ansatt to BusinessCentral Employees
----------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a BusinessCentral Employees.

Once a link between a Tidsbanken Ansatt and a BusinessCentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a BusinessCentral Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - BusinessCentral Employees Property
     - BusinessCentral Data Type
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


Tidsbanken Kunde to BusinessCentral Customers company
-----------------------------------------------------
Every Tidsbanken Kunde will be synchronized with a BusinessCentral Customers company.

Once a link between a Tidsbanken Kunde and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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

