===================================
Wave Financial to YouTrack Dataflow
===================================

Generated: 2023-11-08 13:24:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

