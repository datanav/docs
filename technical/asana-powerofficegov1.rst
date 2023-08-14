=================================
Asana to PowerOfficeGov1 Dataflow
=================================

Generated: 2023-08-14 08:51:46

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to PowerOfficeGov1 Projects
------------------------------------------
Every Asana Projects will be synchronized with a PowerOfficeGov1 Projects.

Once a link between a Asana Projects and a PowerOfficeGov1 Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a PowerOfficeGov1 Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - PowerOfficeGov1 Projects Property
     - PowerOfficeGov1 Data Type
   * - completed
     - completed
     - "string"
   * - completed
     - current_status.gid
     - "string"
   * - completed
     - current_status.title
     - "string"
   * - completed_at
     - completed_at
     - "string"
   * - completed_by.gid
     - completed_by.gid
     - "string"
   * - created_at
     - created_at
     - "string"
   * - current_status.gid
     - completed
     - "string"
   * - current_status.gid
     - current_status.gid
     - "string"
   * - current_status.text
     - current_status.text
     - "string"
   * - current_status.title
     - completed
     - "string"
   * - current_status.title
     - current_status.title
     - "string"
   * - due_on
     - due_on
     - "string"
   * - members.gid
     - members.gid
     - "string"
   * - name
     - name
     - "string"
   * - owner.gid
     - owner.gid
     - "string"
   * - start_on
     - start_on
     - "string"
   * - team.gid
     - team.gid
     - "string"
   * - workspace.gid
     - workspace.gid
     - "string"


Asana Tasks to PowerOfficeGov1 Tasks
------------------------------------
Every Asana Tasks will be synchronized with a PowerOfficeGov1 Tasks.

Once a link between a Asana Tasks and a PowerOfficeGov1 Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a PowerOfficeGov1 Tasks:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - PowerOfficeGov1 Tasks Property
     - PowerOfficeGov1 Data Type
   * - assignee.gid
     - assignee.gid
     - "string"
   * - completed
     - completed
     - "string"
   * - completed_at
     - completed_at
     - "string"
   * - created_at
     - created_at
     - "string"
   * - due_on
     - due_on
     - "string"
   * - modified_at
     - modified_at
     - "string"
   * - name
     - name
     - "string"
   * - parent
     - parent
     - "string"
   * - projects.gid
     - projects.gid
     - "string"
   * - start_at
     - start_at
     - "string"
   * - workspace.gid
     - workspace.gid
     - "string"


Asana Teams to PowerOfficeGov1 Teams
------------------------------------
Every Asana Teams will be synchronized with a PowerOfficeGov1 Teams.

Once a link between a Asana Teams and a PowerOfficeGov1 Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a PowerOfficeGov1 Teams:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - PowerOfficeGov1 Teams Property
     - PowerOfficeGov1 Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - organization.gid
     - organization.gid
     - "string"
   * - permalink_url
     - permalink_url
     - "string"


Asana Users to PowerOfficeGov1 Employee
---------------------------------------
Every Asana Users will be synchronized with a PowerOfficeGov1 Employee.

Once a link between a Asana Users and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - email
     - email
     - "string"
   * - name
     - FirstName
     - "string"
   * - name
     - firstName
     - "string"


Asana Workspaces to PowerOfficeGov1 Companies
---------------------------------------------
Every Asana Workspaces will be synchronized with a PowerOfficeGov1 Companies.

Once a link between a Asana Workspaces and a PowerOfficeGov1 Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a PowerOfficeGov1 Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - PowerOfficeGov1 Companies Property
     - PowerOfficeGov1 Data Type
   * - name
     - Name
     - "string"


Asana Workspaces to PowerOfficeGov1 Workspaces
----------------------------------------------
Every Asana Workspaces will be synchronized with a PowerOfficeGov1 Workspaces.

Once a link between a Asana Workspaces and a PowerOfficeGov1 Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a PowerOfficeGov1 Workspaces:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - PowerOfficeGov1 Workspaces Property
     - PowerOfficeGov1 Data Type
   * - email_domains
     - email_domains
     - "string"
   * - name
     - name
     - "string"

