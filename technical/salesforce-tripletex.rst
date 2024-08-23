================================
Salesforce to Tripletex Dataflow
================================

Generated: 2024-08-23 08:50:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Tripletex Contact
---------------------------------------
Every Salesforce Contact will be synchronized with a Tripletex Contact.

Once a link between a Salesforce Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Email
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - HomePhone
     - phoneNumberWork
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MobilePhone
     - phoneNumberMobile
     - N/A
   * - Phone
     - phoneNumberWork
     - "string"


Salesforce Product2 to Tripletex Product
----------------------------------------
Every Salesforce Product2 will be synchronized with a Tripletex Product.

Once a link between a Salesforce Product2 and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - Description	
     - description
     - "string"
   * - Name	
     - name
     - "string"

