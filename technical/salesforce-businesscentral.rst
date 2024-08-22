======================================
Salesforce to Businesscentral Dataflow
======================================

Generated: 2024-08-22 14:35:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

