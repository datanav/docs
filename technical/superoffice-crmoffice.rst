========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-24 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to  Contacts
-------------------------------
Every SuperOffice Person will be synchronized with a  Contacts.

Once a link between a SuperOffice Person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contacts Property
     -  Data Type
   * - Firstname
     - givenName
     - "string"
   * - Lastname
     - familyName
     - "string"
   * - MobilePhones.Value
     - mobilePhone
     - "string"
   * - OfficePhones.Value
     - directPhone
     - "string"


SuperOffice Product to  Companies
---------------------------------
Every SuperOffice Product will be synchronized with a  Companies.

Once a link between a SuperOffice Product and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Companies Property
     -  Data Type

