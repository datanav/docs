===============================
Tidsbanken to Youtrack Dataflow
===============================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Youtrack Users
-----------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Youtrack Users must be established.

A Tidsbanken Ansatt will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Youtrack Users Property
   * - Epost
     - profile.email.email

Once a link between a Tidsbanken Ansatt and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - Epost
     - profile.email.email
     - "string"
   * - Navn
     - name
     - "string"


Tidsbanken Avdeling to Youtrack Groups
--------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Youtrack Groups.

Once a link between a Tidsbanken Avdeling and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Youtrack Groups Property
     - Youtrack Data Type


Tidsbanken Kunde to Youtrack Groups
-----------------------------------
Every Tidsbanken Kunde will be synchronized with a Youtrack Groups.

Once a link between a Tidsbanken Kunde and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Youtrack Groups Property
     - Youtrack Data Type


Tidsbanken Prosjekt to Youtrack Hubprojects
-------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Youtrack Hubprojects.

Once a link between a Tidsbanken Prosjekt and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type

