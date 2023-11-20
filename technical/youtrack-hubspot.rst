============================
YouTrack to HubSpot Dataflow
============================

Generated: 2023-11-20 15:20:02

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to HubSpot Contact
---------------------------------
Every YouTrack Users will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the YouTrack Users will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A YouTrack Users will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - HubSpot Contact Property
   * - 
     - properties.email
   * - profile.email
     - properties.email
   * - profile.email.email
     - properties.email

Once a link between a YouTrack Users and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - profile.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.work_email
     - "string"


YouTrack Groups to HubSpot Company
----------------------------------
Every YouTrack Groups will be synchronized with a HubSpot Company.

Once a link between a YouTrack Groups and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


YouTrack Organizations to HubSpot Company
-----------------------------------------
Every YouTrack Organizations will be synchronized with a HubSpot Company.

Once a link between a YouTrack Organizations and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


YouTrack Usergroups to HubSpot Company
--------------------------------------
Every YouTrack Usergroups will be synchronized with a HubSpot Company.

Once a link between a YouTrack Usergroups and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


YouTrack Usersyoutrack to HubSpot Contact
-----------------------------------------
Every YouTrack Usersyoutrack will be synchronized with a HubSpot Contact.

Once a link between a YouTrack Usersyoutrack and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usersyoutrack and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Usersyoutrack Property
     - HubSpot Contact Property
     - HubSpot Data Type


YouTrack Workitems to HubSpot Company
-------------------------------------
Every YouTrack Workitems will be synchronized with a HubSpot Company.

Once a link between a YouTrack Workitems and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - date
     - properties.description
     - "string"
   * - updated
     - properties.name
     - "string"


YouTrack Users to HubSpot User
------------------------------
Every YouTrack Users will be synchronized with a HubSpot User.

Once a link between a YouTrack Users and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - HubSpot User Property
     - HubSpot Data Type

