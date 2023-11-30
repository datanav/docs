======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Members
-----------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Members must be established.

A Tripletex Contact will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Contact and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Members Property
     -  Data Type
   * - email
     - loginEmail
     - "string"


Tripletex Employee to  Contacts
-------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Contacts must be established.

A Tripletex Employee will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Tripletex Employee and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contacts Property
     -  Data Type
   * - address.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - address.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - address.city
     - info.addresses.items.address.city
     - "string"
   * - address.postalCode
     - info.addresses.items.address.postalCode
     - "string"
   * - email
     - info.emails
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - id
     - id
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


Tripletex Employee to  Members
------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Members must be established.

A Tripletex Employee will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Members Property
   * - email
     - loginEmail

Once a link between a Tripletex Employee and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Members:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Members Property
     -  Data Type
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
   * - deliveryAddress.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - deliveryAddress.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - deliveryAddress.city
     - info.addresses.items.address.city
     - "string"
   * - deliveryAddress.postalCode
     - info.addresses.items.address.postalCode
     - "string"
   * - id
     - id
     - "string"
   * - physicalAddress.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - physicalAddress.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - physicalAddress.city
     - info.addresses.items.address.city
     - "string"
   * - physicalAddress.postalCode
     - info.addresses.items.address.postalCode
     - "string"
   * - postalAddress.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - postalAddress.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - postalAddress.city
     - info.addresses.items.address.city
     - "string"
   * - postalAddress.postalCode
     - info.addresses.items.address.postalCode
     - "string"


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


Tripletex Product to  Inventory
-------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Inventory.

Once a link between a Tripletex Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Inventory Property
     -  Data Type
   * - stockOfGoods
     - lastUpdated
     - "string"
   * - stockOfGoods
     - variants.quantity
     - "integer"


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

