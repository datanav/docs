=============================
Webcrm to Salesforce Dataflow
=============================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Persons to Salesforce Contact
------------------------------------
Every Webcrm Persons will be synchronized with a Salesforce Contact.

Once a link between a Webcrm Persons and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - PersonDirectPhone
     - Phone
     - "string"
   * - PersonFirstName
     - FirstName
     - "string"
   * - PersonLastName
     - LastName
     - "string"
   * - PersonMobilePhone
     - MobilePhone
     - "string"
   * - document_number
     - Birthdate
     - "string"


Webcrm Products to Salesforce Product2
--------------------------------------
Every Webcrm Products will be synchronized with a Salesforce Product2.

Once a link between a Webcrm Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type

