============================
Asana to Tidsbanken Dataflow
============================

Generated: 2024-03-26 14:22:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to  Prosjekt
---------------------------
Every Asana Projects will be synchronized with a  Prosjekt.

Once a link between a Asana Projects and a  Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a  Prosjekt:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     -  Prosjekt Property
     -  Data Type
   * - completed_at
     - AvsluttetDato
     - "string"
   * - name
     - Navn
     - "string"
   * - owner.gid
     - AnsvarligId
     - "integer"


Asana Users to  Ansatt
----------------------
Every Asana Users will be synchronized with a  Ansatt.

Once a link between a Asana Users and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Ansatt Property
     -  Data Type
   * - name
     - Navn
     - "string"
   * - workspaces.gid
     - AvdelingId
     - "string"
   * - workspaces.gid
     - Tittel
     - "string"

