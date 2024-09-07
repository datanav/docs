=============================
Tidsbanken to Webcrm Dataflow
=============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Webcrm Organisations
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Webcrm Organisations.

Once a link between a Tidsbanken Avdeling and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Adresse
     - OrganisationAddress
     - "string"
   * - Adresse
     - OrganisationDeliveryAddress
     - "string"
   * - Id
     - OrganisationId
     - "string"
   * - Navn
     - OrganisationName
     - "string"
   * - Postnr
     - OrganisationDeliveryPostCode
     - "string"
   * - Postnr
     - OrganisationPostCode
     - "string"
   * - Poststed
     - OrganisationCity
     - "string"
   * - Poststed
     - OrganisationDeliveryCity
     - "string"


Tidsbanken Kunde to Webcrm Organisations
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Webcrm Organisations.

Once a link between a Tidsbanken Kunde and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Gateadresse
     - OrganisationAddress
     - "string"
   * - Gateadresse
     - OrganisationDeliveryAddress
     - "string"
   * - Id
     - OrganisationId
     - "string"
   * - LevPostNr
     - OrganisationDeliveryPostCode
     - "string"
   * - LevPostNr
     - OrganisationPostCode
     - "string"
   * - LevPoststed
     - OrganisationCity
     - "string"
   * - LevPoststed
     - OrganisationDeliveryCity
     - "string"
   * - Leveringsadresse
     - OrganisationAddress
     - "string"
   * - Leveringsadresse
     - OrganisationDeliveryAddress
     - "string"
   * - Navn
     - OrganisationName
     - "string"
   * - Postnr
     - OrganisationDeliveryPostCode
     - "string"
   * - Postnr
     - OrganisationPostCode
     - "string"
   * - Poststed
     - OrganisationCity
     - "string"
   * - Poststed
     - OrganisationDeliveryCity
     - "string"
   * - Telefon
     - OrganisationTelephone
     - "string"

