==============================
YouTrack to Tripletex Dataflow
==============================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Tripletex Contact
-----------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Tripletex Contact must be established.

A YouTrack Users will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Contact Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - profile.email
     - email
     - "string"
   * - profile.email.email
     - email
     - "string"


YouTrack Users to Tripletex Customer person
-------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Tripletex Customer person must be established.

A YouTrack Users will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Customer person Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


YouTrack Users to Tripletex Employee
------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Tripletex Employee must be established.

A YouTrack Users will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Employee Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - groups.id
     - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - N/A
   * - name
     - firstName
     - "string"
   * - name
     - lastName
     - "string"
   * - organizationRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - profile.email.email
     - email
     - "string"
   * - projectRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - sourcedOrganizationRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - sourcedProjectRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - teams.id
     - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - N/A
   * - transitiveGroups.id
     - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - N/A
   * - transitiveOrganizationRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - transitiveProjectRoles.id
     - department.id (Dependant on having wd:Q214339 in  Dependant on having wd:Q214339 in  )
     - N/A
   * - transitiveTeams.id
     - department.id (Dependant on having wd:Q43229 in  Dependant on having wd:Q43229 in  )
     - N/A

