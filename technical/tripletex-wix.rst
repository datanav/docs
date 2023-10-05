=========================
Tripletex to Wix Dataflow
=========================

Generated: 2023-10-05 08:40:19

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Wix Members
--------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Wix Members must be established.

A Tripletex Contact will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Contact and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Tripletex Employee to Wix Contacts
----------------------------------
Every Tripletex Employee will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Tripletex Employee will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Tripletex Employee will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
   * - email
     - info.emails
   * - email
     - primaryInfo.email

Once a link between a Tripletex Employee and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - phoneNumberMobile
     - info.phones
     - "string"
   * - phoneNumberMobile
     - primaryInfo.phone
     - "string"


Tripletex Employee to Wix Members
---------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Wix Members must be established.

A Tripletex Employee will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Employee and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Tripletex Customer to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wix Contacts must be established.

A new Wix Contacts will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Orderline that is synchronized into Wix.

Once a link between a Tripletex Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wix Contacts Property
     - Wix Data Type


Tripletex Customer to Wix Members
---------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wix Members must be established.

A new Wix Members will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Orderline that is synchronized into Wix.

Once a link between a Tripletex Customer and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wix Members Property
     - Wix Data Type


Tripletex Productgrouprelation to Wix Inventory
-----------------------------------------------
Every Tripletex Productgrouprelation will be synchronized with a Wix Inventory.

Once a link between a Tripletex Productgrouprelation and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgrouprelation and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgrouprelation Property
     - Wix Inventory Property
     - Wix Data Type


Tripletex Contact to Wix Contacts
---------------------------------
Every Tripletex Contact will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Tripletex Contact will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Tripletex Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Contacts Property
   * - email
     - info.emails
   * - email
     - primaryInfo.email

Once a link between a Tripletex Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - phoneNumberMobile
     - info.phones
     - "string"
   * - phoneNumberMobile
     - primaryInfo.phone
     - "string"


Tripletex Order to Wix Orders
-----------------------------
Every Tripletex Order will be synchronized with a Wix Orders.

Once a link between a Tripletex Order and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Wix Orders Property
     - Wix Data Type
   * - contact.id
     - buyerInfo.id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - buyerInfo.contactId
     - "string"
   * - customer.id
     - buyerInfo.id
     - "string"


Tripletex Orderline to Wix Orders
---------------------------------
Every Tripletex Orderline will be synchronized with a Wix Orders.

Once a link between a Tripletex Orderline and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Wix Orders Property
     - Wix Data Type
   * - count
     - lineItems.quantity
     - "string"
   * - count
     - lineItems.quantity.quantity
     - "string"
   * - currency.id
     - currency
     - "string"
   * - description
     - lineItems.name
     - "string"
   * - description
     - lineItems.name.name
     - "string"
   * - product.id
     - lineItems.productId
     - "string"
   * - product.id
     - lineItems.productId.productId
     - "string"
   * - unitPriceExcludingVatCurrency
     - lineItems.price
     - "string"
   * - unitPriceExcludingVatCurrency
     - lineItems.price.price
     - "string"


Tripletex Product to Wix Inventory
----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Wix Inventory.

Once a link between a Tripletex Product and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Wix Inventory Property
     - Wix Data Type
   * - stockOfGoods
     - lastUpdated
     - "string"
   * - stockOfGoods
     - variants.quantity
     - "string"


Tripletex Product to Wix Products
---------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Wix Products.

Once a link between a Tripletex Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Wix Products Property
     - Wix Data Type
   * - costExcludingVatCurrency
     - costRange.maxValue
     - "string"
   * - currency.id
     - price.currency
     - "string"
   * - currency.id
     - priceData.currency
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - price.price
     - "string"
   * - priceExcludingVatCurrency
     - priceData.price
     - "decimal"

