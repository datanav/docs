============================
Invoiced to HubSpot Dataflow
============================

Generated: 2024-09-24 13:32:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers (organisation data) to HubSpot Company
---------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a HubSpot Company.

Once a link between a Invoiced Customers (organisation data) and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


Invoiced Customers (human data) to HubSpot Contact
--------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a HubSpot Contact.

Once a link between a Invoiced Customers (human data) and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - address1
     - properties.address
     - "string"
   * - city
     - properties.city
     - "string"
   * - country
     - properties.country
     - "string"
   * - id
     - id
     - "string"
   * - postal_code
     - properties.zip
     - "string"


Invoiced Invoices to HubSpot Deal
---------------------------------
Every Invoiced Invoices will be synchronized with a HubSpot Deal.

Once a link between a Invoiced Invoices and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - currency
     - properties.deal_currency_code
     - "string"


Invoiced Items to HubSpot Product
---------------------------------
Every Invoiced Items will be synchronized with a HubSpot Product.

Once a link between a Invoiced Items and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - unit_cost
     - properties.hs_cost_of_goods_sold
     - "string"


Invoiced Lineitem to HubSpot Lineitem
-------------------------------------
Every Invoiced Lineitem will be synchronized with a HubSpot Lineitem.

Once a link between a Invoiced Lineitem and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - items.amount
     - properties.price
     - "string"
   * - items.description
     - properties.description
     - "string"
   * - items.discounts
     - properties.hs_discount_percentage
     - "string"
   * - items.name
     - properties.name
     - "string"
   * - items.quantity
     - properties.quantity
     - N/A


Invoiced Lineitem to HubSpot Lineitemdealassociationtype
--------------------------------------------------------
Every Invoiced Lineitem will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Invoiced Lineitem and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Invoiced Lineitem to HubSpot Lineitemquoteassociationtype
---------------------------------------------------------
Every Invoiced Lineitem will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Invoiced Lineitem and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type

