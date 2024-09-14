======================================
CRMOffice to Business Central Dataflow
======================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to Business Central Contacts person
------------------------------------------------------
Every CRMOffice Contacts will be synchronized with a Business Central Contacts person.

Once a link between a CRMOffice Contacts and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - mobilePhone
     - mobilePhoneNumber
     - "string"

