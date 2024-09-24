==================================
Shopify to PowerOffice GO Dataflow
==================================

Generated: 2024-09-24 13:16:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to PowerOffice GO Customers
--------------------------------------------
Every Shopify Customer will be synchronized with a PowerOffice GO Customers.

Once a link between a Shopify Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Shopify Customer to PowerOffice GO Customers (human data)
---------------------------------------------------------
Every Shopify Customer will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Shopify Customer and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type
   * - default_address.phone
     - PhoneNumber
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"


Shopify Order to PowerOffice GO Salesorderlines
-----------------------------------------------
Every Shopify Order will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Shopify Order and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - id
     - sesam_SalesOrderId
     - "string"
   * - line_items.price
     - ProductUnitPrice
     - N/A
   * - line_items.quantity
     - Quantity
     - N/A
   * - line_items.title
     - Description
     - "string"
   * - line_items.total_discount
     - Allowance
     - "float"


Shopify Order to PowerOffice GO Salesorders
-------------------------------------------
Every Shopify Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Shopify Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - created_at
     - SalesOrderDate
     - "string"
   * - currency
     - CurrencyCode
     - "string"
   * - customer.id
     - CustomerId
     - "integer"
   * - customer.id
     - CustomerReferenceContactPersonId
     - "integer"
   * - po_number
     - PurchaseOrderReference
     - "string"


Shopify Sesamproduct to PowerOffice GO Product
----------------------------------------------
Every Shopify Sesamproduct will be synchronized with a PowerOffice GO Product.

Once a link between a Shopify Sesamproduct and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - sesam_priceExclVAT
     - salesPrice
     - N/A
   * - title
     - name
     - "string"
   * - variants.inventory_quantity
     - availableStock
     - "integer"
   * - variants.title
     - description
     - "string"

