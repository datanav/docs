=================================
Tidsbanken to Salesforce Dataflow
=================================

Generated: 2024-09-09 00:00:00

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

