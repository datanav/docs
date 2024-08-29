====================
HubSpot to  Dataflow
====================

Generated: 2024-08-29 09:15:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Customer
----------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Customer must be established.

A new  Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, or Quotequotetemplateassociation that is synchronized into .

Once a link between a HubSpot Company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Customer Property
     -  Data Type
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


HubSpot Contact to  Customer
----------------------------
Every HubSpot Contact will be synchronized with a  Customer.

Once a link between a HubSpot Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Customer Property
     -  Data Type
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - first_name
     - "string"
   * - properties.lastname
     - last_name
     - "string"


HubSpot Company to  Business_entity
-----------------------------------
Every HubSpot Company will be synchronized with a  Business_entity.

Once a link between a HubSpot Company and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Business_entity Property
     -  Data Type
   * - properties.name
     - name
     - "string"


HubSpot Contactcompanyassociation to  Customer
----------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Customer.

Once a link between a HubSpot Contactcompanyassociation and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Customer Property
     -  Data Type


HubSpot Dealcompanyassociation to  Order
----------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a  Order.

Once a link between a HubSpot Dealcompanyassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     -  Order Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Dealcontactassociation to  Order
----------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a  Order.

Once a link between a HubSpot Dealcontactassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     -  Order Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Lineitem to  Order
--------------------------
Every HubSpot Lineitem will be synchronized with a  Order.

Once a link between a HubSpot Lineitem and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Order Property
     -  Data Type
   * - properties.description
     - order_line_items.description
     - "string"
   * - properties.price
     - order_line_items.unit_price
     - "string"
   * - properties.quantity
     - order_line_items.amount
     - "string"


HubSpot Lineitemdealassociation to  Order
-----------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a  Order.

Once a link between a HubSpot Lineitemdealassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Order Property
     -  Data Type


HubSpot Lineitemquoteassociation to  Order
------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a  Order.

Once a link between a HubSpot Lineitemquoteassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     -  Order Property
     -  Data Type


HubSpot Quote to  Order
-----------------------
Every HubSpot Quote will be synchronized with a  Order.

Once a link between a HubSpot Quote and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     -  Order Property
     -  Data Type
   * - associations.companies.results.id
     - customer_id
     - "string"
   * - associations.contacts.results.id
     - customer_id
     - "string"


HubSpot Quotecompanyassociation to  Order
-----------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a  Order.

Once a link between a HubSpot Quotecompanyassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     -  Order Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Quotecontactassociation to  Order
-----------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a  Order.

Once a link between a HubSpot Quotecontactassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     -  Order Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customer_id
     - "string"


HubSpot Quotedealassociation to  Order
--------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a  Order.

Once a link between a HubSpot Quotedealassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     -  Order Property
     -  Data Type


HubSpot Quotequotetemplateassociation to  Order
-----------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a  Order.

Once a link between a HubSpot Quotequotetemplateassociation and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     -  Order Property
     -  Data Type


HubSpot User to  Customer
-------------------------
Every HubSpot User will be synchronized with a  Customer.

Once a link between a HubSpot User and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Customer Property
     -  Data Type


HubSpot Deal to  Order
----------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Order.

Once a link between a HubSpot Deal and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Order Property
     -  Data Type
   * - properties.deal_currency_code
     - currency_code
     - "string"


HubSpot Product to  Item
------------------------
Every HubSpot Product will be synchronized with a  Item.

Once a link between a HubSpot Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Item:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Item Property
     -  Data Type

