=====================================
Woocommerce to Powerofficego Dataflow
=====================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to Powerofficego Customers person
------------------------------------------------------
Every Woocommerce Customer will be synchronized with a Powerofficego Customers person.

Once a link between a Woocommerce Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - email
     - EmailAddress
     - "string"
   * - last_name
     - LastName
     - "string"


Woocommerce Order to Powerofficego Salesorderlines
--------------------------------------------------
Every Woocommerce Order will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Woocommerce Order and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
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


Woocommerce Order to Powerofficego Salesorders
----------------------------------------------
Every Woocommerce Order will be synchronized with a Powerofficego Salesorders.

Once a link between a Woocommerce Order and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"


Woocommerce Product to Powerofficego Product
--------------------------------------------
Every Woocommerce Product will be synchronized with a Powerofficego Product.

Once a link between a Woocommerce Product and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Powerofficego Product Property
     - Powerofficego Data Type
   * - name
     - name
     - "string"
   * - price
     - costPrice
     - N/A
   * - sale_price
     - salesPrice
     - N/A

