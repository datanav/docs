========================
HubSpot to Wave Dataflow
========================

Generated: 2023-09-17 18:22:11

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
     - address.addressLine1
     - "string"
   * - properties.address
     - shippingDetails.address.addressLine1
     - "string"
   * - properties.address2
     - address.addressLine2
     - "string"
   * - properties.address2
     - shippingDetails.address.addressLine2
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.city
     - shippingDetails.address.city
     - "string"
   * - properties.country
     - address.country.code
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
     - "string"
   * - properties.description
     - internalNotes
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phone
     - "string"
   * - properties.phone
     - shippingDetails.phone
     - "string"
   * - properties.website
     - website
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - shippingDetails.address.postalCode
     - "string"


HubSpot Company to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wave Customer person must be established.

A new Wave Customer person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Wave.

Once a link between a HubSpot Company and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wave Customer person Property
     - Wave Data Type
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.address2
     - address.addressLine2
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.country
     - address.country.code
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"


HubSpot Contact to Wave Customer
--------------------------------
Every HubSpot Contact will be synchronized with a Wave Customer.

Once a link between a HubSpot Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.country
     - address.country.code
     - "string"
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.mobilephone
     - mobile
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"


HubSpot Contactcompanyassociation to Wave Customer
--------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Wave Customer.

Once a link between a HubSpot Contactcompanyassociation and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Wave Customer Property
     - Wave Data Type


HubSpot User to Wave Customer
-----------------------------
Every HubSpot User will be synchronized with a Wave Customer.

Once a link between a HubSpot User and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Wave Customer Property
     - Wave Data Type


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
   * - properties.deal_currency_code
     - currency.code
     - "string"
   * - properties.dealname
     - memo
     - "string"
   * - properties.description
     - memo
     - "string"


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
   * - properties.description
     - description
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - unitPrice
     - "string"

