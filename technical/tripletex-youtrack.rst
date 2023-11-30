======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Users
---------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Users must be established.

A Tripletex Contact will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Contact and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Users Property
     -  Data Type
   * - email
     - profile.email
     - "string"
   * - email
     - profile.email.email
     - "string"


Tripletex Employee to  Users
----------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Users must be established.

A Tripletex Employee will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Employee and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Users Property
     -  Data Type
   * - email
     - profile.email.email
     - "string"
   * - userType
     - userType.id
     - "string"


Tripletex Customer to  Groups
-----------------------------
Every Tripletex Customer will be synchronized with a  Groups.

Once a link between a Tripletex Customer and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Groups Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Customercategory to  Organizationroles
------------------------------------------------
Every Tripletex Customercategory will be synchronized with a  Organizationroles.

Once a link between a Tripletex Customercategory and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customercategory and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Customercategory Property
     -  Organizationroles Property
     -  Data Type


Tripletex Department to  Groups
-------------------------------
Every Tripletex Department will be synchronized with a  Groups.

Once a link between a Tripletex Department and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Groups Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Productgroup to  Organizationroles
--------------------------------------------
Every Tripletex Productgroup will be synchronized with a  Organizationroles.

Once a link between a Tripletex Productgroup and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     -  Organizationroles Property
     -  Data Type


Tripletex Productunit to  Organizationroles
-------------------------------------------
Every Tripletex Productunit will be synchronized with a  Organizationroles.

Once a link between a Tripletex Productunit and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     -  Organizationroles Property
     -  Data Type


Tripletex Project to  Hubprojects
---------------------------------
Every Tripletex Project will be synchronized with a  Hubprojects.

Once a link between a Tripletex Project and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     -  Hubprojects Property
     -  Data Type


Tripletex Projectcategory to  Organizationroles
-----------------------------------------------
Every Tripletex Projectcategory will be synchronized with a  Organizationroles.

Once a link between a Tripletex Projectcategory and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Projectcategory and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - Tripletex Projectcategory Property
     -  Organizationroles Property
     -  Data Type

