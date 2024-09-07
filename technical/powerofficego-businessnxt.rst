=====================================
Powerofficego to Businessnxt Dataflow
=====================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Businessnxt Address
----------------------------------------------
Every Powerofficego Customers will be synchronized with a Businessnxt Address.

Once a link between a Powerofficego Customers and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"


Powerofficego Departments to Businessnxt Address
------------------------------------------------
Every Powerofficego Departments will be synchronized with a Businessnxt Address.

Once a link between a Powerofficego Departments and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"


Powerofficego Salesorderlines to Businessnxt Order
--------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Businessnxt Order.

Once a link between a Powerofficego Salesorderlines and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Powerofficego Contactperson to Businessnxt Country
--------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Contactperson and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - residenceCountryCode
     - isoCode
     - "string"


Powerofficego Currency to Businessnxt Currency
----------------------------------------------
Every Powerofficego Currency will be synchronized with a Businessnxt Currency.

Once a link between a Powerofficego Currency and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Businessnxt Currency Property
     - Businessnxt Data Type


Powerofficego Customers to Businessnxt Country
----------------------------------------------
Every Powerofficego Customers will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Customers and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - MailAddress.CountryCode
     - isoCode
     - "string"


Powerofficego Location to Businessnxt Country
---------------------------------------------
Every Powerofficego Location will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Location and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Powerofficego Outgoinginvoices to Businessnxt Country
-----------------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Outgoinginvoices and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Powerofficego Product to Businessnxt Product
--------------------------------------------
Every Powerofficego Product will be synchronized with a Businessnxt Product.

Once a link between a Powerofficego Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - availableStock
     - quantityPerUnit
     - "string"
   * - description
     - description
     - "string"
   * - salesPrice
     - priceQuantity
     - "string"


Powerofficego Productgroup to Businessnxt Productcategory
---------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a Businessnxt Productcategory.

Once a link between a Powerofficego Productgroup and a Businessnxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a Businessnxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - Businessnxt Productcategory Property
     - Businessnxt Data Type
   * - name
     - text
     - "string"


Powerofficego Salesorderlines to Businessnxt Orderline
------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Businessnxt Orderline.

Once a link between a Powerofficego Salesorderlines and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - sesam_SalesOrderId
     - orderNo
     - "string"


Powerofficego Salesorders to Businessnxt Order
----------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Businessnxt Order.

Once a link between a Powerofficego Salesorders and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - SalesOrderDate
     - orderDate
     - "string"


Powerofficego Suppliers to Businessnxt Country
----------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Suppliers and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Powerofficego Suppliers person to Businessnxt Country
-----------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Businessnxt Country.

Once a link between a Powerofficego Suppliers person and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Businessnxt Country Property
     - Businessnxt Data Type

