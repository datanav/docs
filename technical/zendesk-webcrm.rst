====================
Zendesk to  Dataflow
====================

Generated: 2024-08-29 08:00:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Organisations
---------------------------------------
Every Zendesk Organizations will be synchronized with a  Organisations.

Once a link between a Zendesk Organizations and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Organisations Property
     -  Data Type
   * - name
     - OrganisationName
     - "string"


Zendesk Users to  Users
-----------------------
When a Zendesk User is of type Agent, it  will be synchronized with a  Users.

Once a link between a Zendesk Users and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Users Property
     -  Data Type

