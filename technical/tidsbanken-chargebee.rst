================================
Tidsbanken to Chargebee Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Chargebee Customer
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Chargebee Customer.

Once a link between a Tidsbanken Ansatt and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Etternavn
     - last_name
     - "string"
   * - Fornavn
     - first_name
     - "string"


Tidsbanken Avdeling to Chargebee Business_entity
------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Chargebee Business_entity.

Once a link between a Tidsbanken Avdeling and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to Chargebee Business_entity
---------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Chargebee Business_entity.

Once a link between a Tidsbanken Kunde and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Navn
     - name
     - "string"

