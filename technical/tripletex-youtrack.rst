==============================
Tripletex to Youtrack Dataflow
==============================

Generated: 2024-06-29 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Youtrack Users
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Youtrack Users must be established.

A Tripletex Contact will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Contact and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email
     - "string"
   * - email
     - profile.email.email
     - "string"


Tripletex Customer person to Youtrack Users
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Youtrack Users must be established.

A Tripletex Customer person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Customer person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - name
     - name
     - "string"


Tripletex Employee to Youtrack Users
------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Youtrack Users must be established.

A Tripletex Employee will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Tripletex Employee and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - groups.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - organizationRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - projectRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - sourcedOrganizationRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - sourcedProjectRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - teams.id
     - "string"
   * - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - transitiveGroups.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - transitiveOrganizationRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - transitiveProjectRoles.id
     - "string"
   * - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - transitiveTeams.id
     - "string"
   * - email
     - profile.email.email
     - "string"
   * - firstName
     - name
     - "string"
   * - lastName
     - name
     - "string"
   * - userType
     - userType.id
     - "string"


Tripletex Customer to Youtrack Groups
-------------------------------------
Every Tripletex Customer will be synchronized with a Youtrack Groups.

Once a link between a Tripletex Customer and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - name
     - name
     - "string"


Tripletex Department to Youtrack Groups
---------------------------------------
Every Tripletex Department will be synchronized with a Youtrack Groups.

Once a link between a Tripletex Department and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - name
     - name
     - "string"


Tripletex Project to Youtrack Hubprojects
-----------------------------------------
Every Tripletex Project will be synchronized with a Youtrack Hubprojects.

Once a link between a Tripletex Project and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type

