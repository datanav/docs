======================
Freshteam to  Dataflow
======================

Generated: 2024-08-27 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to  Contacts
-------------------------------
Every Freshteam Employee will be synchronized with a  Contacts.

Once a link between a Freshteam Employee and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Contacts Property
     -  Data Type
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

