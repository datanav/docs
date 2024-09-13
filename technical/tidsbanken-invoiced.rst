===============================
Tidsbanken to Invoiced Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Invoiced Customers company
----------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Invoiced Customers company.

Once a link between a Tidsbanken Kunde and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Gateadresse
     - address1
     - "string"
   * - Id
     - id
     - "string"
   * - LevPostNr
     - postal_code
     - "string"
   * - LevPoststed
     - city
     - "string"
   * - Leveringsadresse
     - address1
     - "string"
   * - Leveringsadresse2
     - address2
     - "string"
   * - Navn
     - name
     - "string"
   * - Postadresse
     - address2
     - "string"
   * - Postnr
     - postal_code
     - "string"
   * - Poststed
     - city
     - "string"

