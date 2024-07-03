==============================
Tidsbanken to Hubspot Dataflow
==============================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Hubspot Contact
------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Tidsbanken Ansatt will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Hubspot Contact Property
   * - Epost
     - properties.email

Once a link between a Tidsbanken Ansatt and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


Tidsbanken Avdeling to Hubspot Company
--------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Hubspot Company.

Once a link between a Tidsbanken Avdeling and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - Navn
     - properties.name
     - "string"


Tidsbanken Kunde to Hubspot Company
-----------------------------------
Every Tidsbanken Kunde will be synchronized with a Hubspot Company.

Once a link between a Tidsbanken Kunde and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Hubspot Company Property
     - Hubspot Data Type
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

