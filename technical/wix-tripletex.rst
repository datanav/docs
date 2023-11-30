====================
Wix.com to  Dataflow
====================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Employee
-----------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Employee must be established.

A Wix.com Contacts will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Employee Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Employee Property
     -  Data Type
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - info.phones
     - phoneNumberMobile
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - phoneNumberMobile
     - "string"


Wix.com Members to  Contact
---------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Contact must be established.

A Wix.com Members will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contact Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contact Property
     -  Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Members to  Employee
----------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Employee must be established.

A Wix.com Members will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Employee Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Employee Property
     -  Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Contacts to  Customer
-----------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Customer must be established.

A new  Customer will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Contacts and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customer Property
     -  Data Type


Wix.com Contacts to  Contact
----------------------------
Every Wix.com Contacts will be synchronized with a  Contact.

If a matching  Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Wix.com Contacts will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contact Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contact Property
     -  Data Type
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - info.phones
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - phoneNumberMobile
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]


Wix.com Inventory to  Product
-----------------------------
Every Wix.com Inventory will be synchronized with a  Product.

Once a link between a Wix.com Inventory and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     -  Product Property
     -  Data Type
   * - lastUpdated
     - stockOfGoods
     - "integer"
   * - variants.quantity
     - stockOfGoods
     - "integer"


Wix.com Orders to  Order
------------------------
Every Wix.com Orders will be synchronized with a  Order.

Once a link between a Wix.com Orders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Order Property
     -  Data Type
   * - buyerInfo.contactId
     - customer.id
     - "integer"
   * - buyerInfo.id
     - contact.id
     - "integer"
   * - buyerInfo.id
     - customer.id
     - "integer"
   * - currency
     - currency.id
     - "integer"


Wix.com Orders to  Orderline
----------------------------
Every Wix.com Orders will be synchronized with a  Orderline.

Once a link between a Wix.com Orders and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Orderline Property
     -  Data Type
   * - id
     - order.id
     - "integer"
   * - lineItems.name
     - description
     - "string"
   * - lineItems.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - lineItems.productId
     - product.id
     - "integer"
   * - lineItems.quantity
     - count
     - "float"


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
   * - costRange.maxValue
     - costExcludingVatCurrency
     - "integer"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - price.currency
     - currency.id
     - "integer"
   * - price.price
     - priceExcludingVatCurrency
     - "float"
   * - priceData.currency
     - currency.id
     - "integer"
   * - priceData.price
     - priceExcludingVatCurrency
     - "float"

