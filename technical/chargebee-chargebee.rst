===============================
Chargebee to Chargebee Dataflow
===============================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Item_family to Chargebee Currency
-------------------------------------------
Every Chargebee Item_family will be synchronized with a Chargebee Currency.

Once a link between a Chargebee Item_family and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Chargebee Currency Property
     - Chargebee Data Type


Chargebee Address to Chargebee Customer
---------------------------------------
Every Chargebee Address will be synchronized with a Chargebee Customer.

Once a link between a Chargebee Address and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - addr
     - billing_address.line1
     - "string"
   * - city
     - billing_address.city
     - "string"
   * - country
     - billing_address.country
     - "string"
   * - subscription_id
     - id
     - "string"
   * - zip
     - billing_address.zip
     - "string"


Chargebee Customer to Chargebee Address
---------------------------------------
Every Chargebee Customer will be synchronized with a Chargebee Address.

Once a link between a Chargebee Customer and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Chargebee Address Property
     - Chargebee Data Type
   * - billing_address.country
     - country
     - "string"

