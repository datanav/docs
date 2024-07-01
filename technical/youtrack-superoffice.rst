================================
YouTrack to Superoffice Dataflow
================================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Superoffice Person
------------------------------------
Every YouTrack Users will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the YouTrack Users will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A YouTrack Users will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Superoffice Person Property
   * - profile.email.email
     - Emails.Value

Once a link between a YouTrack Users and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - profile.email
     - Emails.Value
     - "string"
   * - profile.email.email
     - Emails.Value
     - "string"


YouTrack Groups to Superoffice Contact
--------------------------------------
Every YouTrack Groups will be synchronized with a Superoffice Contact.

Once a link between a YouTrack Groups and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"


YouTrack Organizations to Superoffice Contact
---------------------------------------------
Every YouTrack Organizations will be synchronized with a Superoffice Contact.

Once a link between a YouTrack Organizations and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"


YouTrack Usergroups to Superoffice Contact
------------------------------------------
Every YouTrack Usergroups will be synchronized with a Superoffice Contact.

Once a link between a YouTrack Usergroups and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"

