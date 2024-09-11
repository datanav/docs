================================
Tidsbanken to CustomCRM Dataflow
================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Custom Contact
-----------------------------------
Every Tidsbanken Ansatt will be synchronized with a Custom Contact.

Once a link between a Tidsbanken Ansatt and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Custom Contact Property
     - Custom Data Type


Tidsbanken Avdeling to Custom Customer
--------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Custom Customer.

Once a link between a Tidsbanken Avdeling and a Custom Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Custom Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Custom Customer Property
     - Custom Data Type


Tidsbanken Kunde to CustomCRM Customer
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a CustomCRM Customer.

Once a link between a Tidsbanken Kunde and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
   * - Gateadresse
     - StreetAddress1
     - "string"
   * - LevPostNr
     - ZipCode
     - "string"
   * - LevPoststed
     - City
     - "string"
   * - Leveringsadresse
     - StreetAddress1
     - "string"
   * - Leveringsadresse2
     - StreetAddress2
     - "string"
   * - Mobil
     - Phone
     - "string"
   * - Navn
     - Name
     - "string"
   * - Postadresse
     - StreetAddress2
     - "string"
   * - Postnr
     - ZipCode
     - "string"
   * - Poststed
     - City
     - "string"
   * - Url
     - Website
     - "string"

