================================
Business Nxt to HubSpot Dataflow
================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to HubSpot Company
---------------------------------------
Every Business Nxt Address will be synchronized with a HubSpot Company.

Once a link between a Business Nxt Address and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"
   * - phone
     - properties.phone
     - "string"


Business Nxt Company to HubSpot Company
---------------------------------------
Every Business Nxt Company will be synchronized with a HubSpot Company.

Once a link between a Business Nxt Company and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


Business Nxt Order to HubSpot Deal
----------------------------------
Every Business Nxt Order will be synchronized with a HubSpot Deal.

Once a link between a Business Nxt Order and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - name
     - properties.dealname
     - "string"
   * - orderDate
     - properties.closedate
     - "string"


Business Nxt Orderline to HubSpot Lineitem
------------------------------------------
Every Business Nxt Orderline will be synchronized with a HubSpot Lineitem.

Once a link between a Business Nxt Orderline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


Business Nxt Orderline to HubSpot Lineitemdealassociationtype
-------------------------------------------------------------
Every Business Nxt Orderline will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Business Nxt Orderline and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Business Nxt Orderline to HubSpot Lineitemquoteassociationtype
--------------------------------------------------------------
Every Business Nxt Orderline will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Business Nxt Orderline and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


Business Nxt Product to HubSpot Product
---------------------------------------
Every Business Nxt Product will be synchronized with a HubSpot Product.

Once a link between a Business Nxt Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - description
     - properties.description
     - "string"
   * - priceQuantity
     - properties.price
     - "string"

