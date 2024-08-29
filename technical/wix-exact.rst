====================
Wix.com to  Dataflow
====================

Generated: 2024-08-29 12:11:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - Email
     - "string"
   * - primaryInfo.phone
     - Phone
     - "string"


Wix.com Currencies to  Currencies
---------------------------------
Every Wix.com Currencies will be synchronized with a  Currencies.

Once a link between a Wix.com Currencies and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     -  Currencies Property
     -  Data Type

