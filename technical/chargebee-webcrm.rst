============================
Chargebee to WebCRM Dataflow
============================

Generated: 2024-09-28 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to WebCRM Organisations
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a WebCRM Organisations.

Once a link between a Chargebee Business_entity and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"


Chargebee Item to WebCRM Products
---------------------------------
Every Chargebee Item will be synchronized with a WebCRM Products.

Once a link between a Chargebee Item and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - WebCRM Products Property
     - WebCRM Data Type

