=======================
HubSpot to Wix Dataflow
=======================

Generated: 2023-11-07 15:54:17

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Wix Contacts
-------------------------------
Every HubSpot Contact will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the HubSpot Contact will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A HubSpot Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
   * - properties.email
     - info.emails
   * - properties.email
     - primaryInfo.email

Once a link between a HubSpot Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - id
     - id
     - "string"
   * - properties.email
     - info.emails
     - "string"
   * - properties.email
     - primaryInfo.email
     - "string"
   * - properties.firstname
     - info.name.first
     - "string"
   * - properties.lastname
     - info.name.last
     - "string"
   * - properties.mobilephone
     - info.phones
     - "string"
   * - properties.mobilephone
     - primaryInfo.phone
     - "string"


HubSpot Contact to Wix Members
------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wix Members must be established.

A HubSpot Contact will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
   * - properties.email
     - loginEmail

Once a link between a HubSpot Contact and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Members:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
     - Wix Data Type
   * - properties.email
     - loginEmail
     - "string"


HubSpot Company to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wix Contacts must be established.

A new Wix Contacts will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wix.

Once a link between a HubSpot Company and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wix Contacts Property
     - Wix Data Type


HubSpot Company to Wix Members
------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wix Members must be established.

A new Wix Members will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Wix.

Once a link between a HubSpot Company and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wix Members:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wix Members Property
     - Wix Data Type


HubSpot Contactcompanyassociation to Wix Contacts
-------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Wix Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Wix Contacts Property
     - Wix Data Type


HubSpot Dealcompanyassociation to Wix Orders
--------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Dealcompanyassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Wix Orders Property
     - Wix Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.contactId
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.id
     - "string"


HubSpot Dealcontactassociation to Wix Orders
--------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Dealcontactassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Wix Orders Property
     - Wix Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.contactId
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.id
     - "string"


HubSpot Lineitem to Wix Orders
------------------------------
Every HubSpot Lineitem will be synchronized with a Wix Orders.

Once a link between a HubSpot Lineitem and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Wix Orders Property
     - Wix Data Type
   * - properties.hs_product_id
     - lineItems.productId
     - "string"
   * - properties.hs_product_id
     - lineItems.productId.productId
     - "string"
   * - properties.name
     - lineItems.name
     - "string"
   * - properties.name
     - lineItems.name.name
     - "string"
   * - properties.price
     - lineItems.price
     - "string"
   * - properties.price
     - lineItems.price.price
     - "string"
   * - properties.quantity
     - lineItems.quantity
     - "integer"
   * - properties.quantity
     - lineItems.quantity.quantity
     - "string"


HubSpot Lineitemdealassociation to Wix Orders
---------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Lineitemdealassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Wix Orders Property
     - Wix Data Type


HubSpot Lineitemquoteassociation to Wix Orders
----------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Lineitemquoteassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Wix Orders Property
     - Wix Data Type


HubSpot Quote to Wix Orders
---------------------------
Every HubSpot Quote will be synchronized with a Wix Orders.

Once a link between a HubSpot Quote and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Wix Orders Property
     - Wix Data Type
   * - associations.companies.results.id
     - buyerInfo.contactId
     - "string"
   * - associations.companies.results.id
     - buyerInfo.id
     - "string"
   * - associations.contacts.results.id
     - buyerInfo.id
     - "string"
   * - properties.hs_quote_amount
     - totals.total
     - "string"


HubSpot Quotecompanyassociation to Wix Orders
---------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Quotecompanyassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Wix Orders Property
     - Wix Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.contactId
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.id
     - "string"


HubSpot Quotecontactassociation to Wix Orders
---------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Quotecontactassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Wix Orders Property
     - Wix Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.contactId
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.id
     - "string"


HubSpot Quotedealassociation to Wix Orders
------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Quotedealassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Wix Orders Property
     - Wix Data Type


HubSpot Quotequotetemplateassociation to Wix Orders
---------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Quotequotetemplateassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Wix Orders Property
     - Wix Data Type


HubSpot Ticketcompanyassociation to Wix Orders
----------------------------------------------
Every HubSpot Ticketcompanyassociation will be synchronized with a Wix Orders.

Once a link between a HubSpot Ticketcompanyassociation and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - Wix Orders Property
     - Wix Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.contactId
     - "string"
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - buyerInfo.id
     - "string"


HubSpot User to Wix Contacts
----------------------------
Every HubSpot User will be synchronized with a Wix Contacts.

Once a link between a HubSpot User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Wix Contacts Property
     - Wix Data Type


HubSpot Deal to Wix Orders
--------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Wix Orders.

Once a link between a HubSpot Deal and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wix Orders Property
     - Wix Data Type
   * - properties.amount
     - totals.total
     - "string"
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Product to Wix Inventory
--------------------------------
Every HubSpot Product will be synchronized with a Wix Inventory.

Once a link between a HubSpot Product and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Wix Inventory Property
     - Wix Data Type


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
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costRange.maxValue
     - "string"
   * - properties.hs_sku
     - sku
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - price.price
     - "string"
   * - properties.price
     - priceData.price
     - "decimal"

