===========================
YouTrack to Webcrm Dataflow
===========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to Webcrm Organisations
---------------------------------------
Every YouTrack Groups will be synchronized with a Webcrm Organisations.

Once a link between a YouTrack Groups and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Webcrm Organisations Property
     - Webcrm Data Type


YouTrack Organizations to Webcrm Organisations
----------------------------------------------
Every YouTrack Organizations will be synchronized with a Webcrm Organisations.

Once a link between a YouTrack Organizations and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - description
     - OrganisationCompanyDescription
     - "string"


YouTrack Usergroups to Webcrm Organisations
-------------------------------------------
Every YouTrack Usergroups will be synchronized with a Webcrm Organisations.

Once a link between a YouTrack Usergroups and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Webcrm Organisations Property
     - Webcrm Data Type


YouTrack Users to Webcrm Users
------------------------------
Every YouTrack Users will be synchronized with a Webcrm Users.

Once a link between a YouTrack Users and a Webcrm Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Webcrm Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Webcrm Users Property
     - Webcrm Data Type
   * - profile.email.email
     - UserEmail
     - "string"

