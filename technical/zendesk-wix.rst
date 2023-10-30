=======================
Zendesk to Wix Dataflow
=======================

Generated: 2023-10-30 16:24:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Wix Contacts
-----------------------------
Every Zendesk Users will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Zendesk Users will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Zendesk Users will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wix Contacts Property
   * - email
     - info.emails
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


Zendesk Users to Wix Members
----------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Wix Members must be established.

A Zendesk Users will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Zendesk Users and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"

