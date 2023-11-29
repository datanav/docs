=============================
Wix.com to Tripletex Dataflow
=============================

Generated: 2023-11-29 14:35:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Tripletex Employee
--------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Tripletex Employee must be established.

A Wix.com Contacts will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Employee Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Employee Property
     - Tripletex Data Type
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


Wix.com Members to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tripletex Contact must be established.

A Wix.com Members will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Contact Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Members to Tripletex Employee
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tripletex Employee must be established.

A Wix.com Members will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Employee Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Contacts to Tripletex Customer
--------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Tripletex.

Once a link between a Wix.com Contacts and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Customer Property
     - Tripletex Data Type


Wix.com Members to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Wix.com Members if it is connected to a Wix.com Wix-orders that is synchronized into Tripletex.

Once a link between a Wix.com Members and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tripletex Customer Property
     - Tripletex Data Type


Wix.com Contacts to Tripletex Contact
-------------------------------------
Every Wix.com Contacts will be synchronized with a Tripletex Contact.

If a matching Tripletex Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching Tripletex Contact is found, a new Tripletex Contact will be created.

A Wix.com Contacts will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Contact Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type
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


Wix.com Inventory to Tripletex Product
--------------------------------------
Every Wix.com Inventory will be synchronized with a Tripletex Product.

Once a link between a Wix.com Inventory and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - lastUpdated
     - stockOfGoods
     - "integer"
   * - variants.quantity
     - stockOfGoods
     - "integer"


Wix.com Orders to Tripletex Order
---------------------------------
Every Wix.com Orders will be synchronized with a Tripletex Order.

Once a link between a Wix.com Orders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Tripletex Order Property
     - Tripletex Data Type
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


Wix.com Orders to Tripletex Orderline
-------------------------------------
Every Wix.com Orders will be synchronized with a Tripletex Orderline.

Once a link between a Wix.com Orders and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Tripletex Orderline Property
     - Tripletex Data Type
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


Wix.com Products to Tripletex Product
-------------------------------------
Every Wix.com Products will be synchronized with a Tripletex Product.

Once a link between a Wix.com Products and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Tripletex Product Property
     - Tripletex Data Type
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

