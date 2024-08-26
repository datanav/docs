=====================
YouTrack to  Dataflow
=====================

Generated: 2024-08-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to  Companies
-----------------------------
Before any synchronization can take place, a link between a YouTrack Groups and a  Companies must be established.

A new  Companies will be created from a YouTrack Groups if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into .

Once a link between a YouTrack Groups and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a  Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     -  Companies Property
     -  Data Type


YouTrack Organization to  Companies
-----------------------------------
Before any synchronization can take place, a link between a YouTrack Organization and a  Companies must be established.

A new  Companies will be created from a YouTrack Organization if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into .

Once a link between a YouTrack Organization and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organization and a  Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Organization Property
     -  Companies Property
     -  Data Type


YouTrack Usergroups to  Companies
---------------------------------
Before any synchronization can take place, a link between a YouTrack Usergroups and a  Companies must be established.

A new  Companies will be created from a YouTrack Usergroups if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into .

Once a link between a YouTrack Usergroups and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a  Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     -  Companies Property
     -  Data Type


YouTrack Hubprojects to  Activities
-----------------------------------
Every YouTrack Hubprojects will be synchronized with a  Activities.

Once a link between a YouTrack Hubprojects and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a  Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     -  Activities Property
     -  Data Type


YouTrack Issues to  Activities
------------------------------
Every YouTrack Issues will be synchronized with a  Activities.

Once a link between a YouTrack Issues and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Activities Property
     -  Data Type
   * - reporter.id
     - ownerId
     - "string"


YouTrack Projectroles to  Activities
------------------------------------
Every YouTrack Projectroles will be synchronized with a  Activities.

Once a link between a YouTrack Projectroles and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a  Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     -  Activities Property
     -  Data Type


YouTrack Users to  Contacts
---------------------------
Every YouTrack Users will be synchronized with a  Contacts.

Once a link between a YouTrack Users and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Contacts:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contacts Property
     -  Data Type


YouTrack Workitems to  Activities
---------------------------------
Every YouTrack Workitems will be synchronized with a  Activities.

Once a link between a YouTrack Workitems and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a  Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     -  Activities Property
     -  Data Type

