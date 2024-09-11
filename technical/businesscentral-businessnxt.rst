=======================================
BusinessCentral to BusinessNxt Dataflow
=======================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Companies to Visma Address
-----------------------------------
Every Business Companies will be synchronized with a Visma Address.

Once a link between a Business Companies and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - Visma Address Property
     - Visma Data Type


Business Salesorderlines to Visma Order
---------------------------------------
Every Business Salesorderlines will be synchronized with a Visma Order.

Once a link between a Business Salesorderlines and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - Visma Order Property
     - Visma Data Type


Business Salesquotes to Visma Order
-----------------------------------
Every Business Salesquotes will be synchronized with a Visma Order.

Once a link between a Business Salesquotes and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesquotes and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Business Salesquotes Property
     - Visma Order Property
     - Visma Data Type


BusinessCentral Currencies to BusinessNxt Currency
--------------------------------------------------
Every BusinessCentral Currencies will be synchronized with a BusinessNxt Currency.

Once a link between a BusinessCentral Currencies and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Currencies and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Currencies Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - code
     - isoCode
     - "string"
   * - displayName
     - name
     - "string"


BusinessCentral Customers company to BusinessNxt Address
--------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a BusinessNxt Address.

Once a link between a BusinessCentral Customers company and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - displayName
     - name
     - "string"
   * - email
     - emailAddress
     - "string"
   * - phoneNumber
     - phone
     - "string"


BusinessCentral Customers company to BusinessNxt Company
--------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a BusinessNxt Company.

Once a link between a BusinessCentral Customers company and a BusinessNxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a BusinessNxt Company:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - BusinessNxt Company Property
     - BusinessNxt Data Type
   * - displayName
     - name
     - "string"


BusinessCentral Itemcategories to BusinessNxt Productcategory
-------------------------------------------------------------
Every BusinessCentral Itemcategories will be synchronized with a BusinessNxt Productcategory.

Once a link between a BusinessCentral Itemcategories and a BusinessNxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Itemcategories and a BusinessNxt Productcategory:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Itemcategories Property
     - BusinessNxt Productcategory Property
     - BusinessNxt Data Type
   * - displayName
     - text
     - "string"


BusinessCentral Items to BusinessNxt Product
--------------------------------------------
Every BusinessCentral Items will be synchronized with a BusinessNxt Product.

Once a link between a BusinessCentral Items and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - inventory
     - quantityPerUnit
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"


BusinessCentral Salesorderlines to BusinessNxt Orderline
--------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a BusinessNxt Orderline.

Once a link between a BusinessCentral Salesorderlines and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - documentId
     - orderNo
     - "string"


BusinessCentral Salesorders to BusinessNxt Country
--------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a BusinessNxt Country.

Once a link between a BusinessCentral Salesorders and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


BusinessCentral Salesorders to BusinessNxt Order
------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a BusinessNxt Order.

Once a link between a BusinessCentral Salesorders and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - orderDate
     - orderDate
     - "string"
   * - requestedDeliveryDate
     - dueDate
     - "string"


BusinessCentral Salesquotes to BusinessNxt Country
--------------------------------------------------
Every BusinessCentral Salesquotes will be synchronized with a BusinessNxt Country.

Once a link between a BusinessCentral Salesquotes and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesquotes and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesquotes Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

