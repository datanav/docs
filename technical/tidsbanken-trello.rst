=============================
Tidsbanken to Trello Dataflow
=============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Trello Organizations
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Trello Organizations.

Once a link between a Tidsbanken Avdeling and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Trello Organizations Property
     - Trello Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to Trello Organizations
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Trello Organizations.

Once a link between a Tidsbanken Kunde and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Trello Organizations Property
     - Trello Data Type
   * - Navn
     - name
     - "string"
   * - Url
     - website
     - "string"


Tidsbanken Prosjekt to Trello Actions
-------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Trello Actions.

Once a link between a Tidsbanken Prosjekt and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Trello Actions Property
     - Trello Data Type
   * - AnsvarligId
     - memberCreator.id
     - "string"
   * - StartDato
     - date
     - "string"


Tidsbanken Ansatt to Trello Members
-----------------------------------
Every Tidsbanken Ansatt will be synchronized with a Trello Members.

Once a link between a Tidsbanken Ansatt and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Trello Members Property
     - Trello Data Type
   * - Navn
     - fullName
     - "string"

