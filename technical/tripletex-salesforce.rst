================================
Tripletex to Salesforce Dataflow
================================

Generated: 2024-08-25 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Salesforce Organization
---------------------------------------------
Every Tripletex Customer will be synchronized with a Salesforce Organization.

Once a link between a Tripletex Customer and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"
   * - phoneNumber
     - Phone	
     - "string"


Tripletex Department to Salesforce Organization
-----------------------------------------------
Every Tripletex Department will be synchronized with a Salesforce Organization.

Once a link between a Tripletex Department and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Tripletex Contact to Salesforce Contact
---------------------------------------
Every Tripletex Contact will be synchronized with a Salesforce Contact.

Once a link between a Tripletex Contact and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - MobilePhone
     - "string"
   * - phoneNumberWork
     - HomePhone
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Product to Salesforce Product2
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Salesforce Product2.

Once a link between a Tripletex Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description	
     - "string"
   * - name
     - Name	
     - "string"

