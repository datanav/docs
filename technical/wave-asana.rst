================================
Wave Financial to Asana Dataflow
================================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

