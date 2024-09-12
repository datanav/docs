==========================
Zendesk to WebCRM Dataflow
==========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to WebCRM Organisations
---------------------------------------------
Every Zendesk Organizations will be synchronized with a WebCRM Organisations.

Once a link between a Zendesk Organizations and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"


Zendesk Users to WebCRM Users
-----------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a WebCRM Users.

Once a link between a Zendesk Users and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - WebCRM Users Property
     - WebCRM Data Type

