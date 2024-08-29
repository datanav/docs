=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-08-29 11:00:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to  Contacts
------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Contacts.

Once a link between a Tidsbanken Ansatt and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Contacts Property
     -  Data Type
   * - Epost
     - BusinessEmail
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - BirthDate
     - "string"
   * - Fornavn
     - FirstName
     - "string"
   * - Mobil
     - Mobile
     - "string"
   * - Navn
     - FullName
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Avdeling to  Accounts
--------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Accounts.

Once a link between a Tidsbanken Avdeling and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Accounts Property
     -  Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Ansatt to  Addresses
-------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Addresses.

Once a link between a Tidsbanken Ansatt and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Addresses Property
     -  Data Type
   * - Adresse
     - AddressLine1
     - "string"
   * - Poststed
     - City
     - "string"


Tidsbanken Kunde to  Accounts
-----------------------------
Every Tidsbanken Kunde will be synchronized with a  Accounts.

Once a link between a Tidsbanken Kunde and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Accounts Property
     -  Data Type
   * - Gateadresse
     - AddressLine1
     - "string"
   * - LevPoststed
     - City
     - "string"
   * - Leveringsadresse
     - AddressLine1
     - "string"
   * - Leveringsadresse2
     - AddressLine2
     - "string"
   * - Postadresse
     - AddressLine2
     - "string"
   * - Poststed
     - City
     - "string"

