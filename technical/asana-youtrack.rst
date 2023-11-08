==========================
Asana to YouTrack Dataflow
==========================

Generated: 2023-11-08 14:31:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to YouTrack Organizationroles
--------------------------------------------
Every Asana Projects will be synchronized with a YouTrack Organizationroles.

Once a link between a Asana Projects and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - due_on
     - id
     - "string"
   * - members.gid
     - role.immutable
     - "string"


Asana Projects to YouTrack Usergroups
-------------------------------------
Every Asana Projects will be synchronized with a YouTrack Usergroups.

Once a link between a Asana Projects and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - due_on
     - name
     - "string"
   * - name
     - users.id
     - "string"


Asana Tasks to YouTrack Organizationroles
-----------------------------------------
Every Asana Tasks will be synchronized with a YouTrack Organizationroles.

Once a link between a Asana Tasks and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - due_on
     - id
     - "string"


Asana Tasks to YouTrack Usergroups
----------------------------------
Every Asana Tasks will be synchronized with a YouTrack Usergroups.

Once a link between a Asana Tasks and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - due_on
     - name
     - "string"
   * - name
     - users.id
     - "string"


Asana Teams to YouTrack Usergroups
----------------------------------
Every Asana Teams will be synchronized with a YouTrack Usergroups.

Once a link between a Asana Teams and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Asana Teams to YouTrack Workitems
---------------------------------
Every Asana Teams will be synchronized with a YouTrack Workitems.

Once a link between a Asana Teams and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - description
     - date
     - "string"
   * - name
     - updated
     - "string"


Asana Workspaces to YouTrack Usergroups
---------------------------------------
Every Asana Workspaces will be synchronized with a YouTrack Usergroups.

Once a link between a Asana Workspaces and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Asana Workspaces to YouTrack Workitems
--------------------------------------
Every Asana Workspaces will be synchronized with a YouTrack Workitems.

Once a link between a Asana Workspaces and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"


Asana Tasks to YouTrack Workitems
---------------------------------
Every Asana Tasks will be synchronized with a YouTrack Workitems.

Once a link between a Asana Tasks and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - workspace.gid
     - attributes.value
     - "string"

