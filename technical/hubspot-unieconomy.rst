==============================
HubSpot to UniEconomy Dataflow
==============================

Generated: 2023-10-05 06:14:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to UniEconomy Companies
---------------------------------------
Every HubSpot Company will be synchronized with a UniEconomy Companies.

Once a link between a HubSpot Company and a UniEconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a UniEconomy Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - UniEconomy Companies Property
     - UniEconomy Data Type
   * - properties.name
     - Name
     - "string"
   * - updatedAt
     - UpdatedAt
     - "string"

