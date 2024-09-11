====================================
CRMOffice to PowerOffice GO Dataflow
====================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to PowerOffice Contactperson
-----------------------------------------------
Every CRMOffice Contacts will be synchronized with a PowerOffice Contactperson.

Once a link between a CRMOffice Contacts and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"

