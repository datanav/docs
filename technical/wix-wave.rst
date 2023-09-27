========================
Wix.com to Wave Dataflow
========================

Generated: 2023-09-27 07:38:59

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wave Customer person
----------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wave Customer person must be established.

A new Wave Customer person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

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
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - mobile
     - "string"


Wix.com Contacts to Wave Customer
---------------------------------
Every Wix.com Contacts will be synchronized with a Wave Customer.

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
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - mobile
     - "string"


Wix.com Members to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wave Customer person must be established.

A new Wave Customer person will be created from a Wix.com Members if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

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


Wix.com Members to Wave Customer
--------------------------------
Every Wix.com Members will be synchronized with a Wave Customer.

Once a link between a Wix.com Members and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wave Customer Property
     - Wave Data Type
   * - loginEmail
     - email
     - "string"


Wix.com Product to Wave Product
-------------------------------
Before any synchronization can take place, a link between a Wix.com Product and a Wave Product must be established.

A new Wave Product will be created from a Wix.com Product if it is connected to a Wix.com Wix-orders that is synchronized into Wave.

Once a link between a Wix.com Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Product Property
     - Wave Product Property
     - Wave Data Type


Wix.com Inventory to Wave Product
---------------------------------
Every Wix.com Inventory will be synchronized with a Wave Product.

Once a link between a Wix.com Inventory and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wave Product Property
     - Wave Data Type


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
     - "datetime-format","%Y-%m-%d","_."]
   * - lineItems.name
     - items.description
     - "string"
   * - lineItems.price
     - items.price
     - "float"
   * - lineItems.price
     - items.unitPrice
     - "float"
   * - lineItems.productId
     - items.product.id
     - "string"
   * - lineItems.quantity
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

