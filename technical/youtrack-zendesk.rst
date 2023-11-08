============================
YouTrack to Zendesk Dataflow
============================

Generated: 2023-11-08 14:31:45

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Usergroups to Zendesk Organizations
--------------------------------------------
Every YouTrack Usergroups will be synchronized with a Zendesk Organizations.

Once a link between a YouTrack Usergroups and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


YouTrack Workitems to Zendesk Organizations
-------------------------------------------
Every YouTrack Workitems will be synchronized with a Zendesk Organizations.

Once a link between a YouTrack Workitems and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - updated
     - name
     - "string"

