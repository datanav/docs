================================
Tidsbanken to Customcrm Dataflow
================================

Generated: 2024-09-10 14:18:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to  Customer
--------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Customer.

Once a link between a Tidsbanken Avdeling and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Customer Property
     -  Data Type


Tidsbanken Kunde to Customcrm Customer
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a Customcrm Customer.

Once a link between a Tidsbanken Kunde and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Customcrm Customer Property
     - Customcrm Data Type
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

