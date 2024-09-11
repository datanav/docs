=============================
Keap to Business Nxt Dataflow
=============================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to BusinessNxt Address
-------------------------------------
Every Keap Companies will be synchronized with a BusinessNxt Address.

Once a link between a Keap Companies and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - company_name
     - name
     - "string"


Keap Opportunity to BusinessNxt Order
-------------------------------------
Every Keap Opportunity will be synchronized with a BusinessNxt Order.

Once a link between a Keap Opportunity and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - opportunity_title
     - name
     - "string"


Keap Product to Business Nxt Product
------------------------------------
Every Keap Product will be synchronized with a Business Nxt Product.

Once a link between a Keap Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - product_desc
     - description
     - "string"
   * - product_price
     - priceQuantity
     - "string"

