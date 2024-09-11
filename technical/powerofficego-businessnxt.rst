=====================================
PowerOfficeGO to BusinessNxt Dataflow
=====================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Customers to Visma Address
--------------------------------------
Every PowerOffice Customers will be synchronized with a Visma Address.

Once a link between a PowerOffice Customers and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Visma Address:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Visma Address Property
     - Visma Data Type
   * - Name
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"


PowerOffice Departments to Visma Address
----------------------------------------
Every PowerOffice Departments will be synchronized with a Visma Address.

Once a link between a PowerOffice Departments and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a Visma Address:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - Visma Address Property
     - Visma Data Type
   * - Name
     - name
     - "string"


PowerOffice Salesorderlines to Visma Order
------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Visma Order.

Once a link between a PowerOffice Salesorderlines and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Visma Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
     - Visma Order Property
     - Visma Data Type


PowerOfficeGO Contactperson to BusinessNxt Country
--------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Contactperson and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - residenceCountryCode
     - isoCode
     - "string"


PowerOfficeGO Currency to BusinessNxt Currency
----------------------------------------------
Every PowerOfficeGO Currency will be synchronized with a BusinessNxt Currency.

Once a link between a PowerOfficeGO Currency and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Currency and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Currency Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type


PowerOfficeGO Customers to BusinessNxt Country
----------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Customers and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - MailAddress.CountryCode
     - isoCode
     - "string"


PowerOfficeGO Location to BusinessNxt Country
---------------------------------------------
Every PowerOfficeGO Location will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Location and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Location and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Location Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


PowerOfficeGO Outgoinginvoices to BusinessNxt Country
-----------------------------------------------------
Every PowerOfficeGO Outgoinginvoices will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Outgoinginvoices and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Outgoinginvoices and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Outgoinginvoices Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


PowerOfficeGO Product to BusinessNxt Product
--------------------------------------------
Every PowerOfficeGO Product will be synchronized with a BusinessNxt Product.

Once a link between a PowerOfficeGO Product and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - availableStock
     - quantityPerUnit
     - "string"
   * - description
     - description
     - "string"
   * - salesPrice
     - priceQuantity
     - "string"


PowerOfficeGO Productgroup to BusinessNxt Productcategory
---------------------------------------------------------
Every PowerOfficeGO Productgroup will be synchronized with a BusinessNxt Productcategory.

Once a link between a PowerOfficeGO Productgroup and a BusinessNxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Productgroup and a BusinessNxt Productcategory:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Productgroup Property
     - BusinessNxt Productcategory Property
     - BusinessNxt Data Type
   * - name
     - text
     - "string"


PowerOfficeGO Salesorderlines to BusinessNxt Orderline
------------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a BusinessNxt Orderline.

Once a link between a PowerOfficeGO Salesorderlines and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - sesam_SalesOrderId
     - orderNo
     - "string"


PowerOfficeGO Salesorders to BusinessNxt Order
----------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a BusinessNxt Order.

Once a link between a PowerOfficeGO Salesorders and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - SalesOrderDate
     - orderDate
     - "string"


PowerOfficeGO Suppliers to BusinessNxt Country
----------------------------------------------
Every PowerOfficeGO Suppliers will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Suppliers and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


PowerOfficeGO Suppliers person to BusinessNxt Country
-----------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a BusinessNxt Country.

Once a link between a PowerOfficeGO Suppliers person and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type

