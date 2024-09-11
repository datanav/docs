=====================================
WooCommerce to PowerOfficeGO Dataflow
=====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to PowerOfficeGO Customers person
------------------------------------------------------
Every WooCommerce Customer will be synchronized with a PowerOfficeGO Customers person.

Once a link between a WooCommerce Customer and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
   * - email
     - EmailAddress
     - "string"
   * - last_name
     - LastName
     - "string"


WooCommerce Order to PowerOfficeGO Salesorderlines
--------------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a WooCommerce Order and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
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


WooCommerce Order to PowerOfficeGO Salesorders
----------------------------------------------
Every WooCommerce Order will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a WooCommerce Order and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"


WooCommerce Product to PowerOfficeGO Product
--------------------------------------------
Every WooCommerce Product will be synchronized with a PowerOfficeGO Product.

Once a link between a WooCommerce Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - name
     - name
     - "string"
   * - price
     - costPrice
     - N/A
   * - sale_price
     - salesPrice
     - N/A

