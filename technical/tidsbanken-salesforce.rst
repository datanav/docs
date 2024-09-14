=================================
Tidsbanken to Salesforce Dataflow
=================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Salesforce Division
------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Salesforce Division.

Once a link between a Tidsbanken Avdeling and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Navn
     - Name
     - "string"
   * - Synlig
     - IsActive
     - "string"


Tidsbanken Kunde to Salesforce Division
---------------------------------------
Every Tidsbanken Kunde will be synchronized with a Salesforce Division.

Once a link between a Tidsbanken Kunde and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Navn
     - Name
     - "string"


Tidsbanken Prosjekt to Salesforce Task
--------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Salesforce Task.

Once a link between a Tidsbanken Prosjekt and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - AnsvarligId
     - OwnerId
     - "string"
   * - Avsluttet
     - IsClosed
     - "string"
   * - Navn
     - Subject
     - "string"


Tidsbanken Ansatt to Salesforce User
------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Salesforce User.

Once a link between a Tidsbanken Ansatt and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Salesforce User Property
     - Salesforce Data Type
   * - Adresse
     - Street
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fornavn
     - FirstName
     - "string"
   * - Id
     - ID
     - "string"
   * - Mobil
     - MobilePhone
     - "string"
   * - Navn
     - Name
     - "string"
   * - Postnummer
     - PostalCode
     - "string"
   * - Poststed
     - City
     - "string"
   * - Tittel
     - Title
     - "string"
   * - sesam_ansattId
     - EmployeeNumber
     - "string"

