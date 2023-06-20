=================================
SuperOffice to Freshteam Dataflow
=================================

Generated: 2023-06-20 01:07:23

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Ownercontactlink to Freshteam Department
----------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a Freshteam Department.

Once a link between a SuperOffice Ownercontactlink and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - name
     - name
     - "string"


SuperOffice User to Freshteam Employee
--------------------------------------
Every SuperOffice User will be synchronized with a Freshteam Employee.

Once a link between a SuperOffice User and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"

