=====================================
Chargebee to BusinessCentral Dataflow
=====================================

Generated: 2024-09-11 08:39:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to BusinessCentral Customers company
-------------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into BusinessCentral.

Once a link between a Chargebee Customer and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type


Chargebee Business_entity to Businesscentral Companies
------------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Businesscentral Companies.

Once a link between a Chargebee Business_entity and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Chargebee Customer to BusinessCentral Customers person
------------------------------------------------------
Every Chargebee Customer will be synchronized with a BusinessCentral Customers person.

Once a link between a Chargebee Customer and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
   * - email
     - email
     - "string"


Chargebee Item to BusinessCentral Items
---------------------------------------
Every Chargebee Item will be synchronized with a BusinessCentral Items.

Once a link between a Chargebee Item and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type


Chargebee Order to BusinessCentral Salesorders
----------------------------------------------
Every Chargebee Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a Chargebee Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
   * - currency_code
     - currencyId
     - "string"
   * - customer_id
     - customerId
     - "string"

