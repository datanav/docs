============================
Crmoffice to Webcrm Dataflow
============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Webcrm Persons
------------------------------------
Every Crmoffice Contacts will be synchronized with a Webcrm Persons.

Once a link between a Crmoffice Contacts and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - directPhone
     - PersonDirectPhone
     - "string"
   * - familyName
     - PersonLastName
     - "string"
   * - givenName
     - PersonFirstName
     - "string"
   * - mobilePhone
     - PersonMobilePhone
     - "string"

