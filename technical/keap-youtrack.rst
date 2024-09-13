=========================
Keap to Youtrack Dataflow
=========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Youtrack Groups
---------------------------------
Every Keap Companies will be synchronized with a Youtrack Groups.

Once a link between a Keap Companies and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Youtrack Groups Property
     - Youtrack Data Type


Keap Users to Youtrack Users
----------------------------
Every Keap Users will be synchronized with a Youtrack Users.

Once a link between a Keap Users and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email_address
     - profile.email.email
     - "string"

