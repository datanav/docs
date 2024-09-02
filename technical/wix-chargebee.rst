====================
Wix.com to  Dataflow
====================

Generated: 2024-09-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Customer
-----------------------------
Every Wix.com Contacts will be synchronized with a  Customer.

Once a link between a Wix.com Contacts and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customer Property
     -  Data Type
   * - info.name.first
     - first_name
     - "string"
   * - info.name.last
     - last_name
     - "string"
   * - primaryInfo.email
     - email
     - "string"


Wix.com Orders to  Order
------------------------
Every Wix.com Orders will be synchronized with a  Order.

Once a link between a Wix.com Orders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Order Property
     -  Data Type
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


Wix.com Products to  Item
-------------------------
Every Wix.com Products will be synchronized with a  Item.

Once a link between a Wix.com Products and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Item:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Item Property
     -  Data Type
   * - name
     - name
     - "string"

