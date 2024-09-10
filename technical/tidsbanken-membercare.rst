=================================
Tidsbanken to Membercare Dataflow
=================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Membercare Persons
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Membercare Persons.

Once a link between a Tidsbanken Ansatt and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Membercare Persons Property
     - Membercare Data Type
   * - Epost
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - Etternavn
     - lastname
     - "string"
   * - Fodt
     - birthDate
     - "string"
   * - Fornavn
     - firstname
     - "string"
   * - Id
     - addresses.id
     - "string"
   * - Id
     - socialSecurityNumber.number (Dependant on having wd:Q36218176 in socialSecurityNumber.iso2Letter)
     - "string"
   * - Navn
     - name
     - "string"
   * - Personnummer
     - socialSecurityNumber.number (Dependant on having wd:Q1140371 in socialSecurityNumber.iso2Letter)
     - "string"
   * - Postnummer
     - addresses.postalCode.zipCode
     - "string"
   * - Poststed
     - addresses.postalCode.city
     - "string"


Tidsbanken Avdeling to Membercare Companies
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Membercare Companies.

Once a link between a Tidsbanken Avdeling and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Navn
     - companyName
     - "string"


Tidsbanken Kunde to Membercare Companies
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Membercare Companies.

Once a link between a Tidsbanken Kunde and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Navn
     - companyName
     - "string"
   * - Url
     - url
     - "string"

