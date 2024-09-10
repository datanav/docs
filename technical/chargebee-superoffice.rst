=================================
Chargebee to Superoffice Dataflow
=================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Superoffice Contact
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Superoffice Contact.

Once a link between a Chargebee Business_entity and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"


Chargebee Customer to Superoffice Person
----------------------------------------
Every Chargebee Customer will be synchronized with a Superoffice Person.

Once a link between a Chargebee Customer and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - email
     - Emails.Value
     - "string"
   * - first_name
     - Firstname
     - "string"
   * - last_name
     - Lastname
     - "string"


Chargebee Item to Superoffice Product
-------------------------------------
Every Chargebee Item will be synchronized with a Superoffice Product.

Once a link between a Chargebee Item and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Superoffice Product Property
     - Superoffice Data Type

