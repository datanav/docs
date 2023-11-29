====================
Zendesk to  Dataflow
====================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to  Users
-----------------------
Before any synchronization can take place, a link between a Zendesk Users and a  Users must be established.

A Zendesk Users will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Users Property
   * - email
     - email

Once a link between a Zendesk Users and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Users Property
     -  Data Type

