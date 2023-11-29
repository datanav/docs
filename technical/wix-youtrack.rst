====================
Wix.com to  Dataflow
====================

Generated: 2023-11-29 23:36:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to YouTrack Users
----------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a YouTrack Users must be established.

A Wix.com Contacts will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - YouTrack Users Property
   * - primaryInfo.email
     - profile.email.email

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
Before any synchronization can take place, a link between a Wix.com Members and a YouTrack Users must be established.

A Wix.com Members will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - YouTrack Users Property
   * - loginEmail
     - profile.email.email

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

