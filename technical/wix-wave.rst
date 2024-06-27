========================
Wix.com to Wave Dataflow
========================

Generated: 2024-06-27 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wave Customer person
----------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wave Customer person must be established.

A new Wave Customer person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

A Wix.com Contacts will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wave Customer person Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wave Customer person Property
     - Wave Data Type
   * - info.name.first
     - firstName
     - "string"
   * - info.name.first
     - lastName
     - N/A
   * - info.name.first
     - name
     - N/A
   * - info.name.last
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - N/A
   * - info.name.last
     - name
     - N/A
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - mobile
     - "string"
   * - primaryInfo.phone
     - phone
     - "string"


Wix.com Members to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wave Customer person must be established.

A Wix.com Members will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wave Customer person Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wave Customer person Property
     - Wave Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Contacts to Wave Customer
---------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wave Customer must be established.

A new Wave Customer will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

Once a link between a Wix.com Contacts and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wave Customer Property
     - Wave Data Type
   * - info.name.first
     - firstName
     - "string"
   * - info.name.first
     - lastName
     - "string"
   * - info.name.last
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - mobile
     - "string"


Wix.com Orders to Wave Invoice
------------------------------
Every Wix.com Orders will be synchronized with a Wave Invoice.

Once a link between a Wix.com Orders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Wave Invoice Property
     - Wave Data Type
   * - buyerInfo.contactId
     - customer.id
     - "string"
   * - buyerInfo.id
     - customer.id
     - "string"
   * - currency
     - currency.code
     - "string"
   * - dateCreated
     - invoiceDate
     - N/A
   * - lineItems.name
     - items.description
     - "string"
   * - lineItems.name
     - items.price
     - "string"
   * - lineItems.name
     - items.quantity
     - N/A
   * - lineItems.name.name
     - items.description
     - "string"
   * - lineItems.price
     - items.description
     - "string"
   * - lineItems.price
     - items.price
     - "string"
   * - lineItems.price
     - items.quantity
     - N/A
   * - lineItems.price
     - items.unitPrice
     - "float"
   * - lineItems.price.price
     - items.price
     - "float"
   * - lineItems.productId
     - items.product.id
     - "string"
   * - lineItems.productId.productId
     - items.product.id
     - "string"
   * - lineItems.quantity
     - items.description
     - "string"
   * - lineItems.quantity
     - items.price
     - "string"
   * - lineItems.quantity
     - items.quantity
     - N/A
   * - lineItems.quantity.quantity
     - items.quantity
     - "float"


Wix.com Products to Wave Product
--------------------------------
Every Wix.com Products will be synchronized with a Wave Product.

Once a link between a Wix.com Products and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - price.price
     - unitPrice
     - "string"
   * - priceData.price
     - unitPrice
     - "string"

