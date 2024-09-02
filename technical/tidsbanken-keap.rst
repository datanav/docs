=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-09-02 13:38:44

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
   * - Fodt
     - birthday
     - "string"


Tidsbanken Avdeling to  Companies
---------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Companies.

Once a link between a Tidsbanken Avdeling and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Companies Property
     -  Data Type
   * - Navn
     - company_name
     - "string"


Tidsbanken Kunde to  Companies
------------------------------
Every Tidsbanken Kunde will be synchronized with a  Companies.

Once a link between a Tidsbanken Kunde and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
     -  Data Type
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

