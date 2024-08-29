=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-08-29 08:00:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to  Customer
------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Customer.

Once a link between a Tidsbanken Ansatt and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Customer Property
     -  Data Type
   * - Etternavn
     - last_name
     - "string"
   * - Fornavn
     - first_name
     - "string"


Tidsbanken Avdeling to  Business_entity
---------------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Business_entity.

Once a link between a Tidsbanken Avdeling and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Business_entity Property
     -  Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to  Business_entity
------------------------------------
Every Tidsbanken Kunde will be synchronized with a  Business_entity.

Once a link between a Tidsbanken Kunde and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Business_entity Property
     -  Data Type
   * - Navn
     - name
     - "string"

