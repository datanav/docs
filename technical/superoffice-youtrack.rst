================================
SuperOffice to YouTrack Dataflow
================================

Generated: 2023-11-16 13:29:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to YouTrack Users
------------------------------------
Every SuperOffice Person will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the SuperOffice Person will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A SuperOffice Person will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - YouTrack Users Property
   * - Emails.Value
     - 
   * - Emails.Value
     - profile.email

Once a link between a SuperOffice Person and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - Emails.Value
     - profile.email
     - "string"


SuperOffice Contact to YouTrack Groups
--------------------------------------
Every SuperOffice Contact will be synchronized with a YouTrack Groups.

Once a link between a SuperOffice Contact and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


SuperOffice Contact to YouTrack Usergroups
------------------------------------------
Every SuperOffice Contact will be synchronized with a YouTrack Usergroups.

Once a link between a SuperOffice Contact and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


SuperOffice Contact to YouTrack Workitems
-----------------------------------------
Every SuperOffice Contact will be synchronized with a YouTrack Workitems.

Once a link between a SuperOffice Contact and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - Name
     - updated
     - "string"


SuperOffice Listbusinessitems to YouTrack Organizationroles
-----------------------------------------------------------
Every SuperOffice Listbusinessitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listbusinessitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listbusinessitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listbusinessitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listcategoryitems to YouTrack Organizationroles
-----------------------------------------------------------
Every SuperOffice Listcategoryitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listcategoryitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcategoryitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcategoryitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listproductcategoryitems to YouTrack Organizationroles
------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listproductcategoryitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listproductfamilyitems to YouTrack Organizationroles
----------------------------------------------------------------
Every SuperOffice Listproductfamilyitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listproductfamilyitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductfamilyitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductfamilyitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listproducttypeitems to YouTrack Organizationroles
--------------------------------------------------------------
Every SuperOffice Listproducttypeitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listproducttypeitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproducttypeitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproducttypeitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listprojectstatusitems to YouTrack Organizationroles
----------------------------------------------------------------
Every SuperOffice Listprojectstatusitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listprojectstatusitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojectstatusitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojectstatusitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listprojecttypeitems to YouTrack Organizationroles
--------------------------------------------------------------
Every SuperOffice Listprojecttypeitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listprojecttypeitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojecttypeitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojecttypeitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listsaletypeitems to YouTrack Organizationroles
-----------------------------------------------------------
Every SuperOffice Listsaletypeitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listsaletypeitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listsaletypeitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listsaletypeitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


SuperOffice Listticketcategoryitems to YouTrack Organizationroles
-----------------------------------------------------------------
Every SuperOffice Listticketcategoryitems will be synchronized with a YouTrack Organizationroles.

Once a link between a SuperOffice Listticketcategoryitems and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listticketcategoryitems and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listticketcategoryitems Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - CategoryMaster
     - organization.id
     - "string"
   * - CategoryMaster
     - owner.id
     - "string"
   * - CategoryMaster
     - role.id
     - "string"


SuperOffice Person to YouTrack Usersyoutrack
--------------------------------------------
Every SuperOffice Person will be synchronized with a YouTrack Usersyoutrack.

Once a link between a SuperOffice Person and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


SuperOffice User to YouTrack Users
----------------------------------
Every SuperOffice User will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the SuperOffice User will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A SuperOffice User will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - YouTrack Users Property
   * - personEmail
     - 
   * - personEmail
     - profile.email

Once a link between a SuperOffice User and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - personEmail
     - profile.email
     - "string"

