=====================
YouTrack to  Dataflow
=====================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to  Contacts
---------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Contacts must be established.

A YouTrack Users will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contacts Property
   * - profile.email.email
     - primaryInfo.email

Once a link between a YouTrack Users and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Contacts:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Contacts Property
     -  Data Type
   * - profile.email
     - primaryInfo.email
     - "string"
   * - profile.email.email
     - primaryInfo.email
     - "string"


YouTrack Users to  Members
--------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Members must be established.

A YouTrack Users will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Members Property
   * - profile.email.email
     - loginEmail

Once a link between a YouTrack Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Members:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Members Property
     -  Data Type
   * - profile.email
     - loginEmail
     - "string"
   * - profile.email.email
     - loginEmail
     - "string"

