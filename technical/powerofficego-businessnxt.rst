==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-29 08:00:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Address
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Address.

Once a link between a Powerofficego Customers and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Address Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"


Powerofficego Departments to  Address
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Address.

Once a link between a Powerofficego Departments and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Address Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Salesorderlines to  Order
---------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Order.

Once a link between a Powerofficego Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Order Property
     -  Data Type


Powerofficego Contactperson to  Country
---------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Country.

Once a link between a Powerofficego Contactperson and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Country Property
     -  Data Type
   * - residenceCountryCode
     - isoCode
     - "string"


Powerofficego Currency to  Currency
-----------------------------------
Every Powerofficego Currency will be synchronized with a  Currency.

Once a link between a Powerofficego Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     -  Currency Property
     -  Data Type


Powerofficego Customers to  Country
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Country.

Once a link between a Powerofficego Customers and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Country Property
     -  Data Type
   * - MailAddress.CountryCode
     - isoCode
     - "string"


Powerofficego Location to  Country
----------------------------------
Every Powerofficego Location will be synchronized with a  Country.

Once a link between a Powerofficego Location and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     -  Country Property
     -  Data Type


Powerofficego Outgoinginvoices to  Country
------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a  Country.

Once a link between a Powerofficego Outgoinginvoices and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     -  Country Property
     -  Data Type


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
   * - availableStock
     - quantityPerUnit
     - "string"
   * - description
     - description
     - "string"
   * - salesPrice
     - priceQuantity
     - "string"


Powerofficego Productgroup to  Productcategory
----------------------------------------------
Every Powerofficego Productgroup will be synchronized with a  Productcategory.

Once a link between a Powerofficego Productgroup and a  Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a  Productcategory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     -  Productcategory Property
     -  Data Type
   * - name
     - text
     - "string"


Powerofficego Salesorderlines to  Orderline
-------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Orderline.

Once a link between a Powerofficego Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Orderline Property
     -  Data Type
   * - sesam_SalesOrderId
     - orderNo
     - "string"


Powerofficego Salesorders to  Order
-----------------------------------
Every Powerofficego Salesorders will be synchronized with a  Order.

Once a link between a Powerofficego Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Order Property
     -  Data Type
   * - SalesOrderDate
     - orderDate
     - "string"


Powerofficego Suppliers to  Country
-----------------------------------
Every Powerofficego Suppliers will be synchronized with a  Country.

Once a link between a Powerofficego Suppliers and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     -  Country Property
     -  Data Type


Powerofficego Suppliers person to  Country
------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Country.

Once a link between a Powerofficego Suppliers person and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Country Property
     -  Data Type

