============================
YouTrack to ZohoCRM Dataflow
============================

Generated: 2024-07-02 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to ZohoCRM Account
----------------------------------
Every YouTrack Groups will be synchronized with a ZohoCRM Account.

Once a link between a YouTrack Groups and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"


YouTrack Organizations to ZohoCRM Account
-----------------------------------------
Every YouTrack Organizations will be synchronized with a ZohoCRM Account.

Once a link between a YouTrack Organizations and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - description
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"


YouTrack Usergroups to ZohoCRM Account
--------------------------------------
Every YouTrack Usergroups will be synchronized with a ZohoCRM Account.

Once a link between a YouTrack Usergroups and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

