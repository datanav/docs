======================
Tripletex to  Dataflow
======================

Generated: 2024-08-29 10:35:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Contacts
------------------------------
Every Tripletex Contact will be synchronized with a  Contacts.

Once a link between a Tripletex Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contacts Property
     -  Data Type
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"

