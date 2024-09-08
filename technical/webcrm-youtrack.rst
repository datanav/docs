===========================
Webcrm to Youtrack Dataflow
===========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Youtrack Groups
---------------------------------------
Every Webcrm Organisations will be synchronized with a Youtrack Groups.

Once a link between a Webcrm Organisations and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Youtrack Groups Property
     - Youtrack Data Type


Webcrm Users to Youtrack Users
------------------------------
Every Webcrm Users will be synchronized with a Youtrack Users.

Once a link between a Webcrm Users and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - UserEmail
     - profile.email.email
     - "string"

