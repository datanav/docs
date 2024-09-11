===============================================
Business Central to Visma Business Nxt Dataflow
===============================================

Generated: 2024-09-11 07:52:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Businessnxt Address
------------------------------------------------
Every Businesscentral Companies will be synchronized with a Businessnxt Address.

Once a link between a Businesscentral Companies and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Businessnxt Address Property
     - Businessnxt Data Type


Businesscentral Salesorderlines to Businessnxt Order
----------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Businessnxt Order.

Once a link between a Businesscentral Salesorderlines and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Businesscentral Salesquotes to Businessnxt Order
------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Businessnxt Order.

Once a link between a Businesscentral Salesquotes and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Business Currencies to Visma Currency
-------------------------------------
Every Business Currencies will be synchronized with a Visma Currency.

Once a link between a Business Currencies and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Currencies and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Business Currencies Property
     - Visma Currency Property
     - Visma Data Type
   * - code
     - isoCode
     - "string"
   * - displayName
     - name
     - "string"


Business Customers company to Visma Address
-------------------------------------------
Every Business Customers company will be synchronized with a Visma Address.

Once a link between a Business Customers company and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
     - Visma Address Property
     - Visma Data Type
   * - displayName
     - name
     - "string"
   * - email
     - emailAddress
     - "string"
   * - phoneNumber
     - phone
     - "string"


Business Customers company to Visma Company
-------------------------------------------
Every Business Customers company will be synchronized with a Visma Company.

Once a link between a Business Customers company and a Visma Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Visma Company:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
     - Visma Company Property
     - Visma Data Type
   * - displayName
     - name
     - "string"


Business Itemcategories to Visma Productcategory
------------------------------------------------
Every Business Itemcategories will be synchronized with a Visma Productcategory.

Once a link between a Business Itemcategories and a Visma Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Itemcategories and a Visma Productcategory:

.. list-table::
   :header-rows: 1

   * - Business Itemcategories Property
     - Visma Productcategory Property
     - Visma Data Type
   * - displayName
     - text
     - "string"


Business Items to Visma Product
-------------------------------
Every Business Items will be synchronized with a Visma Product.

Once a link between a Business Items and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - Visma Product Property
     - Visma Data Type
   * - inventory
     - quantityPerUnit
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"


Business Salesorderlines to Visma Orderline
-------------------------------------------
Every Business Salesorderlines will be synchronized with a Visma Orderline.

Once a link between a Business Salesorderlines and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - Visma Orderline Property
     - Visma Data Type
   * - documentId
     - orderNo
     - "string"


Business Salesorders to Visma Country
-------------------------------------
Every Business Salesorders will be synchronized with a Visma Country.

Once a link between a Business Salesorders and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
     - Visma Country Property
     - Visma Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


Business Salesorders to Visma Order
-----------------------------------
Every Business Salesorders will be synchronized with a Visma Order.

Once a link between a Business Salesorders and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
     - Visma Order Property
     - Visma Data Type
   * - orderDate
     - orderDate
     - "string"
   * - requestedDeliveryDate
     - dueDate
     - "string"


Business Salesquotes to Visma Country
-------------------------------------
Every Business Salesquotes will be synchronized with a Visma Country.

Once a link between a Business Salesquotes and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesquotes and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Business Salesquotes Property
     - Visma Country Property
     - Visma Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

