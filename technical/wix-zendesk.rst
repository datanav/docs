===========================
Wix.com to Zendesk Dataflow
===========================

Generated: 2023-09-05 08:36:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Zendesk Users
---------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Zendesk Users must be established.

A Wix.com Contacts will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Zendesk Users Property
   * - info.emails
     - email

Once a link between a Wix.com Contacts and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Zendesk Users Property
     - Zendesk Data Type

