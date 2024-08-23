====================
ZohoCRM to  Dataflow
====================

Generated: 2024-08-23 12:37:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to  Contacts
----------------------------
Every ZohoCRM Contact will be synchronized with a  Contacts.

Once a link between a ZohoCRM Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Contacts Property
     -  Data Type
   * - Account_Name.id
     - company.id
     - "string"
   * - First_Name
     - givenName
     - "string"
   * - Last_Name
     - familyName
     - "string"
   * - Mobile
     - mobilePhone
     - "string"
   * - Other_Phone
     - directPhone
     - "string"
   * - Phone
     - directPhone
     - "string"

