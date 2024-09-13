===================================
Tidsbanken to Business Nxt Dataflow
===================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Business Nxt Address
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Business Nxt Address.

Once a link between a Tidsbanken Avdeling and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to Business Nxt Address
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Business Nxt Address.

Once a link between a Tidsbanken Kunde and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - Mobil
     - mobilePhone
     - "string"
   * - Navn
     - name
     - "string"
   * - Telefon
     - phone
     - "string"

