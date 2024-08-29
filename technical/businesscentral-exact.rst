============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-29 10:26:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Contacts
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contacts.

Once a link between a Businesscentral Contacts person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts Property
     -  Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - FullName
     - "string"
   * - email
     - Email
     - "string"

