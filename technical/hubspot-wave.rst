========================
HubSpot to Wave Dataflow
========================

Generated: 2023-10-05 08:46:20

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Wave Customer
--------------------------------
Every HubSpot Company will be synchronized with a Wave Customer.

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
   * - properties.state
     - address.province
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


HubSpot Contact to Wave Customer person
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wave Customer person must be established.

A new Wave Customer person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wave.

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
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - properties.mobilephone
     - mobile
     - "string"
   * - properties.phone
     - phone
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
   * - toObjectId (Dependant on having wd:Q703534 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Dealcompanyassociation to Wave Invoice
----------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Dealcompanyassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Wave Invoice Property
     - Wave Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "string"


HubSpot Dealcontactassociation to Wave Invoice
----------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Dealcontactassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Wave Invoice Property
     - Wave Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "string"


HubSpot Lineitem to Wave Invoice
--------------------------------
Every HubSpot Lineitem will be synchronized with a Wave Invoice.

Once a link between a HubSpot Lineitem and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Wave Invoice Property
     - Wave Data Type
   * - properties.hs_product_id
     - items.product.id
     - "string"
   * - properties.name
     - items.description
     - "string"
   * - properties.price
     - items.price
     - "float"
   * - properties.quantity
     - items.quantity
     - "float"


HubSpot Lineitemdealassociation to Wave Invoice
-----------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Lineitemdealassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Wave Invoice Property
     - Wave Data Type


HubSpot Lineitemquoteassociation to Wave Invoice
------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Lineitemquoteassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Wave Invoice Property
     - Wave Data Type


HubSpot Quote to Wave Invoice
-----------------------------
Every HubSpot Quote will be synchronized with a Wave Invoice.

Once a link between a HubSpot Quote and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Wave Invoice Property
     - Wave Data Type
   * - associations.companies.results.id
     - customer.id
     - "string"
   * - associations.contacts.results.id
     - customer.id
     - "string"
   * - properties.hs_title
     - title
     - "string"


HubSpot Quotecompanyassociation to Wave Invoice
-----------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Quotecompanyassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Wave Invoice Property
     - Wave Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "string"


HubSpot Quotecontactassociation to Wave Invoice
-----------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Quotecontactassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Wave Invoice Property
     - Wave Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "string"


HubSpot Quotedealassociation to Wave Invoice
--------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Quotedealassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Wave Invoice Property
     - Wave Data Type


HubSpot Quotequotetemplateassociation to Wave Invoice
-----------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Quotequotetemplateassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Wave Invoice Property
     - Wave Data Type


HubSpot Ticketcompanyassociation to Wave Invoice
------------------------------------------------
Every HubSpot Ticketcompanyassociation will be synchronized with a Wave Invoice.

Once a link between a HubSpot Ticketcompanyassociation and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - Wave Invoice Property
     - Wave Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "string"


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

