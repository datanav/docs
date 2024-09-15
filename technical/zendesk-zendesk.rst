===========================
Zendesk to Zendesk Dataflow
===========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Zendesk Users
------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Zendesk Users must be established.

A Zendesk Users will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Zendesk Users and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Zendesk Users Property
     - Zendesk Data Type

