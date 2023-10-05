===========================
Wix.com to Zendesk Dataflow
===========================

Generated: 2023-10-05 06:14:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Zendesk Users
---------------------------------
Every Wix.com Contacts will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the Wix.com Contacts will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A Wix.com Contacts will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Zendesk Users Property
   * - info.emails
     - email
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - info.emails
     - email
     - "string"


Wix.com Members to Zendesk Users
--------------------------------
Every Wix.com Members will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the Wix.com Members will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A Wix.com Members will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Zendesk Users Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Zendesk Users Property
     - Zendesk Data Type

