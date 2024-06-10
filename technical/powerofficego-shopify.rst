=================================
Powerofficego to Shopify Dataflow
=================================

Generated: 2024-06-10 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to Shopify Inventoryitem
----------------------------------------------
Every Powerofficego Product will be synchronized with a Shopify Inventoryitem.

Once a link between a Powerofficego Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - costPrice
     - cost
     - "string"


Powerofficego Customers person to Shopify Customer
--------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Shopify Customer.

Once a link between a Powerofficego Customers person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - EmailAddress
     - email
     - "string"
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - addresses.address1
     - "string"
   * - MailAddress.AddressLine2
     - addresses.address2
     - "string"
   * - MailAddress.City
     - addresses.city
     - "string"
   * - MailAddress.CountryCode
     - addresses.country
     - "string"
   * - MailAddress.ZipCode
     - addresses.zip
     - "string"
   * - PhoneNumber
     - phone
     - "string"


Powerofficego Product to Shopify Product
----------------------------------------
Every Powerofficego Product will be synchronized with a Shopify Product.

Once a link between a Powerofficego Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - name
     - variants.title
     - "string"
   * - salesPrice
     - variants.price
     - "string"


Powerofficego Salesorders to Shopify Order
------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Shopify Order.

Once a link between a Powerofficego Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
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

