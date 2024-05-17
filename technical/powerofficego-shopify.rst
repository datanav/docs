==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-05-17 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to  Inventoryitem
---------------------------------------
Every Powerofficego Product will be synchronized with a  Inventoryitem.

Once a link between a Powerofficego Product and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Inventoryitem Property
     -  Data Type
   * - costPrice
     - cost
     - "string"


Powerofficego Customers person to  Customer
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customer.

Once a link between a Powerofficego Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customer Property
     -  Data Type
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


Powerofficego Product to  Product
---------------------------------
Every Powerofficego Product will be synchronized with a  Product.

Once a link between a Powerofficego Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Product Property
     -  Data Type
   * - name
     - variants.title
     - "string"
   * - salesPrice
     - variants.price
     - "string"


Powerofficego Salesorders to  Order
-----------------------------------
Every Powerofficego Salesorders will be synchronized with a  Order.

Once a link between a Powerofficego Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Order Property
     -  Data Type
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

