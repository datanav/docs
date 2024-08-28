=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-28 12:21:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to  Organisations
-----------------------------------------
Every Salesforce Organization will be synchronized with a  Organisations.

Once a link between a Salesforce Organization and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Organisations Property
     -  Data Type
   * - Name	
     - OrganisationName
     - "string"
   * - Phone	
     - OrganisationTelephone
     - "string"


Salesforce Contact to  Persons
------------------------------
Every Salesforce Contact will be synchronized with a  Persons.

Once a link between a Salesforce Contact and a  Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Persons Property
     -  Data Type

