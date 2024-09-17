==================================
PowerOffice GO to Shopify Dataflow
==================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Shopify Customer
------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Shopify Customer must be established.

A new Shopify Customer will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorders, or Powerofficego-salesorderlines that is synchronized into Shopify.

Once a link between a PowerOffice GO Contactperson and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Shopify Customer Property
     - Shopify Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - phoneNumber
     - default_address.phone
     - "string"
   * - phoneNumber
     - phone
     - "string"


PowerOffice GO Customers to Shopify Customer
--------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Shopify Customer must be established.

A new Shopify Customer will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-salesorders, or Powerofficego-salesorderlines that is synchronized into Shopify.

Once a link between a PowerOffice GO Customers and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Shopify Customer Property
     - Shopify Data Type


PowerOffice GO Product to Shopify Product
-----------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Product and a Shopify Product must be established.

A new Shopify Product will be created from a PowerOffice GO Product if it is connected to a PowerOffice GO Powerofficego-salesorders, or Powerofficego-salesorderlines that is synchronized into Shopify.

Once a link between a PowerOffice GO Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Shopify Product Property
     - Shopify Data Type


PowerOffice GO Salesorders to Shopify Order
-------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Salesorders and a Shopify Order must be established.

A new Shopify Order will be created from a PowerOffice GO Salesorders if it is connected to a PowerOffice GO Powerofficego-salesorders, or Powerofficego-salesorderlines that is synchronized into Shopify.

Once a link between a PowerOffice GO Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Shopify Order Property
     - Shopify Data Type


PowerOffice GO Customers person to Shopify Customer
---------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Shopify Customer.

Once a link between a PowerOffice GO Customers person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Shopify Customer Property
     - Shopify Data Type


PowerOffice GO Customers to Shopify Customer
--------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Shopify Customer.

Once a link between a PowerOffice GO Customers and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Shopify Customer Property
     - Shopify Data Type


PowerOffice GO Product to Shopify Sesamproduct
----------------------------------------------
Every PowerOffice GO Product will be synchronized with a Shopify Sesamproduct.

Once a link between a PowerOffice GO Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type


PowerOffice GO Salesorders to Shopify Order
-------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Shopify Order.

Once a link between a PowerOffice GO Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Shopify Order Property
     - Shopify Data Type

