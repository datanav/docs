========================
HubSpot to Wave Dataflow
========================

Generated: 2023-08-17 09:33:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wave Customer must be established.

A new Wave Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wave.

Once a link between a HubSpot Company and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wave Customer Property
     - Wave Data Type
   * - properties.address
     - shippingDetails.address.addressLine1
     - "string"
   * - properties.address2
     - shippingDetails.address.addressLine2
     - "string"
   * - properties.city
     - shippingDetails.address.city
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
     - "string"
   * - properties.phone
     - shippingDetails.phone
     - "string"
   * - properties.zip
     - shippingDetails.address.postalCode
     - "string"


HubSpot Deal to Wave Invoice
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Wave Invoice.

Once a link between a HubSpot Deal and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wave Invoice Property
     - Wave Data Type


HubSpot Product to Wave Product
-------------------------------
Every HubSpot Product will be synchronized with a Wave Product.

Once a link between a HubSpot Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Wave Product Property
     - Wave Data Type

