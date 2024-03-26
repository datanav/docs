=====================
YouTrack to  Dataflow
=====================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to  Contact
--------------------------
Every YouTrack Users will be synchronized with a  Contact.

If a matching  Contact already exists, the YouTrack Users will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A YouTrack Users will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contact Property
   * - profile.email.email
     - properties.email

Once a link between a YouTrack Users and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contact Property
     -  Data Type
   * - profile.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.work_email
     - "string"


YouTrack Groups to  Company
---------------------------
Every YouTrack Groups will be synchronized with a  Company.

Once a link between a YouTrack Groups and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a  Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     -  Company Property
     -  Data Type
   * - name
     - properties.name
     - "string"


YouTrack Organizations to  Company
----------------------------------
Every YouTrack Organizations will be synchronized with a  Company.

Once a link between a YouTrack Organizations and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a  Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     -  Company Property
     -  Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


YouTrack Usergroups to  Company
-------------------------------
Every YouTrack Usergroups will be synchronized with a  Company.

Once a link between a YouTrack Usergroups and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a  Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     -  Company Property
     -  Data Type
   * - name
     - properties.name
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

