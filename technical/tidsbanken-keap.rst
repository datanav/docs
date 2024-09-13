===========================
Tidsbanken to Keap Dataflow
===========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Keap Contacts
----------------------------------
Every Tidsbanken Ansatt will be synchronized with a Keap Contacts.

Once a link between a Tidsbanken Ansatt and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Keap Contacts Property
     - Keap Data Type
   * - Fodt
     - birthday
     - "string"


Tidsbanken Avdeling to Keap Companies
-------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Keap Companies.

Once a link between a Tidsbanken Avdeling and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Keap Companies Property
     - Keap Data Type
   * - Navn
     - company_name
     - "string"


Tidsbanken Kunde to Keap Companies
----------------------------------
Every Tidsbanken Kunde will be synchronized with a Keap Companies.

Once a link between a Tidsbanken Kunde and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Keap Companies Property
     - Keap Data Type
   * - Id
     - id
     - "string"
   * - LevPostNr
     - address.zip_code
     - "string"
   * - LevPoststed
     - address.locality
     - "string"
   * - Navn
     - company_name
     - "string"
   * - Postnr
     - address.zip_code
     - "string"
   * - Poststed
     - address.locality
     - "string"

