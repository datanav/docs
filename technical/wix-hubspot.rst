===========================
Wix.com to HubSpot Dataflow
===========================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to HubSpot Contact
-----------------------------------
Every Wix.com Contacts will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Wix.com Contacts will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Wix.com Contacts will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
   * - primaryInfo.email
     - properties.email

Once a link between a Wix.com Contacts and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - info.name.first
     - properties.firstname
     - "string"
   * - info.name.last
     - properties.lastname
     - "string"
   * - primaryInfo.email
     - properties.email
     - "string"
   * - primaryInfo.phone
     - properties.phone
     - "string"


Wix.com Members to HubSpot Contact
----------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a HubSpot Contact must be established.

A Wix.com Members will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
   * - loginEmail
     - properties.email

Once a link between a Wix.com Members and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - loginEmail
     - properties.email
     - "string"


Wix.com Orders to HubSpot Deal
------------------------------
Every Wix.com Orders will be synchronized with a HubSpot Deal.

Once a link between a Wix.com Orders and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - currency
     - properties.deal_currency_code
     - "string"
   * - totals.total
     - properties.amount
     - "string"


Wix.com Orders to HubSpot Lineitem
----------------------------------
Every Wix.com Orders will be synchronized with a HubSpot Lineitem.

Once a link between a Wix.com Orders and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - lineItems.name
     - properties.name
     - "string"
   * - lineItems.price
     - properties.price
     - "string"
   * - lineItems.productId
     - properties.hs_product_id
     - "string"
   * - lineItems.quantity
     - properties.quantity
     - N/A


Wix.com Orders to HubSpot Lineitemdealassociationtype
-----------------------------------------------------
Every Wix.com Orders will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Wix.com Orders and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Wix.com Orders to HubSpot Lineitemquoteassociationtype
------------------------------------------------------
Every Wix.com Orders will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Wix.com Orders and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


Wix.com Products to HubSpot Product
-----------------------------------
Every Wix.com Products will be synchronized with a HubSpot Product.

Once a link between a Wix.com Products and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - costAndProfitData.itemCost
     - properties.hs_cost_of_goods_sold
     - "string"
   * - costRange.maxValue
     - properties.hs_cost_of_goods_sold
     - "string"
   * - name
     - properties.name
     - "string"
   * - priceData.price
     - properties.price
     - "string"
   * - sku
     - properties.hs_sku
     - "string"

