==================================
Tidsbanken to BusinessNxt Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to BusinessNxt Address
------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a BusinessNxt Address.

Once a link between a Tidsbanken Avdeling and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - Navn
     - name
     - "string"


Tidsbanken Kunde to BusinessNxt Address
---------------------------------------
Every Tidsbanken Kunde will be synchronized with a BusinessNxt Address.

Once a link between a Tidsbanken Kunde and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - Mobil
     - mobilePhone
     - "string"
   * - Navn
     - name
     - "string"
   * - Telefon
     - phone
     - "string"

