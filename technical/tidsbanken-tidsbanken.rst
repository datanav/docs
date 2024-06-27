=================================
Tidsbanken to Tidsbanken Dataflow
=================================

Generated: 2024-06-27 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Tidsbanken Ansatt
--------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Tidsbanken Ansatt must be established.

A Tidsbanken Ansatt will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tidsbanken Ansatt Property
   * - Id
     - Id
   * - Epost
     - Epost
   * - Personnummer
     - Personnummer

Once a link between a Tidsbanken Ansatt and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type


Tidsbanken Avdeling to Tidsbanken Avdeling
------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Avdeling and a Tidsbanken Avdeling must be established.

A Tidsbanken Avdeling will merge with a Tidsbanken Avdeling if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Tidsbanken Avdeling Property
   * - Id
     - Id

Once a link between a Tidsbanken Avdeling and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type


Tidsbanken Kunde to Tidsbanken Kunde
------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Tidsbanken Kunde must be established.

A Tidsbanken Kunde will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tidsbanken Kunde Property
   * - Id
     - Id
   * - Epost
     - Epost
   * - Organisasjonsnummer
     - Organisasjonsnummer

Once a link between a Tidsbanken Kunde and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - Gateadresse
     - Leveringsadresse
     - "string"
   * - Id
     - Id
     - "string"
   * - LevPostNr
     - Postnr
     - "string"
   * - LevPoststed
     - Poststed
     - "string"
   * - Leveringsadresse
     - Gateadresse
     - "string"
   * - Leveringsadresse2
     - Postadresse
     - "string"
   * - Postadresse
     - Leveringsadresse2
     - "string"
   * - Postnr
     - LevPostNr
     - "string"
   * - Poststed
     - LevPoststed
     - "string"

