=============================
SuperOffice to Asana Dataflow
=============================

Generated: 2023-06-29 22:03:37

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Asana Teams
----------------------------------
Every SuperOffice Contact will be synchronized with a Asana Teams.

Once a link between a SuperOffice Contact and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Asana Teams Property
     - Asana Data Type
   * - Domains
     - permalink_url
     - "string"
   * - Name
     - member_invite_management_access_level
     - "string"
   * - Name
     - name
     - "string"


SuperOffice Person to Asana Users
---------------------------------
Every SuperOffice Person will be synchronized with a Asana Users.

Once a link between a SuperOffice Person and a Asana Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Asana Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Asana Users Property
     - Asana Data Type
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - name
     - "string"


SuperOffice Project to Asana Projects
-------------------------------------
Every SuperOffice Project will be synchronized with a Asana Projects.

Once a link between a SuperOffice Project and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - Asana Projects Property
     - Asana Data Type


SuperOffice User to Asana Users
-------------------------------
Every SuperOffice User will be synchronized with a Asana Users.

Once a link between a SuperOffice User and a Asana Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Asana Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Asana Users Property
     - Asana Data Type
   * - firstName
     - name
     - "string"
   * - personEmail
     - email
     - "string"

