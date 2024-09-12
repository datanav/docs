===========================
Tidsbanken to Difi Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Difi. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Difi Enhetsregisteret
-----------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Difi Enhetsregisteret must be established.

A Tidsbanken Kunde will merge with a Difi Enhetsregisteret if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Difi Enhetsregisteret Property
   * - Organisasjonsnummer
     - orgnr

Once a link between a Tidsbanken Kunde and a Difi Enhetsregisteret is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Difi Enhetsregisteret:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Difi Enhetsregisteret Property
     - Difi Data Type

