===========================
Tripletex to Asana Dataflow
===========================

Generated: 2023-08-17 08:57:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Asana Teams
---------------------------------
Every Tripletex Customer will be synchronized with a Asana Teams.

Once a link between a Tripletex Customer and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Asana Teams Property
     - Asana Data Type
   * - name
     - member_invite_management_access_level
     - "string"
   * - name
     - name
     - "string"


Tripletex Department to Asana Teams
-----------------------------------
Every Tripletex Department will be synchronized with a Asana Teams.

Once a link between a Tripletex Department and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Asana Teams Property
     - Asana Data Type
   * - departmentNumber
     - description
     - "string"
   * - departmentNumber
     - html_description
     - "string"
   * - name
     - member_invite_management_access_level
     - "string"
   * - name
     - name
     - "string"


Tripletex Supplier to Asana Teams
---------------------------------
Every Tripletex Supplier will be synchronized with a Asana Teams.

Once a link between a Tripletex Supplier and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Asana Teams Property
     - Asana Data Type
   * - name
     - member_invite_management_access_level
     - "string"
   * - name
     - name
     - "string"


Tripletex Project to Asana Projects
-----------------------------------
Every Tripletex Project will be synchronized with a Asana Projects.

Once a link between a Tripletex Project and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Asana Projects Property
     - Asana Data Type
   * - endDate
     - due_date
     - "string"
   * - endDate
     - due_on
     - "string"
   * - name
     - name
     - "string"
   * - projectManager.id
     - owner.gid
     - "string"
   * - startDate
     - start_on
     - "string"

