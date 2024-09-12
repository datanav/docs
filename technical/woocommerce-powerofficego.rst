======================================
WooCommerce to PowerOffice GO Dataflow
======================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to PowerOffice GO Customers person
-------------------------------------------------------
Every WooCommerce Customer will be synchronized with a PowerOffice GO Customers person.

Once a link between a WooCommerce Customer and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
   * - email
     - EmailAddress
     - "string"
   * - last_name
     - LastName
     - "string"


WooCommerce Order to PowerOffice GO Currency
--------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOffice GO Currency.

If a matching PowerOffice GO Currency already exists, the WooCommerce Order will be merged with the existing one.
If no matching PowerOffice GO Currency is found, a new PowerOffice GO Currency will be created.

A WooCommerce Order will merge with a PowerOffice GO Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice GO Currency Property
   * - currency
     - code

Once a link between a WooCommerce Order and a PowerOffice GO Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOffice GO Currency:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice GO Currency Property
     - PowerOffice GO Data Type


WooCommerce Order to PowerOffice GO Salesorderlines
---------------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a WooCommerce Order and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - id
     - sesam_SalesOrderId
     - "string"
   * - line_items.name
     - Description
     - "string"
   * - line_items.price
     - ProductUnitPrice
     - N/A
   * - line_items.quantity
     - Quantity
     - N/A


WooCommerce Order to PowerOffice GO Salesorders
-----------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a WooCommerce Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"


WooCommerce Product to PowerOffice GO Product
---------------------------------------------
Every WooCommerce Product will be synchronized with a PowerOffice GO Product.

Once a link between a WooCommerce Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - name
     - name
     - "string"
   * - price
     - costPrice
     - N/A
   * - sale_price
     - salesPrice
     - N/A

