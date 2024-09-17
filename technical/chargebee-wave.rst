==========================
Chargebee to Wave Dataflow
==========================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Wave Customer must be established.

A new Wave Customer will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Wave.

Once a link between a Chargebee Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"


Chargebee Customer to Wave Customer person
------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Wave Customer person must be established.

A new Wave Customer person will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Wave.

Once a link between a Chargebee Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer person Property
     - Wave Data Type


Chargebee Address to Wave Customer
----------------------------------
Every Chargebee Address will be synchronized with a Wave Customer.

Once a link between a Chargebee Address and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Wave Customer Property
     - Wave Data Type


Chargebee Address to Wave Customer person
-----------------------------------------
Every Chargebee Address will be synchronized with a Wave Customer person.

Once a link between a Chargebee Address and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Wave Customer person Property
     - Wave Data Type


Chargebee Customer to Wave Customer
-----------------------------------
Every Chargebee Customer will be synchronized with a Wave Customer.

Once a link between a Chargebee Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer Property
     - Wave Data Type


Chargebee Customer to Wave Customer person
------------------------------------------
Every Chargebee Customer will be synchronized with a Wave Customer person.

Once a link between a Chargebee Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer person Property
     - Wave Data Type


Chargebee Item to Wave Product
------------------------------
Every Chargebee Item will be synchronized with a Wave Product.

Once a link between a Chargebee Item and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Wave Product Property
     - Wave Data Type


Chargebee Order to Wave Invoice
-------------------------------
Every Chargebee Order will be synchronized with a Wave Invoice.

Once a link between a Chargebee Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Wave Invoice Property
     - Wave Data Type

