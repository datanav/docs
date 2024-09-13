================================
CRMOffice to Salesforce Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Activities to Salesforce Task
---------------------------------------
Every CRMOffice Activities will be synchronized with a Salesforce Task.

Once a link between a CRMOffice Activities and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - ownerId
     - OwnerId
     - "string"
   * - subject
     - Subject
     - "string"


CRMOffice Companies to Salesforce Product2
------------------------------------------
Every CRMOffice Companies will be synchronized with a Salesforce Product2.

Once a link between a CRMOffice Companies and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Salesforce Product2 Property
     - Salesforce Data Type


CRMOffice Contacts to Salesforce Contact
----------------------------------------
Every CRMOffice Contacts will be synchronized with a Salesforce Contact.

Once a link between a CRMOffice Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - directPhone
     - Phone
     - "string"
   * - familyName
     - LastName
     - "string"
   * - givenName
     - FirstName
     - "string"
   * - mobilePhone
     - MobilePhone
     - "string"

