====================
Wave to Wix Dataflow
====================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Wave Customer person to Wix Members
-----------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Wix Members must be established.

A Wave Customer person will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Wave Customer person and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Wix Members Property
     - Wix Data Type


Wave Customer to Wix Members
----------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wix Members must be established.

A Wave Customer will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Wave Customer and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Wave Vendor to Wix Members
--------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wix Members must be established.

A Wave Vendor will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Wave Vendor and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Wave Currency to Wix Currencies
-------------------------------
Every Wave Currency will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the Wave Currency will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A Wave Currency will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Wix Currencies Property
   * - code
     - code

Once a link between a Wave Currency and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Wix Currencies Property
     - Wix Data Type


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


Wave Invoice to Wix Orders
--------------------------
Every Wave Invoice will be synchronized with a Wix Orders.

Once a link between a Wave Invoice and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Wix Orders Property
     - Wix Data Type
   * - business.id
     - buyerInfo.contactId
     - "string"
   * - business.id
     - buyerInfo.id
     - "string"
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - buyerInfo.contactId
     - "string"
   * - customer.id
     - buyerInfo.id
     - "string"
   * - invoiceDate
     - dateCreated
     - "string"
   * - items.description
     - lineItems.name
     - "string"
   * - items.description
     - lineItems.name.name
     - "string"
   * - items.price
     - lineItems.price
     - "string"
   * - items.price
     - lineItems.price.price
     - "string"
   * - items.product.id
     - lineItems.productId
     - "string"
   * - items.product.id
     - lineItems.productId.productId
     - "string"
   * - items.quantity
     - lineItems.quantity
     - "integer"
   * - items.quantity
     - lineItems.quantity.quantity
     - "string"
   * - items.unitPrice
     - lineItems.price
     - "string"
   * - total.value
     - totals.total
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

