=================================
CRMOffice to SuperOffice Dataflow
=================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to SuperOffice Person
----------------------------------------
Every CRMOffice Contacts will be synchronized with a SuperOffice Person.

Once a link between a CRMOffice Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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

