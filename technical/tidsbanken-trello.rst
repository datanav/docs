=============================
Tidsbanken to Trello Dataflow
=============================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to  Organizations
-------------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Organizations.

Once a link between a Tidsbanken Avdeling and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Organizations Property
     -  Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to  Organizations
----------------------------------
Every Tidsbanken Kunde will be synchronized with a  Organizations.

Once a link between a Tidsbanken Kunde and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Organizations Property
     -  Data Type
   * - Navn
     - name
     - "string"
   * - Url
     - website
     - "string"


Tidsbanken Prosjekt to  Actions
-------------------------------
Every Tidsbanken Prosjekt will be synchronized with a  Actions.

Once a link between a Tidsbanken Prosjekt and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a  Actions:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     -  Actions Property
     -  Data Type
   * - AnsvarligId
     - memberCreator.id
     - "string"
   * - StartDato
     - date
     - "string"


Tidsbanken Prosjekt to  Boards
------------------------------
Every Tidsbanken Prosjekt will be synchronized with a  Boards.

Once a link between a Tidsbanken Prosjekt and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a  Boards:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     -  Boards Property
     -  Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Ansatt to  Members
-----------------------------
Every Tidsbanken Ansatt will be synchronized with a  Members.

Once a link between a Tidsbanken Ansatt and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Members:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Members Property
     -  Data Type
   * - Navn
     - fullName
     - "string"

