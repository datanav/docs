===================================
Wave Financial to YouTrack Dataflow
===================================

Generated: 2023-11-16 13:55:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to YouTrack Users
--------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a YouTrack Users must be established.

A Wave Customer person will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - YouTrack Users Property
   * - email
     - 
   * - email
     - profile.email
   * - email
     - profile.email.email

Once a link between a Wave Customer person and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email
     - "string"


Wave Customer to YouTrack Users
-------------------------------
Before any synchronization can take place, a link between a Wave Customer and a YouTrack Users must be established.

A Wave Customer will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - YouTrack Users Property
   * - email
     - 
   * - email
     - profile.email
   * - email
     - profile.email.email

Once a link between a Wave Customer and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email
     - "string"


Wave Vendor to YouTrack Users
-----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a YouTrack Users must be established.

A Wave Vendor will merge with a YouTrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - YouTrack Users Property
   * - email
     - 
   * - email
     - profile.email
   * - email
     - profile.email.email

Once a link between a Wave Vendor and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email
     - "string"


Wave Customer to YouTrack Groups
--------------------------------
Every Wave Customer will be synchronized with a YouTrack Groups.

Once a link between a Wave Customer and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Wave Customer to YouTrack Usergroups
------------------------------------
Every Wave Customer will be synchronized with a YouTrack Usergroups.

Once a link between a Wave Customer and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Wave Customer to YouTrack Workitems
-----------------------------------
Every Wave Customer will be synchronized with a YouTrack Workitems.

Once a link between a Wave Customer and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - internalNotes
     - date
     - "string"
   * - name
     - updated
     - "string"


Wave Vendor to YouTrack Groups
------------------------------
Every Wave Vendor will be synchronized with a YouTrack Groups.

Once a link between a Wave Vendor and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Wave Vendor to YouTrack Usergroups
----------------------------------
Every Wave Vendor will be synchronized with a YouTrack Usergroups.

Once a link between a Wave Vendor and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Wave Vendor to YouTrack Workitems
---------------------------------
Every Wave Vendor will be synchronized with a YouTrack Workitems.

Once a link between a Wave Vendor and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - internalNotes
     - date
     - "string"
   * - name
     - updated
     - "string"

