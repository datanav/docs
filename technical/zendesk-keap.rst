========================
Zendesk to Keap Dataflow
========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Keap Companies
---------------------------------------
Every Zendesk Organizations will be synchronized with a Keap Companies.

Once a link between a Zendesk Organizations and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Zendesk Users to Keap Contacts
------------------------------
Every Zendesk Users will be synchronized with a Keap Contacts.

Once a link between a Zendesk Users and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Keap Contacts Property
     - Keap Data Type

