=============================
YouTrack to Youtrack Dataflow
=============================

Generated: 2024-09-23 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Hubprojects to Youtrack Hubprojects
--------------------------------------------
Before any synchronization can take place, a link between a YouTrack Hubprojects and a Youtrack Hubprojects must be established.

A YouTrack Hubprojects will merge with a Youtrack Hubprojects if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     - Youtrack Hubprojects Property
   * - id
     - id

Once a link between a YouTrack Hubprojects and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type
   * - organization.id
     - team.id
     - "string"
   * - owner.id
     - transitiveProjectRoles.id
     - "string"
   * - team.id
     - organization.id
     - "string"
   * - transitiveProjectRoles.id
     - owner.id
     - "string"


YouTrack Users to Youtrack Users
--------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Youtrack Users must be established.

A YouTrack Users will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Youtrack Users Property
   * - profile.email.email
     - profile.email.email

Once a link between a YouTrack Users and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - groups.id
     - teams.id
     - "string"
   * - groups.id
     - transitiveGroups.id
     - "string"
   * - groups.id
     - transitiveTeams.id
     - "string"
   * - organizationRoles.id
     - projectRoles.id
     - "string"
   * - organizationRoles.id
     - sourcedOrganizationRoles.id
     - "string"
   * - organizationRoles.id
     - sourcedProjectRoles.id
     - "string"
   * - organizationRoles.id
     - transitiveOrganizationRoles.id
     - "string"
   * - organizationRoles.id
     - transitiveProjectRoles.id
     - "string"
   * - projectRoles.id
     - organizationRoles.id
     - "string"
   * - projectRoles.id
     - sourcedOrganizationRoles.id
     - "string"
   * - projectRoles.id
     - sourcedProjectRoles.id
     - "string"
   * - projectRoles.id
     - transitiveOrganizationRoles.id
     - "string"
   * - projectRoles.id
     - transitiveProjectRoles.id
     - "string"
   * - sourcedOrganizationRoles.id
     - organizationRoles.id
     - "string"
   * - sourcedOrganizationRoles.id
     - projectRoles.id
     - "string"
   * - sourcedOrganizationRoles.id
     - sourcedProjectRoles.id
     - "string"
   * - sourcedOrganizationRoles.id
     - transitiveOrganizationRoles.id
     - "string"
   * - sourcedOrganizationRoles.id
     - transitiveProjectRoles.id
     - "string"
   * - sourcedProjectRoles.id
     - organizationRoles.id
     - "string"
   * - sourcedProjectRoles.id
     - projectRoles.id
     - "string"
   * - sourcedProjectRoles.id
     - sourcedOrganizationRoles.id
     - "string"
   * - sourcedProjectRoles.id
     - transitiveOrganizationRoles.id
     - "string"
   * - sourcedProjectRoles.id
     - transitiveProjectRoles.id
     - "string"
   * - teams.id
     - groups.id
     - "string"
   * - teams.id
     - transitiveGroups.id
     - "string"
   * - teams.id
     - transitiveTeams.id
     - "string"
   * - transitiveGroups.id
     - groups.id
     - "string"
   * - transitiveGroups.id
     - teams.id
     - "string"
   * - transitiveGroups.id
     - transitiveTeams.id
     - "string"
   * - transitiveOrganizationRoles.id
     - organizationRoles.id
     - "string"
   * - transitiveOrganizationRoles.id
     - projectRoles.id
     - "string"
   * - transitiveOrganizationRoles.id
     - sourcedOrganizationRoles.id
     - "string"
   * - transitiveOrganizationRoles.id
     - sourcedProjectRoles.id
     - "string"
   * - transitiveOrganizationRoles.id
     - transitiveProjectRoles.id
     - "string"
   * - transitiveProjectRoles.id
     - organizationRoles.id
     - "string"
   * - transitiveProjectRoles.id
     - projectRoles.id
     - "string"
   * - transitiveProjectRoles.id
     - sourcedOrganizationRoles.id
     - "string"
   * - transitiveProjectRoles.id
     - sourcedProjectRoles.id
     - "string"
   * - transitiveProjectRoles.id
     - transitiveOrganizationRoles.id
     - "string"
   * - transitiveTeams.id
     - groups.id
     - "string"
   * - transitiveTeams.id
     - teams.id
     - "string"
   * - transitiveTeams.id
     - transitiveGroups.id
     - "string"


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


YouTrack Issues to Youtrack Hubprojects
---------------------------------------
Every YouTrack Issues will be synchronized with a Youtrack Hubprojects.

Once a link between a YouTrack Issues and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type


YouTrack Organizations to Youtrack Groups
-----------------------------------------
Every YouTrack Organizations will be synchronized with a Youtrack Groups.

Once a link between a YouTrack Organizations and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Youtrack Groups Property
     - Youtrack Data Type


YouTrack Projectroles to Youtrack Hubprojects
---------------------------------------------
Every YouTrack Projectroles will be synchronized with a Youtrack Hubprojects.

Once a link between a YouTrack Projectroles and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type
   * - owner.id
     - owner.id
     - "string"
   * - owner.id
     - transitiveProjectRoles.id
     - "string"
   * - role.id
     - projectRoles.id
     - "string"


YouTrack Roles to Youtrack Organizationroles
--------------------------------------------
Every YouTrack Roles will be synchronized with a Youtrack Organizationroles.

Once a link between a YouTrack Roles and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


YouTrack Workitems to Youtrack Hubprojects
------------------------------------------
Every YouTrack Workitems will be synchronized with a Youtrack Hubprojects.

Once a link between a YouTrack Workitems and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type
   * - author.id
     - owner.id
     - "string"
   * - author.id
     - transitiveProjectRoles.id
     - "string"
   * - creator.id
     - owner.id
     - "string"
   * - creator.id
     - transitiveProjectRoles.id
     - "string"

