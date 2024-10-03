===========================
YouTrack to Trello Dataflow
===========================

Generated: 2024-10-03 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to Trello Organizations
---------------------------------------
Every YouTrack Groups will be synchronized with a Trello Organizations.

Once a link between a YouTrack Groups and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Trello Organizations Property
     - Trello Data Type


YouTrack Hubprojects to Trello Actions
--------------------------------------
Every YouTrack Hubprojects will be synchronized with a Trello Actions.

Once a link between a YouTrack Hubprojects and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     - Trello Actions Property
     - Trello Data Type


YouTrack Issues to Trello Actions
---------------------------------
Every YouTrack Issues will be synchronized with a Trello Actions.

Once a link between a YouTrack Issues and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     - Trello Actions Property
     - Trello Data Type
   * - project.id
     - data.card.id
     - "string"
   * - reporter.id
     - memberCreator.id
     - "string"


YouTrack Organizations to Trello Organizations
----------------------------------------------
Every YouTrack Organizations will be synchronized with a Trello Organizations.

Once a link between a YouTrack Organizations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Trello Organizations Property
     - Trello Data Type
   * - description
     - desc
     - "string"


YouTrack Projectroles to Trello Actions
---------------------------------------
Every YouTrack Projectroles will be synchronized with a Trello Actions.

Once a link between a YouTrack Projectroles and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - Trello Actions Property
     - Trello Data Type


YouTrack Usergroups to Trello Organizations
-------------------------------------------
Every YouTrack Usergroups will be synchronized with a Trello Organizations.

Once a link between a YouTrack Usergroups and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Trello Organizations Property
     - Trello Data Type


YouTrack Users to Trello Members
--------------------------------
Every YouTrack Users will be synchronized with a Trello Members.

Once a link between a YouTrack Users and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Trello Members:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Trello Members Property
     - Trello Data Type
   * - name
     - fullName
     - "string"
   * - profile.email.email
     - email
     - "string"


YouTrack Workitems to Trello Actions
------------------------------------
Every YouTrack Workitems will be synchronized with a Trello Actions.

Once a link between a YouTrack Workitems and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - Trello Actions Property
     - Trello Data Type
   * - issue.id
     - data.card.id
     - "string"

