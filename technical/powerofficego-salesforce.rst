====================================
Powerofficego to Salesforce Dataflow
====================================

Generated: 2024-08-22 13:34:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Salesforce Contact
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Contactperson and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - dateOfBirth
     - Birthdate
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


Powerofficego Suppliers person to Salesforce Contact
----------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Salesforce Contact.

Once a link between a Powerofficego Suppliers person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - DateOfBirth
     - Birthdate
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"

