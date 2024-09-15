==============================
YouTrack to CRMOffice Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to CRMOffice Companies
--------------------------------------
Before any synchronization can take place, a link between a YouTrack Groups and a CRMOffice Companies must be established.

A new CRMOffice Companies will be created from a YouTrack Groups if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into CRMOffice.

Once a link between a YouTrack Groups and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


YouTrack Organization to CRMOffice Companies
--------------------------------------------
Before any synchronization can take place, a link between a YouTrack Organization and a CRMOffice Companies must be established.

A new CRMOffice Companies will be created from a YouTrack Organization if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into CRMOffice.

Once a link between a YouTrack Organization and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organization and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Organization Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


YouTrack Usergroups to CRMOffice Companies
------------------------------------------
Before any synchronization can take place, a link between a YouTrack Usergroups and a CRMOffice Companies must be established.

A new CRMOffice Companies will be created from a YouTrack Usergroups if it is connected to a YouTrack Issues, Workitems, Hubprojects, or Projectroles that is synchronized into CRMOffice.

Once a link between a YouTrack Usergroups and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


YouTrack Hubprojects to CRMOffice Activities
--------------------------------------------
Every YouTrack Hubprojects will be synchronized with a CRMOffice Activities.

Once a link between a YouTrack Hubprojects and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Hubprojects and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Hubprojects Property
     - CRMOffice Activities Property
     - CRMOffice Data Type


YouTrack Issues to CRMOffice Activities
---------------------------------------
Every YouTrack Issues will be synchronized with a CRMOffice Activities.

Once a link between a YouTrack Issues and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - reporter.id
     - ownerId
     - "string"


YouTrack Projectroles to CRMOffice Activities
---------------------------------------------
Every YouTrack Projectroles will be synchronized with a CRMOffice Activities.

Once a link between a YouTrack Projectroles and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - CRMOffice Activities Property
     - CRMOffice Data Type


YouTrack Users to CRMOffice Contacts
------------------------------------
Every YouTrack Users will be synchronized with a CRMOffice Contacts.

Once a link between a YouTrack Users and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type


YouTrack Workitems to CRMOffice Activities
------------------------------------------
Every YouTrack Workitems will be synchronized with a CRMOffice Activities.

Once a link between a YouTrack Workitems and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - CRMOffice Activities Property
     - CRMOffice Data Type

