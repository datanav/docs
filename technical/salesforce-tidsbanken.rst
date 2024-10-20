=================================
Salesforce to Tidsbanken Dataflow
=================================

Generated: 2024-10-20 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Tidsbanken Kunde
---------------------------------------
Every Salesforce Customer will be synchronized with a Tidsbanken Kunde.

Once a link between a Salesforce Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type


Salesforce User to Tidsbanken Ansatt
------------------------------------
Every Salesforce User will be synchronized with a Tidsbanken Ansatt.

Once a link between a Salesforce User and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - City
     - Poststed
     - "string"
   * - Email
     - Epost
     - "string"
   * - EmployeeNumber
     - sesam_ansattId
     - "integer"
   * - FirstName
     - Fornavn
     - "string"
   * - ID
     - Id
     - "integer"
   * - LastName
     - Etternavn
     - "string"
   * - MobilePhone
     - Mobil
     - "string"
   * - Name
     - Navn
     - "string"
   * - PostalCode
     - Postnummer
     - "string"
   * - Street
     - Adresse
     - "string"
   * - Title
     - Tittel
     - "string"

