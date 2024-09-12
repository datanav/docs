========================
Zendesk to Wave Dataflow
========================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Wave Customer person
-------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Wave Customer person must be established.

A Zendesk Users will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer person Property
   * - email
     - email

Once a link between a Zendesk Users and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer person Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - name
     - name
     - N/A

