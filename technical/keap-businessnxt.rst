============================
Keap to Businessnxt Dataflow
============================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Businessnxt Address
-------------------------------------
Every Keap Companies will be synchronized with a Businessnxt Address.

Once a link between a Keap Companies and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - company_name
     - name
     - "string"


Keap Opportunity to Businessnxt Order
-------------------------------------
Every Keap Opportunity will be synchronized with a Businessnxt Order.

Once a link between a Keap Opportunity and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - opportunity_title
     - name
     - "string"


Keap Product to Businessnxt Product
-----------------------------------
Every Keap Product will be synchronized with a Businessnxt Product.

Once a link between a Keap Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - product_desc
     - description
     - "string"
   * - product_price
     - priceQuantity
     - "string"

