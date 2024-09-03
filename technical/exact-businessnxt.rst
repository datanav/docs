==================
Exact to  Dataflow
==================

Generated: 2024-09-03 08:16:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Addresses to  Country
---------------------------
Every Exact Addresses will be synchronized with a  Country.

Once a link between a Exact Addresses and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a  Country:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     -  Country Property
     -  Data Type
   * - CountryName
     - name
     - "string"


Exact Currencies to  Currency
-----------------------------
Every Exact Currencies will be synchronized with a  Currency.

Once a link between a Exact Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     -  Currency Property
     -  Data Type
   * - Description
     - name
     - "string"


Exact Items to  Product
-----------------------
Every Exact Items will be synchronized with a  Product.

Once a link between a Exact Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Product Property
     -  Data Type


Exact Salesorderlines to  Orderline
-----------------------------------
Every Exact Salesorderlines will be synchronized with a  Orderline.

Once a link between a Exact Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Orderline Property
     -  Data Type


Exact Salesorders to  Order
---------------------------
Every Exact Salesorders will be synchronized with a  Order.

Once a link between a Exact Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     -  Order Property
     -  Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"

