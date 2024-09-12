=======================
Zendesk to Wix Dataflow
=======================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Wix Contacts
-----------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Wix Contacts must be established.

A Zendesk Users will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Zendesk Users and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - name
     - info.name.first
     - "string"
   * - name
     - info.name.last
     - "string"

