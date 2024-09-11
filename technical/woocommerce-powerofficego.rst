======================================
WooCommerce to PowerOffice GO Dataflow
======================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to PowerOffice Customers person
----------------------------------------------------
Every WooCommerce Customer will be synchronized with a PowerOffice Customers person.

Once a link between a WooCommerce Customer and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - email
     - EmailAddress
     - "string"
   * - last_name
     - LastName
     - "string"


WooCommerce Order to PowerOffice Salesorderlines
------------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOffice Salesorderlines.

Once a link between a WooCommerce Order and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
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


WooCommerce Order to PowerOffice Salesorders
--------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOffice Salesorders.

Once a link between a WooCommerce Order and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"


WooCommerce Product to PowerOffice Product
------------------------------------------
Every WooCommerce Product will be synchronized with a PowerOffice Product.

Once a link between a WooCommerce Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - name
     - name
     - "string"
   * - price
     - costPrice
     - N/A
   * - sale_price
     - salesPrice
     - N/A

