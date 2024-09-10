=====================================
Crmoffice to Businesscentral Dataflow
=====================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Businesscentral Contacts person
-----------------------------------------------------
Every Crmoffice Contacts will be synchronized with a Businesscentral Contacts person.

Once a link between a Crmoffice Contacts and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - mobilePhone
     - mobilePhoneNumber
     - "string"

