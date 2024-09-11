=================================
CRMOffice to SuperOffice Dataflow
=================================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to Superoffice Person
----------------------------------------
Every CRMOffice Contacts will be synchronized with a Superoffice Person.

Once a link between a CRMOffice Contacts and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
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

