============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-03 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contact person to  Contact
------------------------------------------
Every Businesscentral Contact person will be synchronized with a  Contact.

Once a link between a Businesscentral Contact person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact person Property
     -  Contact Property
     -  Data Type
   * - email
     - email
     - "string"
   * - mobilePhoneNumber
     - phoneNumberMobile
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phoneNumber
     - phoneNumberWork
     - "string"


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

If a matching  Product already exists, the Businesscentral Items will be merged with the existing one.
If no matching  Product is found, a new  Product will be created.

A Businesscentral Items will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
   * - gtin
     - ean

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - gtin
     - ean
     - "string"
   * - inventory
     - stockOfGoods
     - "integer"
   * - taxGroupCode
     - vatType.id
     - "integer"
   * - unitCost
     - costExcludingVatCurrency
     - "float"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Businesscentral Salesorderlines to  Orderline
---------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Orderline.

Once a link between a Businesscentral Salesorderlines and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Orderline Property
     -  Data Type
   * - amountExcludingTax
     - unitPriceExcludingVatCurrency
     - "float"
   * - description
     - description
     - "string"
   * - discountPercent
     - discount
     - "float"
   * - invoiceQuantity
     - count
     - "float"
   * - itemId
     - product.id
     - "integer"
   * - quantity
     - count
     - "float"
   * - taxPercent
     - vatType.id
     - "integer"
   * - unitPrice
     - unitPriceExcludingVatCurrency
     - "float"


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
   * - currencyId
     - currency.id
     - "integer"
   * - customerId
     - contact.id
     - "integer"
   * - customerId
     - customer.id
     - "integer"
   * - orderDate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]
   * - requestedDeliveryDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - salesperson
     - ourContactEmployee.id
     - "integer"

