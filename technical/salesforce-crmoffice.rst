================================
Salesforce to CRMOffice Dataflow
================================

Generated: 2024-09-13 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to CRMOffice Contacts
-----------------------------------------
Every Salesforce Customer will be synchronized with a CRMOffice Contacts.

Once a link between a Salesforce Customer and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type


Salesforce Product2 to CRMOffice Companies
------------------------------------------
Every Salesforce Product2 will be synchronized with a CRMOffice Companies.

Once a link between a Salesforce Product2 and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Salesforce Seller to CRMOffice Contacts
---------------------------------------
Every Salesforce Seller will be synchronized with a CRMOffice Contacts.

Once a link between a Salesforce Seller and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type


Salesforce Task to CRMOffice Activities
---------------------------------------
Every Salesforce Task will be synchronized with a CRMOffice Activities.

Once a link between a Salesforce Task and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Task and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Salesforce Task Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - OwnerId
     - ownerId
     - "string"
   * - Subject
     - subject
     - "string"


Salesforce User to CRMOffice Contacts
-------------------------------------
Every Salesforce User will be synchronized with a CRMOffice Contacts.

Once a link between a Salesforce User and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - EmployeeNumber
     - company.id
     - "string"
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - MobilePhone
     - mobilePhone
     - "string"


Salesforce Contact to CRMOffice Contacts
----------------------------------------
Every Salesforce Contact will be synchronized with a CRMOffice Contacts.

Once a link between a Salesforce Contact and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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

