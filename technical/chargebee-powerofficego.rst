====================================
Chargebee to PowerOffice GO Dataflow
====================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Chargebee Customer to PowerOffice Customers person
--------------------------------------------------
Every Chargebee Customer will be synchronized with a PowerOffice Customers person.

Once a link between a Chargebee Customer and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"


Chargebee Item to PowerOffice Product
-------------------------------------
Every Chargebee Item will be synchronized with a PowerOffice Product.

Once a link between a Chargebee Item and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - PowerOffice Product Property
     - PowerOffice Data Type


Chargebee Order to PowerOffice Salesorders
------------------------------------------
Every Chargebee Order will be synchronized with a PowerOffice Salesorders.

Once a link between a Chargebee Order and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - currency_code
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"

