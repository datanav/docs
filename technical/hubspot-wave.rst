========================
HubSpot to Wave Dataflow
========================

Generated: 2024-09-13 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wave Customer person must be established.

A new Wave Customer person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wave.

A HubSpot Contact will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wave Customer person Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wave Customer person Property
     - Wave Data Type
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.address
     - shippingDetails.address.addressLine1
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
     - address.countryCode
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
     - "string"
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - N/A
   * - properties.mobilephone
     - mobile
     - "string"
   * - properties.phone
     - phone
     - "string"
   * - properties.state
     - address.province.code
     - "string"
   * - properties.state
     - shippingDetails.address.province.code
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - shippingDetails.address.postalCode
     - "string"


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
     - address.countryCode
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
     - "string"
   * - properties.description
     - id
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
   * - properties.state
     - address.province
     - "string"
   * - properties.state
     - address.province.code
     - "string"
   * - properties.state
     - shippingDetails.address.province.code
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

A new Wave Customer person will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wave.

Once a link between a HubSpot Company and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wave Customer person Property
     - Wave Data Type
   * - id
     - id
     - "string"
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
     - address.countryCode
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
     - "string"
   * - properties.state
     - address.province
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"
   * - properties.zip
     - shippingDetails.address.postalCode
     - "string"


HubSpot Contact to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wave Customer must be established.

A new Wave Customer will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wave.

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
   * - properties.address
     - shippingDetails.address.addressLine1
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
     - address.countryCode
     - "string"
   * - properties.country
     - shippingDetails.address.country.code
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
   * - properties.state
     - address.province.code
     - "string"
   * - properties.state
     - shippingDetails.address.province.code
     - "string"
   * - properties.zip
     - address.postalCode
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
   * - properties.deal_currency_code
     - currency.code
     - "string"
   * - properties.dealname
     - memo
     - "string"
   * - properties.dealname
     - title
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

