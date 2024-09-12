===============================
Invoiced to Tidsbanken Dataflow
===============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Tidsbanken Kunde
----------------------------------------------
Every Invoiced Customers company will be synchronized with a Tidsbanken Kunde.

Once a link between a Invoiced Customers company and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - address1
     - Gateadresse
     - "string"
   * - address1
     - Leveringsadresse
     - "string"
   * - address2
     - Leveringsadresse2
     - "string"
   * - address2
     - Postadresse
     - "string"
   * - city
     - LevPoststed
     - "string"
   * - city
     - Poststed
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - Navn
     - "string"
   * - postal_code
     - LevPostNr
     - "string"
   * - postal_code
     - Postnr
     - "string"

