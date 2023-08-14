=========================================
Powerofficego to PowerOfficeGov1 Dataflow
=========================================

Generated: 2023-08-14 08:50:56

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to PowerOfficeGov1 Department
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGov1 Department must be established.

A new PowerOfficeGov1 Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee that is synchronized into PowerOfficeGov1.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


Powerofficego Contactperson to PowerOfficeGov1 Contactperson
------------------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Powerofficego Contactperson and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type


Powerofficego Customer to PowerOfficeGov1 Contactperson
-------------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Contactperson.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Contactperson Property
     - PowerOfficeGov1 Data Type


Powerofficego Customer to PowerOfficeGov1 Customer
--------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Customer.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type


Powerofficego Customer to PowerOfficeGov1 Customers
---------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGov1 Customers.

Once a link between a Powerofficego Customer and a PowerOfficeGov1 Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGov1 Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGov1 Customers Property
     - PowerOfficeGov1 Data Type


Powerofficego Employee to PowerOfficeGov1 Employee
--------------------------------------------------
Every Powerofficego Employee will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Powerofficego Employee will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Powerofficego Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
   * - SocialSecurityNumber
     - SocialSecurityNumber
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


Powerofficego Outgoinginvoice to PowerOfficeGov1 Invoice
--------------------------------------------------------
Every Powerofficego Outgoinginvoice will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type


Powerofficego Outgoinginvoice to PowerOfficeGov1 Outgoinginvoice
----------------------------------------------------------------
Every Powerofficego Outgoinginvoice will be synchronized with a PowerOfficeGov1 Outgoinginvoice.

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGov1 Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGov1 Outgoinginvoice Property
     - PowerOfficeGov1 Data Type


Powerofficego Product to PowerOfficeGov1 Product
------------------------------------------------
Every Powerofficego Product will be synchronized with a PowerOfficeGov1 Product.

If a matching PowerOfficeGov1 Product already exists, the Powerofficego Product will be merged with the existing one.
If no matching PowerOfficeGov1 Product is found, a new PowerOfficeGov1 Product will be created.

A Powerofficego Product will merge with a PowerOfficeGov1 Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
   * - id
     - id

Once a link between a Powerofficego Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type


Powerofficego Product to PowerOfficeGov1 Productunit
----------------------------------------------------
Every Powerofficego Product will be synchronized with a PowerOfficeGov1 Productunit.

If a matching PowerOfficeGov1 Productunit already exists, the Powerofficego Product will be merged with the existing one.
If no matching PowerOfficeGov1 Productunit is found, a new PowerOfficeGov1 Productunit will be created.

A Powerofficego Product will merge with a PowerOfficeGov1 Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
   * - unitOfMeasureCode
     - name

Once a link between a Powerofficego Product and a PowerOfficeGov1 Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a PowerOfficeGov1 Productunit:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - PowerOfficeGov1 Productunit Property
     - PowerOfficeGov1 Data Type


Powerofficego Productgroup to PowerOfficeGov1 Listproductcategoryitems
----------------------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a PowerOfficeGov1 Listproductcategoryitems.

Once a link between a Powerofficego Productgroup and a PowerOfficeGov1 Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a PowerOfficeGov1 Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - PowerOfficeGov1 Listproductcategoryitems Property
     - PowerOfficeGov1 Data Type


Powerofficego Productgroup to PowerOfficeGov1 Productgroup
----------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a PowerOfficeGov1 Productgroup.

Once a link between a Powerofficego Productgroup and a PowerOfficeGov1 Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a PowerOfficeGov1 Productgroup:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - PowerOfficeGov1 Productgroup Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorder to PowerOfficeGov1 Invoice
---------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorder to PowerOfficeGov1 Order
-------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Order.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Order Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorder to PowerOfficeGov1 Salesorder
------------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Powerofficego Salesorder and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorderline to PowerOfficeGov1 Orderline
---------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Orderline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Orderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Orderline Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorderline to PowerOfficeGov1 Quoteline
---------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Quoteline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Quoteline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Quoteline Property
     - PowerOfficeGov1 Data Type


Powerofficego Salesorderline to PowerOfficeGov1 Salesorderline
--------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type


Powerofficego Supplier to PowerOfficeGov1 Supplier
--------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Supplier.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type


Powerofficego Supplier to PowerOfficeGov1 Vendor
------------------------------------------------
Every Powerofficego Supplier will be synchronized with a PowerOfficeGov1 Vendor.

Once a link between a Powerofficego Supplier and a PowerOfficeGov1 Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGov1 Vendor:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGov1 Vendor Property
     - PowerOfficeGov1 Data Type


Powerofficego Vatcode to PowerOfficeGov1 Vatcode
------------------------------------------------
Every Powerofficego Vatcode will be synchronized with a PowerOfficeGov1 Vatcode.

If a matching PowerOfficeGov1 Vatcode already exists, the Powerofficego Vatcode will be merged with the existing one.
If no matching PowerOfficeGov1 Vatcode is found, a new PowerOfficeGov1 Vatcode will be created.

A Powerofficego Vatcode will merge with a PowerOfficeGov1 Vatcode if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
   * - id
     - id

Once a link between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcode and a PowerOfficeGov1 Vatcode:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGov1 Vatcode Property
     - PowerOfficeGov1 Data Type

