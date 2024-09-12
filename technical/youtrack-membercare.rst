===============================
YouTrack to MemberCare Dataflow
===============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Groups to MemberCare Companies
---------------------------------------
Every YouTrack Groups will be synchronized with a MemberCare Companies.

Once a link between a YouTrack Groups and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - MemberCare Companies Property
     - MemberCare Data Type


YouTrack Organizationroles to MemberCare Companycategories
----------------------------------------------------------
Every YouTrack Organizationroles will be synchronized with a MemberCare Companycategories.

Once a link between a YouTrack Organizationroles and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizationroles and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizationroles Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


YouTrack Organizations to MemberCare Companies
----------------------------------------------
Every YouTrack Organizations will be synchronized with a MemberCare Companies.

Once a link between a YouTrack Organizations and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - MemberCare Companies Property
     - MemberCare Data Type


YouTrack Roles to MemberCare Companycategories
----------------------------------------------
Every YouTrack Roles will be synchronized with a MemberCare Companycategories.

Once a link between a YouTrack Roles and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Roles and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - YouTrack Roles Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


YouTrack Usergroups to MemberCare Companies
-------------------------------------------
Every YouTrack Usergroups will be synchronized with a MemberCare Companies.

Once a link between a YouTrack Usergroups and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - MemberCare Companies Property
     - MemberCare Data Type


YouTrack Users to MemberCare Persons
------------------------------------
Every YouTrack Users will be synchronized with a MemberCare Persons.

Once a link between a YouTrack Users and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - name
     - name
     - "string"
   * - profile.email.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"

