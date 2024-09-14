============================
Invoiced to HubSpot Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to HubSpot Company
---------------------------------------------
Every Invoiced Customers company will be synchronized with a HubSpot Company.

Once a link between a Invoiced Customers company and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


Invoiced Customers person to HubSpot Contact
--------------------------------------------
Every Invoiced Customers person will be synchronized with a HubSpot Contact.

Once a link between a Invoiced Customers person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
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

