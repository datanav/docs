=================================
Shopify to Powerofficego Dataflow
=================================

Generated: 2024-07-06 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Powerofficego Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Powerofficego.

Once a link between a Shopify Customer and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - email
     - emailAddress
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone
     - phoneNumber
     - "string"


Shopify Customer to Powerofficego Customers
-------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Powerofficego.

Once a link between a Shopify Customer and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


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
   * - default_address.address1
     - MailAddress.AddressLine1
     - "string"
   * - default_address.address2
     - MailAddress.AddressLine2
     - "string"
   * - default_address.city
     - MailAddress.City
     - "string"
   * - default_address.country
     - MailAddress.CountryCode
     - "string"
   * - default_address.zip
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - last_name
     - LastName
     - "string"
   * - phone
     - PhoneNumber
     - "string"


Shopify Order to Powerofficego Salesorderlines
----------------------------------------------
Every Shopify Order will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Shopify Order and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
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
   * - title
     - name
     - "string"
   * - variants.price
     - salesPrice
     - N/A
   * - variants.title
     - name
     - "string"

