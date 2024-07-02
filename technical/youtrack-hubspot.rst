============================
YouTrack to Hubspot Dataflow
============================

Generated: 2024-07-02 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Hubspot Contact
---------------------------------
Every YouTrack Users will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the YouTrack Users will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A YouTrack Users will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Hubspot Contact Property
   * - profile.email.email
     - properties.email

Once a link between a YouTrack Users and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - profile.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.email
     - "string"
   * - profile.email.email
     - properties.work_email
     - "string"


YouTrack Groups to Hubspot Company
----------------------------------
Every YouTrack Groups will be synchronized with a Hubspot Company.

Once a link between a YouTrack Groups and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"


YouTrack Organizations to Hubspot Company
-----------------------------------------
Every YouTrack Organizations will be synchronized with a Hubspot Company.

Once a link between a YouTrack Organizations and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"


YouTrack Usergroups to Hubspot Company
--------------------------------------
Every YouTrack Usergroups will be synchronized with a Hubspot Company.

Once a link between a YouTrack Usergroups and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"


YouTrack Users to Hubspot User
------------------------------
Every YouTrack Users will be synchronized with a Hubspot User.

Once a link between a YouTrack Users and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Hubspot User Property
     - Hubspot Data Type
   * - profile.email.email
     - email
     - "string"

