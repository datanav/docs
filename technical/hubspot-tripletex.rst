=============================
HubSpot to Tripletex Dataflow
=============================

Generated: 2023-10-05 06:16:43

Introduction.
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
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - properties.phone
     - phoneNumberWork
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
     - "datetime-format","%Y-%m-%d","_."]
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
     - "string"
   * - properties.phone
     - phoneNumberWork
     - "string"
   * - properties.zip
     - address.postalCode
     - "string"


HubSpot Company to Tripletex Contact
------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Contact Property
     - Tripletex Data Type


HubSpot Company to Tripletex Customer
-------------------------------------
Every HubSpot Company will be synchronized with a Tripletex Customer.

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

A new Tripletex Customer will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into Tripletex.

Once a link between a HubSpot Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type


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


HubSpot Contactcompanyassociationtype to Tripletex Customercategory
-------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Contactcompanyassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Deal to Tripletex Order
-------------------------------
Every HubSpot Deal will be synchronized with a Tripletex Order.

Once a link between a HubSpot Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Dealcompanyassociation to Tripletex Order
-------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Dealcompanyassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - contact.id
     - "integer"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "integer"


HubSpot Dealcompanyassociationtype to Tripletex Customercategory
----------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Dealcompanyassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Dealcontactassociation to Tripletex Order
-------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Dealcontactassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - contact.id
     - "integer"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "integer"


HubSpot Dealcontactassociationtype to Tripletex Customercategory
----------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Dealcontactassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Lineitem to Tripletex Order
-----------------------------------
Every HubSpot Lineitem will be synchronized with a Tripletex Order.

Once a link between a HubSpot Lineitem and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Lineitemdealassociation to Tripletex Order
--------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Lineitemdealassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Lineitemdealassociationtype to Tripletex Customercategory
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Lineitemdealassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Lineitemquoteassociation to Tripletex Order
---------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Lineitemquoteassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Lineitemquoteassociationtype to Tripletex Customercategory
------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Lineitemquoteassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Quote to Tripletex Order
--------------------------------
Every HubSpot Quote will be synchronized with a Tripletex Order.

Once a link between a HubSpot Quote and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - associations.companies.results.id
     - customer.id
     - "integer"
   * - associations.contacts.results.id
     - contact.id
     - "integer"
   * - properties.hs_title
     - invoiceComment
     - "string"


HubSpot Quotecompanyassociation to Tripletex Order
--------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Quotecompanyassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - contact.id
     - "integer"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "integer"


HubSpot Quotecompanyassociationtype to Tripletex Customercategory
-----------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Quotecompanyassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Quotecontactassociation to Tripletex Order
--------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Quotecontactassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - contact.id
     - "integer"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "integer"


HubSpot Quotecontactassociationtype to Tripletex Customercategory
-----------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Quotecontactassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Quotedealassociation to Tripletex Order
-----------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Quotedealassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Quotedealassociationtype to Tripletex Customercategory
--------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Quotedealassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Quotequotetemplateassociation to Tripletex Order
--------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Quotequotetemplateassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Quotequotetemplateassociationtype to Tripletex Customercategory
-----------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"


HubSpot Ticket to Tripletex Project
-----------------------------------
Every HubSpot Ticket will be synchronized with a Tripletex Project.

Once a link between a HubSpot Ticket and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Tripletex Project Property
     - Tripletex Data Type


HubSpot Ticketcompanyassociation to Tripletex Order
---------------------------------------------------
Every HubSpot Ticketcompanyassociation will be synchronized with a Tripletex Order.

Once a link between a HubSpot Ticketcompanyassociation and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - toObjectId (Dependant on having wd:Q760086 in sesam_simpleAssociationTypes)
     - contact.id
     - "integer"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer.id
     - "integer"


HubSpot Ticketcompanyassociationtype to Tripletex Customercategory
------------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Tripletex Customercategory.

Once a link between a HubSpot Ticketcompanyassociationtype and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - label
     - name
     - "string"

