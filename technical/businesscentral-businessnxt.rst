=======================================
Businesscentral to Businessnxt Dataflow
=======================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Businesscentral Currencies to Businessnxt Currency
--------------------------------------------------
Every Businesscentral Currencies will be synchronized with a Businessnxt Currency.

Once a link between a Businesscentral Currencies and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - code
     - isoCode
     - "string"
   * - displayName
     - name
     - "string"


Businesscentral Customers company to Businessnxt Address
--------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Businessnxt Address.

Once a link between a Businesscentral Customers company and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - displayName
     - name
     - "string"
   * - email
     - emailAddress
     - "string"
   * - phoneNumber
     - phone
     - "string"


Businesscentral Customers company to Businessnxt Company
--------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Businessnxt Company.

Once a link between a Businesscentral Customers company and a Businessnxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Businessnxt Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Businessnxt Company Property
     - Businessnxt Data Type
   * - displayName
     - name
     - "string"


Businesscentral Itemcategories to Businessnxt Productcategory
-------------------------------------------------------------
Every Businesscentral Itemcategories will be synchronized with a Businessnxt Productcategory.

Once a link between a Businesscentral Itemcategories and a Businessnxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Itemcategories and a Businessnxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Businesscentral Itemcategories Property
     - Businessnxt Productcategory Property
     - Businessnxt Data Type
   * - displayName
     - text
     - "string"


Businesscentral Items to Businessnxt Product
--------------------------------------------
Every Businesscentral Items will be synchronized with a Businessnxt Product.

Once a link between a Businesscentral Items and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - inventory
     - quantityPerUnit
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"


Businesscentral Salesorderlines to Businessnxt Orderline
--------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Businessnxt Orderline.

Once a link between a Businesscentral Salesorderlines and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - documentId
     - orderNo
     - "string"


Businesscentral Salesorders to Businessnxt Country
--------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Businessnxt Country.

Once a link between a Businesscentral Salesorders and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


Businesscentral Salesorders to Businessnxt Order
------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Businessnxt Order.

Once a link between a Businesscentral Salesorders and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - orderDate
     - orderDate
     - "string"
   * - requestedDeliveryDate
     - dueDate
     - "string"


Businesscentral Salesquotes to Businessnxt Country
--------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Businessnxt Country.

Once a link between a Businesscentral Salesquotes and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

