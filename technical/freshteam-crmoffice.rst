===============================
Freshteam to Crmoffice Dataflow
===============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Crmoffice Contacts
----------------------------------------
Every Freshteam Employee will be synchronized with a Crmoffice Contacts.

Once a link between a Freshteam Employee and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - first_name
     - givenName
     - "string"
   * - last_name
     - familyName
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - directPhone
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - mobilePhone
     - "string"

