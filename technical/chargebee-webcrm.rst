============================
Chargebee to Webcrm Dataflow
============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Webcrm Organisations
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Webcrm Organisations.

Once a link between a Chargebee Business_entity and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"


Chargebee Item to Webcrm Products
---------------------------------
Every Chargebee Item will be synchronized with a Webcrm Products.

Once a link between a Chargebee Item and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Webcrm Products Property
     - Webcrm Data Type

