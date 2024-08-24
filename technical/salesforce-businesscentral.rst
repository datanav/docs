======================================
Salesforce to Businesscentral Dataflow
======================================

Generated: 2024-08-24 00:00:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to Businesscentral Companies
----------------------------------------------------
Every Salesforce Organization will be synchronized with a Businesscentral Companies.

Once a link between a Salesforce Organization and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Salesforce Contact to Businesscentral Contacts person
-----------------------------------------------------
Every Salesforce Contact will be synchronized with a Businesscentral Contacts person.

Once a link between a Salesforce Contact and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - Email
     - email
     - "string"
   * - HomePhone
     - phoneNumber
     - "string"
   * - MobilePhone
     - mobilePhoneNumber
     - "string"
   * - Phone
     - phoneNumber
     - "string"


Salesforce Product2 to Businesscentral Items
--------------------------------------------
Every Salesforce Product2 will be synchronized with a Businesscentral Items.

Once a link between a Salesforce Product2 and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - Name	
     - displayName
     - "string"

