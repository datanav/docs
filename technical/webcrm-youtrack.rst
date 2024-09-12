===========================
WebCRM to Youtrack Dataflow
===========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Youtrack Groups
---------------------------------------
Every WebCRM Organisations will be synchronized with a Youtrack Groups.

Once a link between a WebCRM Organisations and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Youtrack Groups Property
     - Youtrack Data Type


WebCRM Users to Youtrack Users
------------------------------
Every WebCRM Users will be synchronized with a Youtrack Users.

Once a link between a WebCRM Users and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - UserEmail
     - profile.email.email
     - "string"

