=================================
Crmoffice to Superoffice Dataflow
=================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Superoffice Person
----------------------------------------
Every Crmoffice Contacts will be synchronized with a Superoffice Person.

Once a link between a Crmoffice Contacts and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - directPhone
     - OfficePhones.Value
     - "string"
   * - familyName
     - Lastname
     - "string"
   * - givenName
     - Firstname
     - "string"
   * - mobilePhone
     - MobilePhones.Value
     - "string"

