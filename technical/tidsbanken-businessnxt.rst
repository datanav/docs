=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-09-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to  Address
-------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Address.

Once a link between a Tidsbanken Avdeling and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Address Property
     -  Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to  Address
----------------------------
Every Tidsbanken Kunde will be synchronized with a  Address.

Once a link between a Tidsbanken Kunde and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Address Property
     -  Data Type
   * - Mobil
     - mobilePhone
     - "string"
   * - Navn
     - name
     - "string"
   * - Telefon
     - phone
     - "string"

