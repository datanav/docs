===========================
Shopify to HubSpot Dataflow
===========================

Generated: 2024-09-21 00:00:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to HubSpot Contact
-----------------------------------
Every Shopify Customer will be synchronized with a HubSpot Contact.

Once a link between a Shopify Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - default_address.phone
     - properties.phone
     - "string"
   * - email
     - properties.email
     - "string"
   * - first_name
     - properties.firstname
     - "string"
   * - last_name
     - properties.lastname
     - "string"
   * - phone
     - properties.mobilephone
     - "string"


Shopify Order to HubSpot Deal
-----------------------------
Every Shopify Order will be synchronized with a HubSpot Deal.

Once a link between a Shopify Order and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - created_at
     - properties.closedate
     - "string"
   * - currency
     - properties.deal_currency_code
     - "string"
   * - current_total_price
     - properties.amount
     - "string"
   * - name
     - properties.dealname
     - "string"
   * - total_price
     - properties.amount
     - "string"


Shopify Order to HubSpot Lineitem
---------------------------------
Every Shopify Order will be synchronized with a HubSpot Lineitem.

Once a link between a Shopify Order and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


Shopify Order to HubSpot Lineitemdealassociationtype
----------------------------------------------------
Every Shopify Order will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Shopify Order and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Shopify Order to HubSpot Lineitemquoteassociationtype
-----------------------------------------------------
Every Shopify Order will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Shopify Order and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


Shopify Sesamproduct to HubSpot Product
---------------------------------------
Every Shopify Sesamproduct will be synchronized with a HubSpot Product.

Once a link between a Shopify Sesamproduct and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - sesam_priceExclVAT
     - properties.price
     - "string"
   * - title
     - properties.name
     - "string"
   * - variants.sku
     - properties.hs_sku
     - "string"
   * - variants.title
     - properties.description
     - "string"

