==============================
Wave Financial to Wix Dataflow
==============================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Wix Contacts
------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Wix Contacts must be established.

A Wave Customer person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Wave Customer person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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
   * - phone
     - primaryInfo.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - shippingDetails.address.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - info.addresses.items.address.city
     - "string"
   * - shippingDetails.address.postalCode
     - info.addresses.items.address.postalCode
     - "string"
   * - shippingDetails.phone
     - primaryInfo.phone
     - "string"


Wave Customer to Wix Contacts
-----------------------------
Every Wave Customer will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Wave Customer will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Wave Customer will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Wave Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
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
   * - mobile
     - info.phones
     - "string"
   * - mobile
     - primaryInfo.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - shippingDetails.address.addressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - info.addresses.items.address.city
     - "string"
   * - shippingDetails.address.postalCode
     - info.addresses.items.address.postalCode
     - "string"


Wave Product to Wix Products
----------------------------
Every Wave Product will be synchronized with a Wix Products.

Once a link between a Wave Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Wix Products Property
     - Wix Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - price.price
     - "string"
   * - unitPrice
     - priceData.price
     - N/A


Wave Vendor to Wix Contacts
---------------------------
Every Wave Vendor will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Wave Vendor will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Wave Vendor will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Wave Vendor and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - mobile
     - info.phones
     - "string"
   * - mobile
     - primaryInfo.phone
     - "string"
   * - phone
     - primaryInfo.phone
     - "string"

