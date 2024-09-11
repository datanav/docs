=============================================
PowerOffice GO to Visma Business Nxt Dataflow
=============================================

Generated: 2024-09-11 07:52:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


PowerOffice Contactperson to Visma Country
------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Visma Country.

Once a link between a PowerOffice Contactperson and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Visma Country Property
     - Visma Data Type
   * - residenceCountryCode
     - isoCode
     - "string"


PowerOffice Currency to Visma Currency
--------------------------------------
Every PowerOffice Currency will be synchronized with a Visma Currency.

Once a link between a PowerOffice Currency and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Currency and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - PowerOffice Currency Property
     - Visma Currency Property
     - Visma Data Type


PowerOffice Customers to Visma Country
--------------------------------------
Every PowerOffice Customers will be synchronized with a Visma Country.

Once a link between a PowerOffice Customers and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Visma Country Property
     - Visma Data Type
   * - MailAddress.CountryCode
     - isoCode
     - "string"


PowerOffice Location to Visma Country
-------------------------------------
Every PowerOffice Location will be synchronized with a Visma Country.

Once a link between a PowerOffice Location and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Location and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Location Property
     - Visma Country Property
     - Visma Data Type


PowerOffice Outgoinginvoices to Visma Country
---------------------------------------------
Every PowerOffice Outgoinginvoices will be synchronized with a Visma Country.

Once a link between a PowerOffice Outgoinginvoices and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Outgoinginvoices and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Outgoinginvoices Property
     - Visma Country Property
     - Visma Data Type


PowerOffice Product to Visma Product
------------------------------------
Every PowerOffice Product will be synchronized with a Visma Product.

Once a link between a PowerOffice Product and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Visma Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - Visma Product Property
     - Visma Data Type
   * - availableStock
     - quantityPerUnit
     - "string"
   * - description
     - description
     - "string"
   * - salesPrice
     - priceQuantity
     - "string"


PowerOffice Productgroup to Visma Productcategory
-------------------------------------------------
Every PowerOffice Productgroup will be synchronized with a Visma Productcategory.

Once a link between a PowerOffice Productgroup and a Visma Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Productgroup and a Visma Productcategory:

.. list-table::
   :header-rows: 1

   * - PowerOffice Productgroup Property
     - Visma Productcategory Property
     - Visma Data Type
   * - name
     - text
     - "string"


PowerOffice Salesorderlines to Visma Orderline
----------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Visma Orderline.

Once a link between a PowerOffice Salesorderlines and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
     - Visma Orderline Property
     - Visma Data Type
   * - sesam_SalesOrderId
     - orderNo
     - "string"


PowerOffice Salesorders to Visma Order
--------------------------------------
Every PowerOffice Salesorders will be synchronized with a Visma Order.

Once a link between a PowerOffice Salesorders and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a Visma Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
     - Visma Order Property
     - Visma Data Type
   * - SalesOrderDate
     - orderDate
     - "string"


PowerOffice Suppliers to Visma Country
--------------------------------------
Every PowerOffice Suppliers will be synchronized with a Visma Country.

Once a link between a PowerOffice Suppliers and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Suppliers and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Suppliers Property
     - Visma Country Property
     - Visma Data Type


PowerOffice Suppliers person to Visma Country
---------------------------------------------
Every PowerOffice Suppliers person will be synchronized with a Visma Country.

Once a link between a PowerOffice Suppliers person and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Suppliers person and a Visma Country:

.. list-table::
   :header-rows: 1

   * - PowerOffice Suppliers person Property
     - Visma Country Property
     - Visma Data Type

