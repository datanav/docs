==================================
Powerofficego to YouTrack Dataflow
==================================

Generated: 2023-11-16 13:55:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to YouTrack Users
---------------------------------------------
Every Powerofficego Contactperson will be synchronized with a YouTrack Users.

If a matching YouTrack Users already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching YouTrack Users is found, a new YouTrack Users will be created.

A Powerofficego Contactperson will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - YouTrack Users Property
   * - emailAddress
     - 
   * - emailAddress
     - profile.email

Once a link between a Powerofficego Contactperson and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - emailAddress
     - profile.email
     - "string"
   * - emailAddress
     - profile.email.email
     - "string"


Powerofficego Customers person to YouTrack Users
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a YouTrack Users must be established.

A Powerofficego Customers person will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - YouTrack Users Property
   * - EmailAddress
     - 
   * - EmailAddress
     - profile.email

Once a link between a Powerofficego Customers person and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - EmailAddress
     - profile.email
     - "string"


Powerofficego Contactperson to YouTrack Usersyoutrack
-----------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Powerofficego Contactperson and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


Powerofficego Currency to YouTrack Organizationroles
----------------------------------------------------
Every Powerofficego Currency will be synchronized with a YouTrack Organizationroles.

Once a link between a Powerofficego Currency and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Powerofficego Customers to YouTrack Groups
------------------------------------------
Every Powerofficego Customers will be synchronized with a YouTrack Groups.

Once a link between a Powerofficego Customers and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Customers to YouTrack Usergroups
----------------------------------------------
Every Powerofficego Customers will be synchronized with a YouTrack Usergroups.

Once a link between a Powerofficego Customers and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Customers to YouTrack Workitems
---------------------------------------------
Every Powerofficego Customers will be synchronized with a YouTrack Workitems.

Once a link between a Powerofficego Customers and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - Name
     - updated
     - "string"


Powerofficego Departments to YouTrack Groups
--------------------------------------------
Every Powerofficego Departments will be synchronized with a YouTrack Groups.

Once a link between a Powerofficego Departments and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to YouTrack Usergroups
------------------------------------------------
Every Powerofficego Departments will be synchronized with a YouTrack Usergroups.

Once a link between a Powerofficego Departments and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to YouTrack Workitems
-----------------------------------------------
Every Powerofficego Departments will be synchronized with a YouTrack Workitems.

Once a link between a Powerofficego Departments and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - Name
     - updated
     - "string"


Powerofficego Employees to YouTrack Usersyoutrack
-------------------------------------------------
Every Powerofficego Employees will be synchronized with a YouTrack Usersyoutrack.

Once a link between a Powerofficego Employees and a YouTrack Usersyoutrack is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a YouTrack Usersyoutrack:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - YouTrack Usersyoutrack Property
     - YouTrack Data Type


Powerofficego Productgroup to YouTrack Organizationroles
--------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a YouTrack Organizationroles.

Once a link between a Powerofficego Productgroup and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Powerofficego Employees to YouTrack Users
-----------------------------------------
Every Powerofficego Employees will be synchronized with a YouTrack Users.

Once a link between a Powerofficego Employees and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - YouTrack Users Property
     - YouTrack Data Type

