==============================
Tripletex to YouTrack Dataflow
==============================

Generated: 2023-11-29 14:44:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to YouTrack Users
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a YouTrack Users must be established.

A Tripletex Contact will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - YouTrack Users Property
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


Tripletex Employee to YouTrack Users
------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a YouTrack Users must be established.

A Tripletex Employee will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - YouTrack Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Employee and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email.email
     - "string"
   * - userType
     - userType.id
     - "string"


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

