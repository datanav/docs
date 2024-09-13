=========================
Tripletex to Wix Dataflow
=========================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to Wix Contacts
-----------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Wix Contacts must be established.

A Tripletex Customer person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Tripletex Customer person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - primaryInfo.email
     - "string"
   * - phoneNumber
     - primaryInfo.phone
     - "string"


Tripletex Employee to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Wix Contacts must be established.

A Tripletex Employee will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Tripletex Employee and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wix Contacts Property
     - Wix Data Type
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
   * - firstName
     - info.name.last
     - "string"
   * - id
     - id
     - "string"
   * - lastName
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
   * - phoneNumberWork
     - primaryInfo.phone
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
   * - phoneNumberWork
     - primaryInfo.phone
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
     - costAndProfitData.itemCost
     - N/A
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
     - N/A

