============================
Businesscentral to  Dataflow
============================

Generated: 2023-11-30 12:43:05

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contact person to  Contacts
-------------------------------------------
Every Businesscentral Contact person will be synchronized with a  Contacts.

Once a link between a Businesscentral Contact person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact person Property
     -  Contacts Property
     -  Data Type
   * - email
     - primaryInfo.email
     - "string"
   * - mobilePhoneNumber
     - primaryInfo.phone
     - "string"

