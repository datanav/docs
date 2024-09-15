=============================
Chargebee to HubSpot Dataflow
=============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to HubSpot Company
--------------------------------------------
Every Chargebee Business_entity will be synchronized with a HubSpot Company.

Once a link between a Chargebee Business_entity and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


Chargebee Customer to HubSpot Contact
-------------------------------------
Every Chargebee Customer will be synchronized with a HubSpot Contact.

Once a link between a Chargebee Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.email
     - "string"
   * - first_name
     - properties.firstname
     - "string"
   * - last_name
     - properties.lastname
     - "string"


Chargebee Item to HubSpot Product
---------------------------------
Every Chargebee Item will be synchronized with a HubSpot Product.

Once a link between a Chargebee Item and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - HubSpot Product Property
     - HubSpot Data Type

