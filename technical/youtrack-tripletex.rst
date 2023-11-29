=====================
YouTrack to  Dataflow
=====================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to  Contact
--------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Contact must be established.

A YouTrack Users will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contact Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contact Property
     -  Data Type
   * - profile.email
     - email
     - "string"
   * - profile.email.email
     - email
     - "string"


YouTrack Users to  Employee
---------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Employee must be established.

A YouTrack Users will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Employee Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Employee:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Employee Property
     -  Data Type
   * - profile.email.email
     - email
     - "string"

