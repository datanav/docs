============================
Businessnxt to Keap Dataflow
============================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Keap Companies
-------------------------------------
Every Businessnxt Address will be synchronized with a Keap Companies.

Once a link between a Businessnxt Address and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Businessnxt Company to Keap Companies
-------------------------------------
Every Businessnxt Company will be synchronized with a Keap Companies.

Once a link between a Businessnxt Company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Businessnxt Product to Keap Product
-----------------------------------
Every Businessnxt Product will be synchronized with a Keap Product.

Once a link between a Businessnxt Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - priceQuantity
     - product_price
     - "string"

