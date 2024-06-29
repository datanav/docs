============================
Tidsbanken to Asana Dataflow
============================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Prosjekt to Asana Projects
-------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Asana Projects.

Once a link between a Tidsbanken Prosjekt and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Asana Projects Property
     - Asana Data Type
   * - AnsvarligId
     - owner.gid
     - "string"
   * - Navn
     - name
     - "string"

