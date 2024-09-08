=============================
Chargebee to Hubspot Dataflow
=============================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Hubspot Company
--------------------------------------------
Every Chargebee Business_entity will be synchronized with a Hubspot Company.

Once a link between a Chargebee Business_entity and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"


Chargebee Customer to Hubspot Contact
-------------------------------------
Every Chargebee Customer will be synchronized with a Hubspot Contact.

Once a link between a Chargebee Customer and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - email
     - properties.email
     - "string"
   * - first_name
     - properties.firstname
     - "string"
   * - last_name
     - properties.lastname
     - "string"


Chargebee Item to Hubspot Product
---------------------------------
Every Chargebee Item will be synchronized with a Hubspot Product.

Once a link between a Chargebee Item and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Hubspot Product Property
     - Hubspot Data Type

