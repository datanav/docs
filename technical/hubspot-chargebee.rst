=============================
HubSpot to Chargebee Dataflow
=============================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Chargebee Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, or Quotequotetemplateassociation that is synchronized into Chargebee.

Once a link between a HubSpot Company and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - properties.country
     - billing_address.country
     - "string"
   * - properties.industry
     - billing_address.country
     - "string"
   * - properties.state
     - billing_address.country
     - "string"
   * - properties.type
     - billing_address.country
     - "string"


HubSpot Contact to Chargebee Customer
-------------------------------------
Every HubSpot Contact will be synchronized with a Chargebee Customer.

Once a link between a HubSpot Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - first_name
     - "string"
   * - properties.lastname
     - last_name
     - "string"


HubSpot Company to Chargebee Business_entity
--------------------------------------------
Every HubSpot Company will be synchronized with a Chargebee Business_entity.

Once a link between a HubSpot Company and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - properties.name
     - name
     - "string"


HubSpot Contactcompanyassociation to Chargebee Customer
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Chargebee Customer.

Once a link between a HubSpot Contactcompanyassociation and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Chargebee Customer Property
     - Chargebee Data Type


HubSpot Contactcompanyassociationtype to Chargebee Currency
-----------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Contactcompanyassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Dealcompanyassociation to Chargebee Order
-------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Dealcompanyassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Dealcompanyassociationtype to Chargebee Currency
--------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Dealcompanyassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Dealcontactassociation to Chargebee Order
-------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Dealcontactassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Dealcontactassociationtype to Chargebee Currency
--------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Dealcontactassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Lineitem to Chargebee Order
-----------------------------------
Every HubSpot Lineitem will be synchronized with a Chargebee Order.

Once a link between a HubSpot Lineitem and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - properties.description
     - order_line_items.description
     - "string"
   * - properties.price
     - order_line_items.unit_price
     - "string"
   * - properties.quantity
     - order_line_items.amount
     - "string"


HubSpot Lineitemdealassociation to Chargebee Order
--------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Lineitemdealassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Chargebee Order Property
     - Chargebee Data Type


HubSpot Lineitemdealassociationtype to Chargebee Currency
---------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Lineitemdealassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Lineitemquoteassociation to Chargebee Order
---------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Lineitemquoteassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Chargebee Order Property
     - Chargebee Data Type


HubSpot Lineitemquoteassociationtype to Chargebee Currency
----------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Lineitemquoteassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Quote to Chargebee Order
--------------------------------
Every HubSpot Quote will be synchronized with a Chargebee Order.

Once a link between a HubSpot Quote and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - associations.companies.results.id
     - customer_id
     - "string"
   * - associations.contacts.results.id
     - customer_id
     - "string"


HubSpot Quotecompanyassociation to Chargebee Order
--------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Quotecompanyassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Quotecompanyassociationtype to Chargebee Currency
---------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Quotecompanyassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Quotecontactassociation to Chargebee Order
--------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Quotecontactassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Quotecontactassociationtype to Chargebee Currency
---------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Quotecontactassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Quotedealassociation to Chargebee Order
-----------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Quotedealassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Chargebee Order Property
     - Chargebee Data Type


HubSpot Quotedealassociationtype to Chargebee Currency
------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Quotedealassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot Quotequotetemplateassociation to Chargebee Order
--------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Chargebee Order.

Once a link between a HubSpot Quotequotetemplateassociation and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Chargebee Order Property
     - Chargebee Data Type


HubSpot Quotequotetemplateassociationtype to Chargebee Currency
---------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Chargebee Currency.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Chargebee Currency Property
     - Chargebee Data Type


HubSpot User to Chargebee Customer
----------------------------------
Every HubSpot User will be synchronized with a Chargebee Customer.

Once a link between a HubSpot User and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Chargebee Customer Property
     - Chargebee Data Type


HubSpot Deal to Chargebee Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Chargebee Order.

Once a link between a HubSpot Deal and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - properties.deal_currency_code
     - currency_code
     - "string"


HubSpot Product to Chargebee Item
---------------------------------
Every HubSpot Product will be synchronized with a Chargebee Item.

Once a link between a HubSpot Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - properties.name
     - name
     - "string"

