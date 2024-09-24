====================
Wave to Wix Dataflow
====================

Generated: 2024-09-24 13:16:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Wix Contacts
-----------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wix Contacts must be established.

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
   * - email
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - phone
     - primaryInfo.phone
     - "string"
   * - shippingDetails.phone
     - primaryInfo.phone
     - "string"


Wave Customer to Wix Contacts
-----------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wix Contacts must be established.

A new Wix Contacts will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Wix.

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


Wave Vendor to Wix Contacts
---------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wix Contacts must be established.

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


Wave Customer to Wix Contacts
-----------------------------
Every Wave Customer will be synchronized with a Wix Contacts.

Once a link between a Wave Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
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
   * - name
     - name
     - "string"
   * - unitPrice
     - priceData.price
     - N/A


Wave Vendor to Wix Contacts
---------------------------
Every Wave Vendor will be synchronized with a Wix Contacts.

Once a link between a Wave Vendor and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - phone
     - primaryInfo.phone
     - "string"

