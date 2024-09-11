======================================
Visma Business Nxt to Hubspot Dataflow
======================================

Generated: 2024-09-11 07:47:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Hubspot Company
--------------------------------------
Every Businessnxt Address will be synchronized with a Hubspot Company.

Once a link between a Businessnxt Address and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"
   * - phone
     - properties.phone
     - "string"


Businessnxt Company to Hubspot Company
--------------------------------------
Every Businessnxt Company will be synchronized with a Hubspot Company.

Once a link between a Businessnxt Company and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"


Visma Orderline to Hubspot Lineitem
-----------------------------------
Every Visma Orderline will be synchronized with a Hubspot Lineitem.

Once a link between a Visma Orderline and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


Visma Product to Hubspot Product
--------------------------------
Every Visma Product will be synchronized with a Hubspot Product.

Once a link between a Visma Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - description
     - properties.description
     - "string"
   * - priceQuantity
     - properties.price
     - "string"

