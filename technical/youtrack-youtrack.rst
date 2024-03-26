=====================
YouTrack to  Dataflow
=====================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Hubprojects to  Hubprojects
------------------------------------
Before any synchronization can take place, a link between a YouTrack Hubprojects and a  Hubprojects must be established.

A YouTrack Hubprojects will merge with a  Hubprojects if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     -  Hubprojects Property
   * - id
     - id

Once a link between a YouTrack Hubprojects and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     -  Hubprojects Property
     -  Data Type
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


YouTrack Users to  Users
------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Users must be established.

A YouTrack Users will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Users Property
   * - profile.email.email
     - profile.email.email

Once a link between a YouTrack Users and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Users Property
     -  Data Type
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


YouTrack Groups to YouTrack Usergroups
--------------------------------------
Before any synchronization can take place, a link between a YouTrack Groups and a YouTrack Usergroups must be established.

A new YouTrack Usergroups will be created from a YouTrack Groups if it is connected to a YouTrack Issues, Projects, Workitems, Hubprojects, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Groups and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - YouTrack Usergroups Property
     - YouTrack Data Type


YouTrack Organization to YouTrack Usergroups
--------------------------------------------
Before any synchronization can take place, a link between a YouTrack Organization and a YouTrack Usergroups must be established.

A new YouTrack Usergroups will be created from a YouTrack Organization if it is connected to a YouTrack Issues, Projects, Workitems, Hubprojects, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Organization and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organization and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - YouTrack Organization Property
     - YouTrack Usergroups Property
     - YouTrack Data Type


YouTrack Organizationroles to YouTrack Projectroles
---------------------------------------------------
Before any synchronization can take place, a link between a YouTrack Organizationroles and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Organizationroles if it is connected to a YouTrack Team, Owner, Users, Author, Leader, Parent, Creator, Created by, Usergroups, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Organizationroles and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizationroles and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizationroles Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Projectroles to YouTrack Organizationroles
---------------------------------------------------
Before any synchronization can take place, a link between a YouTrack Projectroles and a YouTrack Organizationroles must be established.

A new YouTrack Organizationroles will be created from a YouTrack Projectroles if it is connected to a YouTrack Team, Owner, Users, Author, Leader, Parent, Creator, Created by, Usergroups, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Projectroles and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


YouTrack Projectroles to YouTrack Roles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Projectroles and a YouTrack Roles must be established.

A new YouTrack Roles will be created from a YouTrack Projectroles if it is connected to a YouTrack Role, Team, Owner, Roles, Users, Author, Leader, Creator, Created by, Usersyoutrack, or Organizationroles that is synchronized into YouTrack.

Once a link between a YouTrack Projectroles and a YouTrack Roles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a YouTrack Roles:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - YouTrack Roles Property
     - YouTrack Data Type


YouTrack Projectroles to YouTrack Users
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Projectroles and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Projectroles if it is connected to a YouTrack Role, Team, Owner, Roles, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Hubprojects, Projectroles, Usersyoutrack, or Organizationroles that is synchronized into YouTrack.

Once a link between a YouTrack Projectroles and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Roles to YouTrack Projectroles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Roles and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Roles if it is connected to a YouTrack Issues, Projects, Workitems, Hubprojects, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Roles and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Users to YouTrack Projectroles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Users if it is connected to a YouTrack Issues, Projects, Workitems, Hubprojects, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Users and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Usersyoutrack to YouTrack Projectroles
-----------------------------------------------
Before any synchronization can take place, a link between a YouTrack Usersyoutrack and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Usersyoutrack if it is connected to a YouTrack Issues, Projects, Workitems, Hubprojects, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Usersyoutrack and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usersyoutrack and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Usersyoutrack Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Usersyoutrack to YouTrack Users
----------------------------------------
Before any synchronization can take place, a link between a YouTrack Usersyoutrack and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Usersyoutrack if it is connected to a YouTrack Role, Team, Owner, Roles, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Hubprojects, Projectroles, Usersyoutrack, or Organizationroles that is synchronized into YouTrack.

Once a link between a YouTrack Usersyoutrack and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usersyoutrack and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Usersyoutrack Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Issues to  Hubprojects
-------------------------------
Every YouTrack Issues will be synchronized with a  Hubprojects.

Once a link between a YouTrack Issues and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Hubprojects Property
     -  Data Type
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
     - team.id
     - "string"
   * - reporter.id
     - transitiveProjectRoles.id
     - "string"
   * - subtasks.id
     - projectType.id
     - "string"


YouTrack Organizations to  Groups
---------------------------------
Every YouTrack Organizations will be synchronized with a  Groups.

Once a link between a YouTrack Organizations and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a  Groups:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     -  Groups Property
     -  Data Type
   * - name
     - name
     - "string"


YouTrack Projectroles to  Hubprojects
-------------------------------------
Every YouTrack Projectroles will be synchronized with a  Hubprojects.

Once a link between a YouTrack Projectroles and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     -  Hubprojects Property
     -  Data Type
   * - owner.id
     - owner.id
     - "string"
   * - owner.id
     - team.id
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


YouTrack Roles to  Organizationroles
------------------------------------
Every YouTrack Roles will be synchronized with a  Organizationroles.

Once a link between a YouTrack Roles and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     -  Organizationroles Property
     -  Data Type


YouTrack Usergroups to  Groups
------------------------------
Every YouTrack Usergroups will be synchronized with a  Groups.

Once a link between a YouTrack Usergroups and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a  Groups:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     -  Groups Property
     -  Data Type
   * - name
     - name
     - "string"


YouTrack Workitems to  Hubprojects
----------------------------------
Every YouTrack Workitems will be synchronized with a  Hubprojects.

Once a link between a YouTrack Workitems and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     -  Hubprojects Property
     -  Data Type
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
   * - updated
     - creationTime
     - "string"

