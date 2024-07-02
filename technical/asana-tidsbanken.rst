============================
Asana to Tidsbanken Dataflow
============================

Generated: 2024-07-02 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to Tidsbanken Prosjekt
-------------------------------------
Every Asana Projects will be synchronized with a Tidsbanken Prosjekt.

Once a link between a Asana Projects and a Tidsbanken Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Tidsbanken Prosjekt:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Tidsbanken Prosjekt Property
     - Tidsbanken Data Type
   * - completed_at
     - AvsluttetDato
     - "string"
   * - name
     - Navn
     - "string"
   * - owner.gid
     - AnsvarligId
     - "integer"


Asana Users to Tidsbanken Ansatt
--------------------------------
Every Asana Users will be synchronized with a Tidsbanken Ansatt.

Once a link between a Asana Users and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - name
     - Navn
     - "string"
   * - workspaces.gid
     - AvdelingId
     - "string"
   * - workspaces.gid
     - Tittel
     - "string"

