================================
Chargebee to Membercare Dataflow
================================

Generated: 2024-09-03 09:02:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Membercare Countries
-----------------------------------------
Every Chargebee Address will be synchronized with a Membercare Countries.

Once a link between a Chargebee Address and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Membercare Countries Property
     - Membercare Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to Membercare Companies
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Membercare Companies.

Once a link between a Chargebee Business_entity and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Chargebee Customer to Membercare Countries
------------------------------------------
Every Chargebee Customer will be synchronized with a Membercare Countries.

Once a link between a Chargebee Customer and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billing_address.country
     - name
     - "string"

