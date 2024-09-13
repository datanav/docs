=============================
Wix.com to Chargebee Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Chargebee Customer
--------------------------------------
Every Wix.com Contacts will be synchronized with a Chargebee Customer.

Once a link between a Wix.com Contacts and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - info.name.first
     - first_name
     - "string"
   * - info.name.last
     - last_name
     - "string"
   * - primaryInfo.email
     - email
     - "string"


Wix.com Orders to Chargebee Order
---------------------------------
Every Wix.com Orders will be synchronized with a Chargebee Order.

Once a link between a Wix.com Orders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - buyerInfo.id
     - customer_id
     - "string"
   * - currency
     - currency_code
     - "string"
   * - lineItems.price
     - order_line_items.unit_price
     - "string"
   * - lineItems.quantity
     - order_line_items.amount
     - "string"


Wix.com Products to Chargebee Item
----------------------------------
Every Wix.com Products will be synchronized with a Chargebee Item.

Once a link between a Wix.com Products and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - name
     - name
     - "string"

