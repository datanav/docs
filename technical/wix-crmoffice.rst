====================
Wix.com to  Dataflow
====================

Generated: 2024-08-23 12:35:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Products to  Companies
------------------------------
Every Wix.com Products will be synchronized with a  Companies.

Once a link between a Wix.com Products and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Companies:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Companies Property
     -  Data Type


Wix.com Contacts to  Contacts
-----------------------------
Every Wix.com Contacts will be synchronized with a  Contacts.

Once a link between a Wix.com Contacts and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contacts Property
     -  Data Type
   * - info.name.first
     - givenName
     - "string"
   * - info.name.last
     - familyName
     - "string"
   * - primaryInfo.phone
     - directPhone
     - "string"

