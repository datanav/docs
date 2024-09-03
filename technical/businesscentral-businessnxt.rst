============================
Businesscentral to  Dataflow
============================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Address
-------------------------------------
Every Businesscentral Companies will be synchronized with a  Address.

Once a link between a Businesscentral Companies and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Address:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Address Property
     -  Data Type


Businesscentral Salesorderlines to  Order
-----------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Order.

Once a link between a Businesscentral Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Order Property
     -  Data Type


Businesscentral Salesquotes to  Order
-------------------------------------
Every Businesscentral Salesquotes will be synchronized with a  Order.

Once a link between a Businesscentral Salesquotes and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     -  Order Property
     -  Data Type


Businesscentral Currencies to  Currency
---------------------------------------
Every Businesscentral Currencies will be synchronized with a  Currency.

Once a link between a Businesscentral Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
     -  Data Type
   * - code
     - isoCode
     - "string"
   * - displayName
     - name
     - "string"


Businesscentral Customers company to  Address
---------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Address.

Once a link between a Businesscentral Customers company and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Address:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Address Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - email
     - emailAddress
     - "string"
   * - phoneNumber
     - phone
     - "string"


Businesscentral Customers company to  Company
---------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Company.

Once a link between a Businesscentral Customers company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Company Property
     -  Data Type
   * - displayName
     - name
     - "string"


Businesscentral Itemcategories to  Productcategory
--------------------------------------------------
Every Businesscentral Itemcategories will be synchronized with a  Productcategory.

Once a link between a Businesscentral Itemcategories and a  Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Itemcategories and a  Productcategory:

.. list-table::
   :header-rows: 1

   * - Businesscentral Itemcategories Property
     -  Productcategory Property
     -  Data Type
   * - displayName
     - text
     - "string"


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
   * - inventory
     - quantityPerUnit
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"


Businesscentral Salesorderlines to  Orderline
---------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Orderline.

Once a link between a Businesscentral Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Orderline Property
     -  Data Type
   * - documentId
     - orderNo
     - "string"


Businesscentral Salesorders to  Country
---------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Country.

Once a link between a Businesscentral Salesorders and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Country Property
     -  Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


Businesscentral Salesorders to  Order
-------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Order.

Once a link between a Businesscentral Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Order Property
     -  Data Type
   * - orderDate
     - orderDate
     - "string"
   * - requestedDeliveryDate
     - dueDate
     - "string"


Businesscentral Salesquotes to  Country
---------------------------------------
Every Businesscentral Salesquotes will be synchronized with a  Country.

Once a link between a Businesscentral Salesquotes and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a  Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     -  Country Property
     -  Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

