=============================
YouTrack to YouTrack Dataflow
=============================

Generated: 2023-11-10 01:45:16

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
   * - created
     - creationTime
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

