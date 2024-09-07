=============================
ZohoCRM to Crmoffice Dataflow
=============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Crmoffice Contacts
-------------------------------------
Every ZohoCRM Contact will be synchronized with a Crmoffice Contacts.

Once a link between a ZohoCRM Contact and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
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

