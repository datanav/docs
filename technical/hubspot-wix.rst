=======================
HubSpot to Wix Dataflow
=======================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wix Contacts must be established.

A new Wix Contacts will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wix.

A HubSpot Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
   * - properties.email
     - primaryInfo.email

Once a link between a HubSpot Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - properties.email
     - primaryInfo.email
     - "string"
   * - properties.firstname
     - info.name.first
     - "string"
   * - properties.lastname
     - info.name.last
     - "string"
   * - properties.phone
     - primaryInfo.phone
     - "string"


HubSpot Product to Wix Products
-------------------------------
Every HubSpot Product will be synchronized with a Wix Products.

Once a link between a HubSpot Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Wix Products Property
     - Wix Data Type
   * - properties.hs_cost_of_goods_sold
     - costAndProfitData.itemCost
     - N/A
   * - properties.hs_sku
     - sku
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - priceData.price
     - N/A

