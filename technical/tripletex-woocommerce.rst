======================
Tripletex to  Dataflow
======================

Generated: 2024-07-04 09:58:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to  Orders
--------------------------
Every Tripletex Order will be synchronized with a  Orders.

Once a link between a Tripletex Order and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Orders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Orders Property
     -  Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Product to  Products
------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Products.

Once a link between a Tripletex Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Products Property
     -  Data Type
   * - costExcludingVatCurrency
     - price
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - sale_price
     - "string"

