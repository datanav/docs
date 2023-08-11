================================
Wave Financial to Asana Dataflow
================================

Generated: 2023-08-11 11:55:53

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Asana Teams
----------------------------
Every Wave Customer will be synchronized with a Asana Teams.

Once a link between a Wave Customer and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Asana Teams Property
     - Asana Data Type
   * - internalNotes
     - description
     - "string"
   * - internalNotes
     - html_description
     - "string"
   * - name
     - member_invite_management_access_level
     - "string"
   * - name
     - name
     - "string"
   * - website
     - permalink_url
     - "string"


Wave Vendor to Asana Teams
--------------------------
Every Wave Vendor will be synchronized with a Asana Teams.

Once a link between a Wave Vendor and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Asana Teams Property
     - Asana Data Type
   * - internalNotes
     - description
     - "string"
   * - internalNotes
     - html_description
     - "string"
   * - name
     - member_invite_management_access_level
     - "string"
   * - name
     - name
     - "string"
   * - website
     - permalink_url
     - "string"


Wave Business to Asana Teams
----------------------------
Every Wave Business will be synchronized with a Asana Teams.

Once a link between a Wave Business and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - Asana Teams Property
     - Asana Data Type
   * - name
     - name
     - "string"
   * - website
     - permalink_url
     - "string"

