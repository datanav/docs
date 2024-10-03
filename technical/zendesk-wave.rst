========================
Zendesk to Wave Dataflow
========================

Generated: 2024-10-03 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Wave Customer
------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Wave Customer must be established.

A Zendesk Users will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Zendesk Users and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - name
     - name
     - N/A

