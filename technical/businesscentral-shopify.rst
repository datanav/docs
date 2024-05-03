============================
Businesscentral to  Dataflow
============================

Generated: 2024-05-03 12:26:05

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Inventoryitem
---------------------------------------
Every Businesscentral Items will be synchronized with a  Inventoryitem.

Once a link between a Businesscentral Items and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Inventoryitem Property
     -  Data Type
   * - unitCost
     - cost
     - "string"


Businesscentral Customers person to  Customer
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customer.

Once a link between a Businesscentral Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customer Property
     -  Data Type
   * - addressLine1
     - addresses.address1
     - "string"
   * - addressLine2
     - addresses.address2
     - "string"
   * - city
     - addresses.city
     - "string"
   * - country
     - addresses.country
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - addresses.zip
     - "string"


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type


Businesscentral Salesorders to  Order
-------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Order.

Once a link between a Businesscentral Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Order Property
     -  Data Type
   * - billToAddressLine1
     - shipping_address.address1
     - "string"
   * - billToAddressLine2
     - shipping_address.address2
     - "string"
   * - billToCity
     - shipping_address.city
     - "string"
   * - billToCountry
     - shipping_address.country
     - "string"
   * - billToCountry
     - shipping_address.country_code
     - "string"
   * - billToPostCode
     - shipping_address.zip
     - "string"
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer.id
     - "string"
   * - shipToAddressLine1
     - shipping_address.address1
     - "string"
   * - shipToAddressLine2
     - shipping_address.address2
     - "string"
   * - shipToCity
     - shipping_address.city
     - "string"
   * - shipToCountry
     - shipping_address.country
     - "string"
   * - shipToCountry
     - shipping_address.country_code
     - "string"
   * - shipToPostCode
     - shipping_address.zip
     - "string"
   * - totalAmountExcludingTax
     - current_total_price
     - "string"
   * - totalAmountExcludingTax
     - total_price
     - "string"

