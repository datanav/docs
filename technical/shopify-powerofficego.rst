=================================
Shopify to Powerofficego Dataflow
=================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Powerofficego Customers person
--------------------------------------------------
Every Shopify Customer will be synchronized with a Powerofficego Customers person.

Once a link between a Shopify Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - addresses.address1
     - MailAddress.AddressLine1
     - "string"
   * - addresses.address2
     - MailAddress.AddressLine2
     - "string"
   * - addresses.city
     - MailAddress.City
     - "string"
   * - addresses.country
     - MailAddress.CountryCode
     - "string"
   * - addresses.zip
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "integer"
   * - phone
     - PhoneNumber
     - "string"


Shopify Order to Powerofficego Salesorders
------------------------------------------
Every Shopify Order will be synchronized with a Powerofficego Salesorders.

Once a link between a Shopify Order and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
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


Shopify Product to Powerofficego Product
----------------------------------------
Every Shopify Product will be synchronized with a Powerofficego Product.

Once a link between a Shopify Product and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Powerofficego Product Property
     - Powerofficego Data Type
   * - variants.price
     - salesPrice
     - N/A
   * - variants.title
     - name
     - "string"

