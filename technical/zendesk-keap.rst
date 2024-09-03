====================
Zendesk to  Dataflow
====================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Companies
-----------------------------------
Every Zendesk Organizations will be synchronized with a  Companies.

Once a link between a Zendesk Organizations and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Companies:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Companies Property
     -  Data Type
   * - name
     - company_name
     - "string"


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

