==================================
PowerOffice GO to Shopify Dataflow
==================================

Generated: 2024-10-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers (human data) to Shopify Customer
---------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a Shopify Customer.

Once a link between a PowerOffice GO Customers (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - Shopify Customer Property
     - Shopify Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"
   * - PhoneNumber
     - default_address.phone
     - "string"


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
   * - availableStock
     - variants.inventory_quantity
     - "integer"
   * - description
     - variants.title
     - "string"
   * - name
     - title
     - "string"
   * - salesPrice
     - sesam_priceExclVAT
     - "string"


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
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer.id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer.id
     - "string"
   * - NetAmount
     - current_total_price
     - "string"
   * - NetAmount
     - total_price
     - "string"
   * - PurchaseOrderReference
     - po_number
     - "string"

