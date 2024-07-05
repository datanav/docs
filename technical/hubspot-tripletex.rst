=============================
HubSpot to Tripletex Dataflow
=============================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

A HubSpot Contact will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Contact Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type
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
     - phoneNumberMobile
     - N/A
   * - properties.phone
     - phoneNumberWork
     - "string"


HubSpot Contact to Tripletex Customer person
--------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

A HubSpot Contact will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Customer person Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - deliveryAddress.addressLine1
     - "string"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address
     - postalAddress.addressLine1
     - "string"
   * - properties.city
     - deliveryAddress.city
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.city
     - postalAddress.city
     - "string"
   * - properties.country
     - deliveryAddress.country.id
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.country
     - postalAddress.country.id
     - "integer"
   * - properties.email
     - email
     - "string"
   * - properties.mobilephone
     - phoneNumberMobile
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.zip
     - deliveryAddress.postalCode
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"
   * - properties.zip
     - postalAddress.postalCode
     - "string"


HubSpot Contact to Tripletex Employee
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Employee must be established.

A HubSpot Contact will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Employee Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - address.addressLine1
     - "string"
   * - properties.city
     - address.city
     - "string"
   * - properties.country
     - address.country.id
     - "integer"
   * - properties.date_of_birth
     - dateOfBirth
     - N/A
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
     - phoneNumberMobile
     - N/A
   * - properties.phone
     - phoneNumberWork
     - "string"
   * - properties.work_email
     - email
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"


HubSpot Company to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Contact Property
     - Tripletex Data Type


HubSpot Company to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - deliveryAddress.addressLine1
     - "string"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address
     - postalAddress.addressLine1
     - "string"
   * - properties.address2
     - deliveryAddress.addressLine2
     - "string"
   * - properties.address2
     - physicalAddress.addressLine2
     - "string"
   * - properties.address2
     - postalAddress.addressLine2
     - "string"
   * - properties.city
     - deliveryAddress.city
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.city
     - postalAddress.city
     - "string"
   * - properties.country
     - deliveryAddress.country.id
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.country
     - postalAddress.country.id
     - "integer"
   * - properties.industry
     - isPrivateIndividual
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.type
     - isPrivateIndividual
     - "string"
   * - properties.website
     - url
     - "string"
   * - properties.website
     - website
     - "string"
   * - properties.zip
     - deliveryAddress.postalCode
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"
   * - properties.zip
     - postalAddress.postalCode
     - "string"


HubSpot Company to Tripletex Customer person
--------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - deliveryAddress.addressLine1
     - "string"
   * - properties.address
     - physicalAddress.addressLine1
     - "string"
   * - properties.address
     - postalAddress.addressLine1
     - "string"
   * - properties.address2
     - deliveryAddress.addressLine2
     - "string"
   * - properties.address2
     - physicalAddress.addressLine2
     - "string"
   * - properties.address2
     - postalAddress.addressLine2
     - "string"
   * - properties.city
     - deliveryAddress.city
     - "string"
   * - properties.city
     - physicalAddress.city
     - "string"
   * - properties.city
     - postalAddress.city
     - "string"
   * - properties.country
     - deliveryAddress.country.id
     - "string"
   * - properties.country
     - physicalAddress.country.id
     - "integer"
   * - properties.country
     - postalAddress.country.id
     - "integer"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.website
     - website
     - "string"
   * - properties.zip
     - deliveryAddress.postalCode
     - "string"
   * - properties.zip
     - physicalAddress.postalCode
     - "string"
   * - properties.zip
     - postalAddress.postalCode
     - "string"


HubSpot Contact to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Tripletex.

Once a link between a HubSpot Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


HubSpot Deal to Tripletex Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Tripletex Order.

Once a link between a HubSpot Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - properties.closedate
     - deliveryDate
     - N/A
   * - properties.closedate
     - orderDate
     - N/A
   * - properties.deal_currency_code
     - currency.id
     - "integer"
   * - properties.dealname
     - invoiceComment
     - "string"


HubSpot Lineitem to Tripletex Orderline
---------------------------------------
Every HubSpot Lineitem will be synchronized with a Tripletex Orderline.

Once a link between a HubSpot Lineitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_discount_percentage
     - discount
     - "float"
   * - properties.hs_product_id
     - product.id
     - "integer"
   * - properties.name
     - description
     - "string"
   * - properties.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - properties.quantity
     - count
     - N/A


HubSpot Product to Tripletex Product
------------------------------------
Every HubSpot Product will be synchronized with a Tripletex Product.

Once a link between a HubSpot Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costExcludingVatCurrency
     - "integer"
   * - properties.hs_sku
     - number
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - priceExcludingVatCurrency
     - "float"

