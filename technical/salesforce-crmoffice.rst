================================
Salesforce to Crmoffice Dataflow
================================

Generated: 2024-09-08 00:00:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Crmoffice Contacts
-----------------------------------------
Every Salesforce Customer will be synchronized with a Crmoffice Contacts.

Once a link between a Salesforce Customer and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type


Salesforce Product2 to Crmoffice Companies
------------------------------------------
Every Salesforce Product2 will be synchronized with a Crmoffice Companies.

Once a link between a Salesforce Product2 and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Salesforce Contact to Crmoffice Contacts
----------------------------------------
Every Salesforce Contact will be synchronized with a Crmoffice Contacts.

Once a link between a Salesforce Contact and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - MobilePhone
     - mobilePhone
     - "string"
   * - Phone
     - directPhone
     - "string"

