=====================
YouTrack to  Dataflow
=====================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to  Account
---------------------------
Every YouTrack Groups will be synchronized with a  Account.

Once a link between a YouTrack Groups and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a  Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     -  Account Property
     -  Data Type
   * - name
     - Account_Name
     - "string"


YouTrack Organizations to  Account
----------------------------------
Every YouTrack Organizations will be synchronized with a  Account.

Once a link between a YouTrack Organizations and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a  Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     -  Account Property
     -  Data Type
   * - description
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"


YouTrack Usergroups to  Account
-------------------------------
Every YouTrack Usergroups will be synchronized with a  Account.

Once a link between a YouTrack Usergroups and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a  Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     -  Account Property
     -  Data Type
   * - name
     - Account_Name
     - "string"

