===========================
YouTrack to Trello Dataflow
===========================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Issues to  Cards
-------------------------
Before any synchronization can take place, a link between a YouTrack Issues and a  Cards must be established.

A new  Cards will be created from a YouTrack Issues if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into .

Once a link between a YouTrack Issues and a  Cards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Cards:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Cards Property
     -  Data Type


YouTrack Project to  Cards
--------------------------
Before any synchronization can take place, a link between a YouTrack Project and a  Cards must be established.

A new  Cards will be created from a YouTrack Project if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into .

Once a link between a YouTrack Project and a  Cards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Project and a  Cards:

.. list-table::
   :header-rows: 1

   * - YouTrack Project Property
     -  Cards Property
     -  Data Type


YouTrack Groups to  Organizations
---------------------------------
Every YouTrack Groups will be synchronized with a  Organizations.

Once a link between a YouTrack Groups and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a  Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     -  Organizations Property
     -  Data Type


YouTrack Hubprojects to  Actions
--------------------------------
Every YouTrack Hubprojects will be synchronized with a  Actions.

Once a link between a YouTrack Hubprojects and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a  Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     -  Actions Property
     -  Data Type


YouTrack Hubprojects to  Boards
-------------------------------
Every YouTrack Hubprojects will be synchronized with a  Boards.

Once a link between a YouTrack Hubprojects and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a  Boards:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     -  Boards Property
     -  Data Type


YouTrack Issues to  Actions
---------------------------
Every YouTrack Issues will be synchronized with a  Actions.

Once a link between a YouTrack Issues and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Actions Property
     -  Data Type
   * - project.id
     - data.card.id
     - "string"
   * - reporter.id
     - memberCreator.id
     - "string"


YouTrack Issues to  Boards
--------------------------
Every YouTrack Issues will be synchronized with a  Boards.

Once a link between a YouTrack Issues and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Boards:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Boards Property
     -  Data Type


YouTrack Organizations to  Organizations
----------------------------------------
Every YouTrack Organizations will be synchronized with a  Organizations.

Once a link between a YouTrack Organizations and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a  Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     -  Organizations Property
     -  Data Type
   * - description
     - desc
     - "string"


YouTrack Projectroles to  Actions
---------------------------------
Every YouTrack Projectroles will be synchronized with a  Actions.

Once a link between a YouTrack Projectroles and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a  Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     -  Actions Property
     -  Data Type


YouTrack Projectroles to  Boards
--------------------------------
Every YouTrack Projectroles will be synchronized with a  Boards.

Once a link between a YouTrack Projectroles and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a  Boards:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     -  Boards Property
     -  Data Type


YouTrack Usergroups to  Organizations
-------------------------------------
Every YouTrack Usergroups will be synchronized with a  Organizations.

Once a link between a YouTrack Usergroups and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a  Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     -  Organizations Property
     -  Data Type


YouTrack Users to  Members
--------------------------
Every YouTrack Users will be synchronized with a  Members.

Once a link between a YouTrack Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Members:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Members Property
     -  Data Type
   * - name
     - fullName
     - "string"


YouTrack Workitems to  Actions
------------------------------
Every YouTrack Workitems will be synchronized with a  Actions.

Once a link between a YouTrack Workitems and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a  Actions:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     -  Actions Property
     -  Data Type
   * - issue.id
     - data.card.id
     - "string"


YouTrack Workitems to  Boards
-----------------------------
Every YouTrack Workitems will be synchronized with a  Boards.

Once a link between a YouTrack Workitems and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a  Boards:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     -  Boards Property
     -  Data Type

