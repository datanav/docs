====================
Zendesk to  Dataflow
====================

Generated: 2024-08-29 11:00:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Accounts
----------------------------------
Every Zendesk Organizations will be synchronized with a  Accounts.

Once a link between a Zendesk Organizations and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Accounts Property
     -  Data Type


Zendesk Users to  Contacts
--------------------------
Every Zendesk Users will be synchronized with a  Contacts.

Once a link between a Zendesk Users and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contacts Property
     -  Data Type
   * - email
     - Email
     - "string"
   * - name
     - FullName
     - "string"

