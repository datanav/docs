======================
Tripletex to  Dataflow
======================

Generated: 2024-09-02 11:16:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - priceExcludingVatCurrency
     - product_price
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
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - priceExcludingVatCurrency
     - product_price
     - "string"

