============================
Wix.com to YouTrack Dataflow
============================

Generated: 2023-11-16 13:55:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to YouTrack Users
----------------------------------
Every Wix.com Contacts will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the Wix.com Contacts will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A Wix.com Contacts will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - YouTrack Users Property
   * - primaryInfo.email
     - 
   * - primaryInfo.email
     - profile.email

Once a link between a Wix.com Contacts and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - primaryInfo.email
     - profile.email
     - "string"
   * - primaryInfo.email
     - profile.email.email
     - "string"


Wix.com Members to YouTrack Users
---------------------------------
Every Wix.com Members will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the Wix.com Members will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A Wix.com Members will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - YouTrack Users Property
   * - loginEmail
     - 
   * - loginEmail
     - profile.email

Once a link between a Wix.com Members and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - loginEmail
     - profile.email
     - "string"
   * - loginEmail
     - profile.email.email
     - "string"


Wix.com Contacts to YouTrack Usersyoutrack
------------------------------------------
Every Wix.com Contacts will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Wix.com Contacts and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


Wix.com Members to YouTrack Usersyoutrack
-----------------------------------------
Every Wix.com Members will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Wix.com Members and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type

