====================
HubSpot to  Dataflow
====================

Generated: 2023-11-30 20:56:59

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Product to  Items
-------------------------
Every HubSpot Product will be synchronized with a  Items.

Once a link between a HubSpot Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Items Property
     -  Data Type


HubSpot Company to  Company
---------------------------
Every HubSpot Company will be synchronized with a  Company.

Once a link between a HubSpot Company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Company Property
     -  Data Type


HubSpot Deal to  Salesorders
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Salesorders.

Once a link between a HubSpot Deal and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Salesorders Property
     -  Data Type
   * - properties.amount
     - totalAmountExcludingTax
     - "string"
   * - properties.closedate
     - orderDate
     - "string"
   * - properties.closedate
     - requestedDeliveryDate
     - "string"


HubSpot Lineitem to  Salesorderlines
------------------------------------
Every HubSpot Lineitem will be synchronized with a  Salesorderlines.

Once a link between a HubSpot Lineitem and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Salesorderlines Property
     -  Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_product_id
     - itemId
     - "string"
   * - properties.price
     - amountExcludingTax
     - "string"
   * - properties.price
     - unitPrice
     - "string"
   * - properties.quantity
     - invoiceQuantity
     - "string"
   * - properties.quantity
     - quantity
     - "string"


HubSpot Lineitemdealassociation to  Salesorderlines
---------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a  Salesorderlines.

Once a link between a HubSpot Lineitemdealassociation and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Salesorderlines Property
     -  Data Type

