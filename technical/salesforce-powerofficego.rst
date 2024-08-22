====================================
Salesforce to Powerofficego Dataflow
====================================

Generated: 2024-08-22 13:34:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Powerofficego Contactperson
-------------------------------------------------
Every Salesforce Contact will be synchronized with a Powerofficego Contactperson.

Once a link between a Salesforce Contact and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - Birthdate
     - dateOfBirth
     - N/A
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"

