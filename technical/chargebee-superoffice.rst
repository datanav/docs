=================================
Chargebee to SuperOffice Dataflow
=================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to SuperOffice Contact
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a SuperOffice Contact.

Once a link between a Chargebee Business_entity and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


Chargebee Customer to SuperOffice Person
----------------------------------------
Every Chargebee Customer will be synchronized with a SuperOffice Person.

Once a link between a Chargebee Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - email
     - Emails.Value
     - "string"
   * - first_name
     - Firstname
     - "string"
   * - last_name
     - Lastname
     - "string"


Chargebee Item to SuperOffice Product
-------------------------------------
Every Chargebee Item will be synchronized with a SuperOffice Product.

Once a link between a Chargebee Item and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - SuperOffice Product Property
     - SuperOffice Data Type

