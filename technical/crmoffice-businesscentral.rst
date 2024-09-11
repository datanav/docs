=====================================
CRMOffice to BusinessCentral Dataflow
=====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to BusinessCentral Contacts person
-----------------------------------------------------
Every CRMOffice Contacts will be synchronized with a BusinessCentral Contacts person.

Once a link between a CRMOffice Contacts and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - mobilePhone
     - mobilePhoneNumber
     - "string"

