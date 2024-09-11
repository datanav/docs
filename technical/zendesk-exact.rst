===============================
Zendesk to ExactOnline Dataflow
===============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to ExactOnline Accounts
---------------------------------------------
Every Zendesk Organizations will be synchronized with a ExactOnline Accounts.

Once a link between a Zendesk Organizations and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - name
     - Name
     - "string"


Zendesk Users to ExactOnline Contacts
-------------------------------------
Every Zendesk Users will be synchronized with a ExactOnline Contacts.

Once a link between a Zendesk Users and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
   * - email
     - Email
     - "string"
   * - name
     - FullName
     - "string"

