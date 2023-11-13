=============================
YouTrack to YouTrack Dataflow
=============================

Generated: 2023-11-13 14:41:50

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Issues to YouTrack Hubprojects
---------------------------------------
Every YouTrack Issues will be synchronized with a YouTrack Hubprojects.

Once a link between a YouTrack Issues and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type
   * - attachments.id
     - owner.id
     - "string"
   * - attachments.id
     - projectRoles.id
     - "string"
   * - attachments.id
     - projectType.id
     - "string"
   * - attachments.id
     - resources.id
     - "string"
   * - attachments.id
     - team.id
     - "string"
   * - attachments.id
     - transitiveProjectRoles.id
     - "string"
   * - comments.id
     - owner.id
     - "string"
   * - comments.id
     - projectRoles.id
     - "string"
   * - comments.id
     - projectType.id
     - "string"
   * - comments.id
     - resources.id
     - "string"
   * - comments.id
     - team.id
     - "string"
   * - comments.id
     - transitiveProjectRoles.id
     - "string"
   * - created
     - creationTime
     - "string"
   * - externalIssue.id
     - projectType.id
     - "string"
   * - links.id
     - projectType.id
     - "string"
   * - parent.id
     - projectType.id
     - "string"
   * - project.id
     - projectType.id
     - "string"
   * - reporter.id
     - owner.id
     - "string"
   * - reporter.id
     - transitiveProjectRoles.id
     - "string"
   * - subtasks.id
     - projectType.id
     - "string"


YouTrack Organizations to YouTrack Groups
-----------------------------------------
Every YouTrack Organizations will be synchronized with a YouTrack Groups.

Once a link between a YouTrack Organizations and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


YouTrack Projectroles to YouTrack Hubprojects
---------------------------------------------
Every YouTrack Projectroles will be synchronized with a YouTrack Hubprojects.

Once a link between a YouTrack Projectroles and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type
   * - owner.id
     - owner.id
     - "string"
   * - owner.id
     - transitiveProjectRoles.id
     - "string"
   * - project.id
     - projectType.id
     - "string"
   * - role.id
     - projectRoles.id
     - "string"
   * - role.id
     - team.id
     - "string"


YouTrack Projects to YouTrack Hubprojects
-----------------------------------------
Every YouTrack Projects will be synchronized with a YouTrack Hubprojects.

Once a link between a YouTrack Projects and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projects and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projects Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type
   * - createdBy.id
     - owner.id
     - "string"
   * - createdBy.id
     - transitiveProjectRoles.id
     - "string"


YouTrack Roles to YouTrack Organizationroles
--------------------------------------------
Every YouTrack Roles will be synchronized with a YouTrack Organizationroles.

Once a link between a YouTrack Roles and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


YouTrack Usergroups to YouTrack Groups
--------------------------------------
Every YouTrack Usergroups will be synchronized with a YouTrack Groups.

Once a link between a YouTrack Usergroups and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


YouTrack Usergroups to YouTrack Organizationroles
-------------------------------------------------
Every YouTrack Usergroups will be synchronized with a YouTrack Organizationroles.

Once a link between a YouTrack Usergroups and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - name
     - id
     - "string"


YouTrack Usersyoutrack to YouTrack Users
----------------------------------------
Every YouTrack Usersyoutrack will be synchronized with a YouTrack Users.

Once a link between a YouTrack Usersyoutrack and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usersyoutrack and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Usersyoutrack Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Workitems to YouTrack Hubprojects
------------------------------------------
Every YouTrack Workitems will be synchronized with a YouTrack Hubprojects.

Once a link between a YouTrack Workitems and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type
   * - updated
     - creationTime
     - "string"

