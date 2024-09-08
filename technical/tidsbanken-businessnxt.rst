==================================
Tidsbanken to Businessnxt Dataflow
==================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Businessnxt Address
------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Businessnxt Address.

Once a link between a Tidsbanken Avdeling and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to Businessnxt Address
---------------------------------------
Every Tidsbanken Kunde will be synchronized with a Businessnxt Address.

Once a link between a Tidsbanken Kunde and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Mobil
     - mobilePhone
     - "string"
   * - Navn
     - name
     - "string"
   * - Telefon
     - phone
     - "string"

