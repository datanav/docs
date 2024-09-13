================================
YouTrack to SuperOffice Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to SuperOffice Person
------------------------------------
Every YouTrack Users will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the YouTrack Users will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A YouTrack Users will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - SuperOffice Person Property
   * - profile.email.email
     - Emails.Value

Once a link between a YouTrack Users and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - profile.email
     - Emails.Value
     - "string"
   * - profile.email.email
     - Emails.Value
     - "string"


YouTrack Groups to SuperOffice Contact
--------------------------------------
Every YouTrack Groups will be synchronized with a SuperOffice Contact.

Once a link between a YouTrack Groups and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


YouTrack Organizations to SuperOffice Contact
---------------------------------------------
Every YouTrack Organizations will be synchronized with a SuperOffice Contact.

Once a link between a YouTrack Organizations and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


YouTrack Usergroups to SuperOffice Contact
------------------------------------------
Every YouTrack Usergroups will be synchronized with a SuperOffice Contact.

Once a link between a YouTrack Usergroups and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"

