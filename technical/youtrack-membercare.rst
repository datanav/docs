===============================
YouTrack to Membercare Dataflow
===============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to Membercare Companies
---------------------------------------
Every YouTrack Groups will be synchronized with a Membercare Companies.

Once a link between a YouTrack Groups and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Membercare Companies Property
     - Membercare Data Type


YouTrack Organizationroles to Membercare Companycategories
----------------------------------------------------------
Every YouTrack Organizationroles will be synchronized with a Membercare Companycategories.

Once a link between a YouTrack Organizationroles and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizationroles and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizationroles Property
     - Membercare Companycategories Property
     - Membercare Data Type


YouTrack Organizations to Membercare Companies
----------------------------------------------
Every YouTrack Organizations will be synchronized with a Membercare Companies.

Once a link between a YouTrack Organizations and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Membercare Companies Property
     - Membercare Data Type


YouTrack Roles to Membercare Companycategories
----------------------------------------------
Every YouTrack Roles will be synchronized with a Membercare Companycategories.

Once a link between a YouTrack Roles and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - Membercare Companycategories Property
     - Membercare Data Type


YouTrack Usergroups to Membercare Companies
-------------------------------------------
Every YouTrack Usergroups will be synchronized with a Membercare Companies.

Once a link between a YouTrack Usergroups and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Membercare Companies Property
     - Membercare Data Type


YouTrack Users to Membercare Persons
------------------------------------
Every YouTrack Users will be synchronized with a Membercare Persons.

Once a link between a YouTrack Users and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Membercare Persons Property
     - Membercare Data Type
   * - name
     - name
     - "string"
   * - profile.email.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"

