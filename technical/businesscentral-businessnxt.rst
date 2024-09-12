=========================================
Business Central to Business Nxt Dataflow
=========================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to Business Nxt Address
--------------------------------------------------
Every Business Central Companies will be synchronized with a Business Nxt Address.

Once a link between a Business Central Companies and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Business Nxt Address Property
     - Business Nxt Data Type


Business Central Salesorderlines to Business Nxt Order
------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Business Nxt Order.

Once a link between a Business Central Salesorderlines and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Business Central Salesquotes to Business Nxt Order
--------------------------------------------------
Every Business Central Salesquotes will be synchronized with a Business Nxt Order.

Once a link between a Business Central Salesquotes and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Business Central Currencies to Business Nxt Currency
----------------------------------------------------
Every Business Central Currencies will be synchronized with a Business Nxt Currency.

Once a link between a Business Central Currencies and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - code
     - isoCode
     - "string"
   * - displayName
     - name
     - "string"


Business Central Customers company to Business Nxt Address
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Business Nxt Address.

Once a link between a Business Central Customers company and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - displayName
     - name
     - "string"
   * - email
     - emailAddress
     - "string"
   * - phoneNumber
     - phone
     - "string"


Business Central Customers company to Business Nxt Company
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Business Nxt Company.

Once a link between a Business Central Customers company and a Business Nxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Business Nxt Company:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Business Nxt Company Property
     - Business Nxt Data Type
   * - displayName
     - name
     - "string"


Business Central Itemcategories to Business Nxt Productcategory
---------------------------------------------------------------
Every Business Central Itemcategories will be synchronized with a Business Nxt Productcategory.

Once a link between a Business Central Itemcategories and a Business Nxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Itemcategories and a Business Nxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Business Central Itemcategories Property
     - Business Nxt Productcategory Property
     - Business Nxt Data Type
   * - displayName
     - text
     - "string"


Business Central Items to Business Nxt Product
----------------------------------------------
Every Business Central Items will be synchronized with a Business Nxt Product.

Once a link between a Business Central Items and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - inventory
     - quantityPerUnit
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"


Business Central Salesorderlines to Business Nxt Orderline
----------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Business Nxt Orderline.

Once a link between a Business Central Salesorderlines and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - documentId
     - orderNo
     - "string"


Business Central Salesorders to Business Nxt Country
----------------------------------------------------
Every Business Central Salesorders will be synchronized with a Business Nxt Country.

Once a link between a Business Central Salesorders and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


Business Central Salesorders to Business Nxt Order
--------------------------------------------------
Every Business Central Salesorders will be synchronized with a Business Nxt Order.

Once a link between a Business Central Salesorders and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - orderDate
     - orderDate
     - "string"
   * - requestedDeliveryDate
     - dueDate
     - "string"


Business Central Salesquotes to Business Nxt Country
----------------------------------------------------
Every Business Central Salesquotes will be synchronized with a Business Nxt Country.

Once a link between a Business Central Salesquotes and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

