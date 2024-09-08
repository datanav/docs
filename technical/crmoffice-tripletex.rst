===============================
Crmoffice to Tripletex Dataflow
===============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Tripletex Contact
---------------------------------------
Every Crmoffice Contacts will be synchronized with a Tripletex Contact.

Once a link between a Crmoffice Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - directPhone
     - phoneNumberWork
     - "string"
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"
   * - mobilePhone
     - phoneNumberMobile
     - N/A

