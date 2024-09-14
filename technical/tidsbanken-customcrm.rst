=================================
Tidsbanken to Custom CRM Dataflow
=================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Custom CRM Contact
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Custom CRM Contact.

Once a link between a Tidsbanken Ansatt and a Custom CRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Custom CRM Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Custom CRM Contact Property
     - Custom CRM Data Type


Tidsbanken Avdeling to Custom CRM Customer
------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Custom CRM Customer.

Once a link between a Tidsbanken Avdeling and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Custom CRM Customer Property
     - Custom CRM Data Type


Tidsbanken Kunde to Custom CRM Customer
---------------------------------------
Every Tidsbanken Kunde will be synchronized with a Custom CRM Customer.

Once a link between a Tidsbanken Kunde and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Custom CRM Customer Property
     - Custom CRM Data Type
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

