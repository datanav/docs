================================
Wave Financial to Asana Dataflow
================================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Business to  Teams
-----------------------
Every Wave Business will be synchronized with a  Teams.

Once a link between a Wave Business and a  Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a  Teams:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     -  Teams Property
     -  Data Type
   * - name
     - name
     - "string"
   * - website
     - permalink_url
     - "string"

