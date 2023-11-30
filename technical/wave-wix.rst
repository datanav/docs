===========================
Wave Financial to  Dataflow
===========================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Contacts
---------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Contacts must be established.

A Wave Customer person will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Wave Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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
   * - id
     - id
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


Wave Customer person to  Members
--------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Members must be established.

A Wave Customer person will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Members Property
   * - email
     - loginEmail

Once a link between a Wave Customer person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Members Property
     -  Data Type


Wave Customer to  Members
-------------------------
Before any synchronization can take place, a link between a Wave Customer and a  Members must be established.

A Wave Customer will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Members Property
   * - email
     - loginEmail

Once a link between a Wave Customer and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Members Property
     -  Data Type
   * - email
     - loginEmail
     - "string"


Wave Vendor to  Contacts
------------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Contacts must be established.

A Wave Vendor will merge with a  Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contacts Property
   * - email
     - primaryInfo.email

Once a link between a Wave Vendor and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - mobile
     - info.phones
     - "string"
   * - mobile
     - primaryInfo.phone
     - "string"


Wave Vendor to  Members
-----------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Members must be established.

A Wave Vendor will merge with a  Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Members Property
   * - email
     - loginEmail

Once a link between a Wave Vendor and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Members:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Members Property
     -  Data Type
   * - email
     - loginEmail
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
   * - id
     - id
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


Wave Product to  Inventory
--------------------------
Every Wave Product will be synchronized with a  Inventory.

Once a link between a Wave Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Inventory Property
     -  Data Type


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
     - "decimal"

