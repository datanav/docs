====================
ZohoCRM to  Dataflow
====================

Generated: 2024-08-29 10:37:37

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
   * - Email
     - Email
     - "string"
   * - First_Name
     - FirstName
     - "string"
   * - Full_Name
     - FullName
     - "string"
   * - Last_Name
     - LastName
     - "string"
   * - Mailing_City
     - City
     - "string"
   * - Mailing_Country
     - Country
     - "string"
   * - Mobile
     - Mobile
     - "string"
   * - Other_City
     - City
     - "string"
   * - Other_Country
     - Country
     - "string"
   * - Other_Phone
     - Phone
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Secondary_Email
     - Email
     - "string"


ZohoCRM Contact to  Addresses
-----------------------------
Every ZohoCRM Contact will be synchronized with a  Addresses.

Once a link between a ZohoCRM Contact and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Addresses:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Addresses Property
     -  Data Type

