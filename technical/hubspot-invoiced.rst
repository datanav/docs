============================
HubSpot to Invoiced Dataflow
============================

Generated: 2024-09-21 00:00:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to Invoiced Invoices
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Invoiced Invoices.

Once a link between a HubSpot Deal and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Invoiced Invoices Property
     - Invoiced Data Type


HubSpot Lineitem to Invoiced Lineitem
-------------------------------------
Every HubSpot Lineitem will be synchronized with a Invoiced Lineitem.

Once a link between a HubSpot Lineitem and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


HubSpot Lineitemdealassociationtype to Invoiced Lineitem
--------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Invoiced Lineitem.

Once a link between a HubSpot Lineitemdealassociationtype and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


HubSpot Lineitemquoteassociationtype to Invoiced Lineitem
---------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Invoiced Lineitem.

Once a link between a HubSpot Lineitemquoteassociationtype and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


HubSpot Product to Invoiced Items
---------------------------------
Every HubSpot Product will be synchronized with a Invoiced Items.

Once a link between a HubSpot Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - unit_cost
     - "string"
   * - properties.name
     - name
     - "string"

