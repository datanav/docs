==============================
Tidsbanken to HubSpot Dataflow
==============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to HubSpot Contact
------------------------------------
Every Tidsbanken Ansatt will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Tidsbanken Ansatt will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - HubSpot Contact Property
   * - Epost
     - properties.email

Once a link between a Tidsbanken Ansatt and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - Adresse
     - properties.address
     - "string"
   * - Etternavn
     - properties.lastname
     - "string"
   * - Fodt
     - properties.date_of_birth
     - "string"
   * - Fornavn
     - properties.firstname
     - "string"
   * - Id
     - id
     - "string"
   * - Mobil
     - properties.mobilephone
     - "string"
   * - Postnummer
     - properties.zip
     - "string"
   * - Poststed
     - properties.city
     - "string"


Tidsbanken Avdeling to HubSpot Company
--------------------------------------
Every Tidsbanken Avdeling will be synchronized with a HubSpot Company.

Once a link between a Tidsbanken Avdeling and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Navn
     - properties.name
     - "string"


Tidsbanken Kunde to HubSpot Company
-----------------------------------
Every Tidsbanken Kunde will be synchronized with a HubSpot Company.

Once a link between a Tidsbanken Kunde and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Gateadresse
     - properties.address
     - "string"
   * - Id
     - id
     - "string"
   * - LevPostNr
     - properties.zip
     - "string"
   * - LevPoststed
     - properties.city
     - "string"
   * - Leveringsadresse
     - properties.address
     - "string"
   * - Leveringsadresse2
     - properties.address2
     - "string"
   * - Navn
     - properties.name
     - "string"
   * - Postadresse
     - properties.address2
     - "string"
   * - Postnr
     - properties.zip
     - "string"
   * - Poststed
     - properties.city
     - "string"
   * - Telefon
     - properties.phone
     - "string"
   * - Url
     - properties.website
     - "string"

