================================
Zendesk to Exact Online Dataflow
================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Exact Online Accounts
----------------------------------------------
Every Zendesk Organizations will be synchronized with a Exact Online Accounts.

Once a link between a Zendesk Organizations and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - name
     - Name
     - "string"


Zendesk Users to Exact Online Contacts
--------------------------------------
Every Zendesk Users will be synchronized with a Exact Online Contacts.

Once a link between a Zendesk Users and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - email
     - Email
     - "string"
   * - name
     - FullName
     - "string"

