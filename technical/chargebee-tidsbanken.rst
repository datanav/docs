================================
Chargebee to Tidsbanken Dataflow
================================

Generated: 2024-09-23 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Tidsbanken Kunde
-------------------------------------
Every Chargebee Address will be synchronized with a Tidsbanken Kunde.

Once a link between a Chargebee Address and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - addr
     - Gateadresse
     - "string"
   * - addr
     - Leveringsadresse
     - "string"
   * - city
     - LevPoststed
     - "string"
   * - city
     - Poststed
     - "string"
   * - subscription_id
     - Id
     - "string"
   * - zip
     - LevPostNr
     - "string"
   * - zip
     - Postnr
     - "string"


Chargebee Customer to Tidsbanken Kunde
--------------------------------------
Every Chargebee Customer will be synchronized with a Tidsbanken Kunde.

Once a link between a Chargebee Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type

