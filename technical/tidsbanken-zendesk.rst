==============================
Tidsbanken to Zendesk Dataflow
==============================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Zendesk Users
----------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Zendesk Users must be established.

A Tidsbanken Ansatt will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Zendesk Users Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - Navn
     - name
     - "string"
   * - TlfPrivat
     - phone
     - "string"


Tidsbanken Avdeling to Zendesk Organizations
--------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Zendesk Organizations.

Once a link between a Tidsbanken Avdeling and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to Zendesk Organizations
-----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Zendesk Organizations.

Once a link between a Tidsbanken Kunde and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Navn
     - name
     - "string"

