=============================
Tidsbanken to WebCRM Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to WebCRM Organisations
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a WebCRM Organisations.

Once a link between a Tidsbanken Avdeling and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - WebCRM Organisations Property
     - WebCRM Data Type
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


Tidsbanken Kunde to WebCRM Organisations
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a WebCRM Organisations.

Once a link between a Tidsbanken Kunde and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - WebCRM Organisations Property
     - WebCRM Data Type
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

