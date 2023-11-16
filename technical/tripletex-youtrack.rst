==============================
Tripletex to YouTrack Dataflow
==============================

Generated: 2023-11-16 13:55:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to YouTrack Users
-----------------------------------
Every Tripletex Contact will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the Tripletex Contact will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A Tripletex Contact will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - YouTrack Users Property
   * - email
     - 
   * - email
     - profile.email
   * - email
     - profile.email.email

Once a link between a Tripletex Contact and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email
     - "string"
   * - email
     - profile.email.email
     - "string"


Tripletex Contact to YouTrack Usersyoutrack
-------------------------------------------
Every Tripletex Contact will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Tripletex Contact and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


Tripletex Customer to YouTrack Groups
-------------------------------------
Every Tripletex Customer will be synchronized with a YouTrack Groups.

Once a link between a Tripletex Customer and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Customer to YouTrack Usergroups
-----------------------------------------
Every Tripletex Customer will be synchronized with a YouTrack Usergroups.

Once a link between a Tripletex Customer and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Customer to YouTrack Workitems
----------------------------------------
Every Tripletex Customer will be synchronized with a YouTrack Workitems.

Once a link between a Tripletex Customer and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"


Tripletex Customercategory to YouTrack Organizationroles
--------------------------------------------------------
Every Tripletex Customercategory will be synchronized with a YouTrack Organizationroles.

Once a link between a Tripletex Customercategory and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customercategory and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Customercategory Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Tripletex Department to YouTrack Groups
---------------------------------------
Every Tripletex Department will be synchronized with a YouTrack Groups.

Once a link between a Tripletex Department and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Department to YouTrack Usergroups
-------------------------------------------
Every Tripletex Department will be synchronized with a YouTrack Usergroups.

Once a link between a Tripletex Department and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Department to YouTrack Workitems
------------------------------------------
Every Tripletex Department will be synchronized with a YouTrack Workitems.

Once a link between a Tripletex Department and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"


Tripletex Employee to YouTrack Usersyoutrack
--------------------------------------------
Every Tripletex Employee will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Tripletex Employee and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


Tripletex Productgroup to YouTrack Organizationroles
----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a YouTrack Organizationroles.

Once a link between a Tripletex Productgroup and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Tripletex Productunit to YouTrack Organizationroles
---------------------------------------------------
Every Tripletex Productunit will be synchronized with a YouTrack Organizationroles.

Once a link between a Tripletex Productunit and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Tripletex Project to YouTrack Hubprojects
-----------------------------------------
Every Tripletex Project will be synchronized with a YouTrack Hubprojects.

Once a link between a Tripletex Project and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type


Tripletex Project to YouTrack Organizationroles
-----------------------------------------------
Every Tripletex Project will be synchronized with a YouTrack Organizationroles.

Once a link between a Tripletex Project and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - endDate
     - id
     - "string"


Tripletex Project to YouTrack Usergroups
----------------------------------------
Every Tripletex Project will be synchronized with a YouTrack Usergroups.

Once a link between a Tripletex Project and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - endDate
     - name
     - "string"
   * - name
     - users.id
     - "string"


Tripletex Projectcategory to YouTrack Organizationroles
-------------------------------------------------------
Every Tripletex Projectcategory will be synchronized with a YouTrack Organizationroles.

Once a link between a Tripletex Projectcategory and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectcategory and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectcategory Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Tripletex Supplier to YouTrack Groups
-------------------------------------
Every Tripletex Supplier will be synchronized with a YouTrack Groups.

Once a link between a Tripletex Supplier and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Supplier to YouTrack Usergroups
-----------------------------------------
Every Tripletex Supplier will be synchronized with a YouTrack Usergroups.

Once a link between a Tripletex Supplier and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Tripletex Supplier to YouTrack Workitems
----------------------------------------
Every Tripletex Supplier will be synchronized with a YouTrack Workitems.

Once a link between a Tripletex Supplier and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"


Tripletex Employee to YouTrack Users
------------------------------------
Every Tripletex Employee will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the Tripletex Employee will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A Tripletex Employee will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - YouTrack Users Property
   * - email
     - 
   * - email
     - profile.email
   * - email
     - profile.email.email

Once a link between a Tripletex Employee and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - YouTrack Users Property
     - YouTrack Data Type

