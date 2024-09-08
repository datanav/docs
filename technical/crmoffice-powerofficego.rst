===================================
Crmoffice to Powerofficego Dataflow
===================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Powerofficego Contactperson
-------------------------------------------------
Every Crmoffice Contacts will be synchronized with a Powerofficego Contactperson.

Once a link between a Crmoffice Contacts and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"

