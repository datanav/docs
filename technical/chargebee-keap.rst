==========================
Chargebee to Keap Dataflow
==========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Keap Companies
-------------------------------------------
Every Chargebee Business_entity will be synchronized with a Keap Companies.

Once a link between a Chargebee Business_entity and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Chargebee Customer to Keap Contacts
-----------------------------------
Every Chargebee Customer will be synchronized with a Keap Contacts.

Once a link between a Chargebee Customer and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Keap Contacts Property
     - Keap Data Type


Chargebee Item to Keap Product
------------------------------
Every Chargebee Item will be synchronized with a Keap Product.

Once a link between a Chargebee Item and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Keap Product Property
     - Keap Data Type

