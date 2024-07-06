===========================
Wix.com to Hubspot Dataflow
===========================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Hubspot Contact
-----------------------------------
Every Wix.com Contacts will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Wix.com Contacts will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Hubspot Contact Property
   * - primaryInfo.email
     - properties.email

Once a link between a Wix.com Contacts and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - info.addresses.items.address.countryFullname
     - properties.country
     - "string"
   * - info.addresses.items.address.countryFullname
     - properties.state
     - "string"
   * - info.emails
     - properties.email
     - "string"
   * - info.name.first
     - properties.firstname
     - "string"
   * - info.name.last
     - properties.lastname
     - "string"
   * - info.phones
     - properties.mobilephone
     - "string"
   * - primaryInfo.email
     - properties.email
     - "string"
   * - primaryInfo.phone
     - properties.mobilephone
     - "string"
   * - primaryInfo.phone
     - properties.phone
     - "string"


Wix.com Members to Hubspot Contact
----------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Hubspot Contact must be established.

A Wix.com Members will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Hubspot Contact Property
   * - loginEmail
     - properties.email

Once a link between a Wix.com Members and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - loginEmail
     - properties.email
     - "string"


Wix.com Orders to Hubspot Lineitem
----------------------------------
Every Wix.com Orders will be synchronized with a Hubspot Lineitem.

Once a link between a Wix.com Orders and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - lineItems.name
     - properties.name
     - "string"
   * - lineItems.name.name
     - properties.name
     - "string"
   * - lineItems.price
     - properties.price
     - "string"
   * - lineItems.price.price
     - properties.price
     - "string"
   * - lineItems.productId
     - properties.hs_product_id
     - "string"
   * - lineItems.productId.productId
     - properties.hs_product_id
     - "string"
   * - lineItems.quantity
     - properties.quantity
     - N/A
   * - lineItems.quantity.quantity
     - properties.quantity
     - "string"


Wix.com Products to Hubspot Product
-----------------------------------
Every Wix.com Products will be synchronized with a Hubspot Product.

Once a link between a Wix.com Products and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - costAndProfitData.itemCost
     - properties.hs_cost_of_goods_sold
     - "string"
   * - costRange.maxValue
     - properties.hs_cost_of_goods_sold
     - "string"
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - price.price
     - properties.price
     - "string"
   * - priceData.price
     - properties.price
     - "string"
   * - sku
     - properties.hs_sku
     - "string"

