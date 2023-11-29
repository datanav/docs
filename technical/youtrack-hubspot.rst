=====================
YouTrack to  Dataflow
=====================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


YouTrack Issues to  Ticket
--------------------------
Every YouTrack Issues will be synchronized with a  Ticket.

Once a link between a YouTrack Issues and a  Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Ticket:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Ticket Property
     -  Data Type
   * - reporter.id
     - properties.hubspot_owner_id
     - "string"


YouTrack Users to  User
-----------------------
Every YouTrack Users will be synchronized with a  User.

Once a link between a YouTrack Users and a  User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  User:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  User Property
     -  Data Type
   * - profile.email.email
     - email
     - "string"

