===================================
Chargebee to Powerofficego Dataflow
===================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Powerofficego Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Powerofficego.

Once a link between a Chargebee Customer and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - email
     - emailAddress
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"


Chargebee Customer to Powerofficego Customers
---------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Powerofficego.

Once a link between a Chargebee Customer and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Chargebee Customer to Powerofficego Customers person
----------------------------------------------------
Every Chargebee Customer will be synchronized with a Powerofficego Customers person.

Once a link between a Chargebee Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"


Chargebee Item to Powerofficego Product
---------------------------------------
Every Chargebee Item will be synchronized with a Powerofficego Product.

Once a link between a Chargebee Item and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Powerofficego Product Property
     - Powerofficego Data Type


Chargebee Order to Powerofficego Salesorders
--------------------------------------------
Every Chargebee Order will be synchronized with a Powerofficego Salesorders.

Once a link between a Chargebee Order and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - currency_code
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"

