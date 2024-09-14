=============================
ZohoCRM to CRMOffice Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to CRMOffice Contacts
-------------------------------------
Every ZohoCRM Contact will be synchronized with a CRMOffice Contacts.

Once a link between a ZohoCRM Contact and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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

