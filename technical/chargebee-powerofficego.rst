====================================
Chargebee to PowerOffice GO Dataflow
====================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to PowerOffice GO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into PowerOffice GO.

Once a link between a Chargebee Customer and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - email
     - emailAddress
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"


Chargebee Customer to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into PowerOffice GO.

Once a link between a Chargebee Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Chargebee Customer to PowerOffice GO Customers person
-----------------------------------------------------
Every Chargebee Customer will be synchronized with a PowerOffice GO Customers person.

Once a link between a Chargebee Customer and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"


Chargebee Item to PowerOffice GO Product
----------------------------------------
Every Chargebee Item will be synchronized with a PowerOffice GO Product.

Once a link between a Chargebee Item and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type


Chargebee Order to PowerOffice GO Salesorders
---------------------------------------------
Every Chargebee Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Chargebee Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - currency_code
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"

