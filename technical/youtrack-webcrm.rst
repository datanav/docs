===========================
YouTrack to WebCRM Dataflow
===========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to WebCRM Organisations
---------------------------------------
Every YouTrack Groups will be synchronized with a WebCRM Organisations.

Once a link between a YouTrack Groups and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - WebCRM Organisations Property
     - WebCRM Data Type


YouTrack Organizations to WebCRM Organisations
----------------------------------------------
Every YouTrack Organizations will be synchronized with a WebCRM Organisations.

Once a link between a YouTrack Organizations and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - description
     - OrganisationCompanyDescription
     - "string"


YouTrack Usergroups to WebCRM Organisations
-------------------------------------------
Every YouTrack Usergroups will be synchronized with a WebCRM Organisations.

Once a link between a YouTrack Usergroups and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - WebCRM Organisations Property
     - WebCRM Data Type


YouTrack Users to WebCRM Users
------------------------------
Every YouTrack Users will be synchronized with a WebCRM Users.

Once a link between a YouTrack Users and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - WebCRM Users Property
     - WebCRM Data Type
   * - profile.email.email
     - UserEmail
     - "string"

