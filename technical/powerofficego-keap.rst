==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-09-02 11:16:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to  Product
---------------------------------
Every Powerofficego Product will be synchronized with a  Product.

Once a link between a Powerofficego Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Product Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - salesPrice
     - product_price
     - "string"


Powerofficego Product to  Products
----------------------------------
Every Powerofficego Product will be synchronized with a  Products.

Once a link between a Powerofficego Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Products Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - salesPrice
     - product_price
     - "string"

