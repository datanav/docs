================================
CustomPMS to Custom PMS Dataflow
================================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomPMS to Custom PMS. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Task to Custom Project
-----------------------------
Every Custom Task will be synchronized with a Custom Project.

Once a link between a Custom Task and a Custom Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Task and a Custom Project:

.. list-table::
   :header-rows: 1

   * - Custom Task Property
     - Custom Project Property
     - Custom Data Type

