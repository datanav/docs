=============================
YouTrack to YouTrack Dataflow
=============================

Generated: 2023-11-27 12:08:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Projects to YouTrack Hubprojects
-----------------------------------------
Every YouTrack Projects will be synchronized with a YouTrack Hubprojects.

If a matching YouTrack Hubprojects already exists, the YouTrack Projects will be merged with the existing one.
If no matching YouTrack Hubprojects is found, a new YouTrack Hubprojects will be created.

A YouTrack Projects will merge with a YouTrack Hubprojects if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Projects Property
     - YouTrack Hubprojects Property
   * - ringId
     - id

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
     - team.id
     - "string"
   * - createdBy.id
     - transitiveProjectRoles.id
     - "string"
   * - leader.id
     - owner.id
     - "string"
   * - leader.id
     - team.id
     - "string"
   * - leader.id
     - transitiveProjectRoles.id
     - "string"
   * - team.id
     - owner.id
     - "string"
   * - team.id
     - team.id
     - "string"
   * - team.id
     - transitiveProjectRoles.id
     - "string"


YouTrack Author to YouTrack Projectroles
----------------------------------------
Before any synchronization can take place, a link between a YouTrack Author and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Author if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Author and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Author and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Author Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Author to YouTrack Users
---------------------------------
Before any synchronization can take place, a link between a YouTrack Author and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Author if it is connected to a YouTrack Role, Team, Owner, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Author and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Author and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Author Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Created by to YouTrack Projectroles
--------------------------------------------
Before any synchronization can take place, a link between a YouTrack Created by and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Created by if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Created by and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Created by and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Created by Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Created by to YouTrack Users
-------------------------------------
Before any synchronization can take place, a link between a YouTrack Created by and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Created by if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Created by and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Created by and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Created by Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Creator to YouTrack Projectroles
-----------------------------------------
Before any synchronization can take place, a link between a YouTrack Creator and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Creator if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Creator and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Creator and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Creator Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Creator to YouTrack Users
----------------------------------
Before any synchronization can take place, a link between a YouTrack Creator and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Creator if it is connected to a YouTrack Role, Team, Owner, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Creator and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Creator and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Creator Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Leader to YouTrack Projectroles
----------------------------------------
Before any synchronization can take place, a link between a YouTrack Leader and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Leader if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Leader and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Leader and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Leader Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Leader to YouTrack Users
---------------------------------
Before any synchronization can take place, a link between a YouTrack Leader and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Leader if it is connected to a YouTrack Role, Team, Owner, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Leader and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Leader and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Leader Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Organization to YouTrack Usergroups
--------------------------------------------
Before any synchronization can take place, a link between a YouTrack Organization and a YouTrack Usergroups must be established.

A new YouTrack Usergroups will be created from a YouTrack Organization if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Organization and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organization and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - YouTrack Organization Property
     - YouTrack Usergroups Property
     - YouTrack Data Type


YouTrack Owner to YouTrack Projectroles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Owner and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Owner if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Owner and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Owner and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Owner Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Owner to YouTrack Users
--------------------------------
Before any synchronization can take place, a link between a YouTrack Owner and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Owner if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Owner and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Owner and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Owner Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Projectroles to YouTrack Roles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Projectroles and a YouTrack Roles must be established.

A new YouTrack Roles will be created from a YouTrack Projectroles if it is connected to a YouTrack Role, Team, Owner, Users, Author, Leader, Creator, Created by, or Usersyoutrack that is synchronized into YouTrack.

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

A new YouTrack Users will be created from a YouTrack Projectroles if it is connected to a YouTrack Role, Team, Owner, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Projectroles and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Role to YouTrack Projectroles
--------------------------------------
Before any synchronization can take place, a link between a YouTrack Role and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Role if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Role and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Role and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Role Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Roles to YouTrack Projectroles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Roles and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Roles if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Roles and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Team to YouTrack Projectroles
--------------------------------------
Before any synchronization can take place, a link between a YouTrack Team and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Team if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Team and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Team and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Team Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


YouTrack Team to YouTrack Users
-------------------------------
Before any synchronization can take place, a link between a YouTrack Team and a YouTrack Users must be established.

A new YouTrack Users will be created from a YouTrack Team if it is connected to a YouTrack Role, Team, Owner, Users, Author, Issues, Leader, Creator, Projects, Workitems, Created by, Projectroles, or Usersyoutrack that is synchronized into YouTrack.

Once a link between a YouTrack Team and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Team and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Team Property
     - YouTrack Users Property
     - YouTrack Data Type


YouTrack Users to YouTrack Projectroles
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a YouTrack Projectroles must be established.

A new YouTrack Projectroles will be created from a YouTrack Users if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

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

A new YouTrack Projectroles will be created from a YouTrack Usersyoutrack if it is connected to a YouTrack Issues, Projects, Workitems, or Projectroles that is synchronized into YouTrack.

Once a link between a YouTrack Usersyoutrack and a YouTrack Projectroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usersyoutrack and a YouTrack Projectroles:

.. list-table::
   :header-rows: 1

   * - YouTrack Usersyoutrack Property
     - YouTrack Projectroles Property
     - YouTrack Data Type


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
     - team.id
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

