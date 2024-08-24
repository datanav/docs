====================================
Salesforce to Powerofficego Dataflow
====================================

Generated: 2024-08-24 00:00:36

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
   * - Email
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - HomePhone
     - phoneNumber
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Phone
     - phoneNumber
     - "string"


Salesforce Product2 to Powerofficego Product
--------------------------------------------
Every Salesforce Product2 will be synchronized with a Powerofficego Product.

Once a link between a Salesforce Product2 and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Powerofficego Product Property
     - Powerofficego Data Type
   * - Description	
     - description
     - "string"
   * - Name	
     - name
     - "string"

