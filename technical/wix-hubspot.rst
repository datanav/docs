====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Contact
----------------------------
Every Wix.com Contacts will be synchronized with a  Contact.

If a matching  Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Wix.com Contacts will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contact Property
   * - primaryInfo.email
     - properties.email

Once a link between a Wix.com Contacts and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contact Property
     -  Data Type
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


Wix.com Members to  Contact
---------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Contact must be established.

A Wix.com Members will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contact Property
   * - loginEmail
     - properties.email

Once a link between a Wix.com Members and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contact Property
     -  Data Type
   * - loginEmail
     - properties.email
     - "string"


Wix.com Orders to  Lineitem
---------------------------
Every Wix.com Orders will be synchronized with a  Lineitem.

Once a link between a Wix.com Orders and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Lineitem Property
     -  Data Type
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
     - "string", "integer", "decimal"]]
   * - lineItems.quantity.quantity
     - properties.quantity
     - "string"


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
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

