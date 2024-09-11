=============================
Business Nxt to Keap Dataflow
=============================

Generated: 2024-09-11 11:40:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Address to Keap Companies
-------------------------------------
Every BusinessNxt Address will be synchronized with a Keap Companies.

Once a link between a BusinessNxt Address and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


BusinessNxt Company to Keap Companies
-------------------------------------
Every BusinessNxt Company will be synchronized with a Keap Companies.

Once a link between a BusinessNxt Company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Business Nxt Product to Keap Product
------------------------------------
Every Business Nxt Product will be synchronized with a Keap Product.

Once a link between a Business Nxt Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - priceQuantity
     - product_price
     - "string"

