==================================
PowerOffice GO to Shopify Dataflow
==================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to Shopify Customer
-----------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a Shopify Customer must be established.

A new Shopify Customer will be created from a PowerOfficeGO Contactperson if it is connected to a PowerOfficeGO Salesorders, or Salesorderlines that is synchronized into Shopify.

Once a link between a PowerOfficeGO Contactperson and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - Shopify Customer Property
     - Shopify Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - phoneNumber
     - default_address.phone
     - "string"
   * - phoneNumber
     - phone
     - "string"


PowerOfficeGO Customers to Shopify Customer
-------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers and a Shopify Customer must be established.

A new Shopify Customer will be created from a PowerOfficeGO Customers if it is connected to a PowerOfficeGO Salesorders, or Salesorderlines that is synchronized into Shopify.

Once a link between a PowerOfficeGO Customers and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - Shopify Customer Property
     - Shopify Data Type


PowerOfficeGO Product to Shopify Product
----------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Product and a Shopify Product must be established.

A new Shopify Product will be created from a PowerOfficeGO Product if it is connected to a PowerOfficeGO Salesorders, or Salesorderlines that is synchronized into Shopify.

Once a link between a PowerOfficeGO Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - Shopify Product Property
     - Shopify Data Type


PowerOfficeGO Customers person to Shopify Customer
--------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a Shopify Customer.

Once a link between a PowerOfficeGO Customers person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MailAddress.AddressLine1
     - addresses.address1
     - "string"
   * - MailAddress.AddressLine1
     - default_address.address1
     - "string"
   * - MailAddress.AddressLine2
     - addresses.address2
     - "string"
   * - MailAddress.AddressLine2
     - default_address.address2
     - "string"
   * - MailAddress.City
     - addresses.city
     - "string"
   * - MailAddress.City
     - default_address.city
     - "string"
   * - MailAddress.CountryCode
     - addresses.country
     - "string"
   * - MailAddress.CountryCode
     - default_address.country
     - "string"
   * - MailAddress.ZipCode
     - addresses.zip
     - "string"
   * - MailAddress.ZipCode
     - default_address.zip
     - "string"
   * - PhoneNumber
     - default_address.phone
     - "string"
   * - PhoneNumber
     - phone
     - "string"


PowerOfficeGO Product to Shopify Sesamproduct
---------------------------------------------
Every PowerOfficeGO Product will be synchronized with a Shopify Sesamproduct.

Once a link between a PowerOfficeGO Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - availableStock
     - variants.inventory_quantity
     - "integer"
   * - availableStock
     - variants.inventory_quantity.inventory_quantity
     - "string"
   * - description
     - variants.title
     - "string"
   * - name
     - title
     - "string"
   * - salesPrice
     - sesam_priceExclVAT
     - "string"
   * - salesPrice
     - variants.price
     - "string"


PowerOfficeGO Salesorders to Shopify Order
------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a Shopify Order.

Once a link between a PowerOfficeGO Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
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

