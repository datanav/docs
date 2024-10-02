=========================
Tripletex to Wix Dataflow
=========================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Wix Contacts
---------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Wix Contacts must be established.

A new Wix Contacts will be created from a Tripletex Contact if it is connected to a Tripletex Order, or Orderline that is synchronized into Wix.

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
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - phoneNumberWork
     - primaryInfo.phone
     - "string"


Tripletex Customer to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wix Contacts must be established.

A Tripletex Customer will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Tripletex Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
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
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - phoneNumberWork
     - primaryInfo.phone
     - "string"


Tripletex Contact to Wix Contacts
---------------------------------
Every Tripletex Contact will be synchronized with a Wix Contacts.

Once a link between a Tripletex Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wix Contacts Property
     - Wix Data Type


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
   * - currency.id
     - priceData.currency
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - priceData.price
     - N/A

