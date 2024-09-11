============================
BusinessNxt to Keap Dataflow
============================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Keap Companies
-------------------------------
Every Visma Address will be synchronized with a Keap Companies.

Once a link between a Visma Address and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Visma Company to Keap Companies
-------------------------------
Every Visma Company will be synchronized with a Keap Companies.

Once a link between a Visma Company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Visma Product to Keap Product
-----------------------------
Every Visma Product will be synchronized with a Keap Product.

Once a link between a Visma Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - priceQuantity
     - product_price
     - "string"

