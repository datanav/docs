=============================
HubSpot to Tripletex Dataflow
=============================

Generated: 2023-06-27 05:05:49

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Tripletex Customer
-------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Tripletex.

Once a link between a HubSpot Company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Tripletex Customer Property
     - Tripletex Data Type


HubSpot Deal to Tripletex Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Tripletex Order.

Once a link between a HubSpot Deal and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Tripletex Order Property
     - Tripletex Data Type


HubSpot Lineitemdealassociation to Tripletex Orderline
------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Tripletex Orderline.

Once a link between a HubSpot Lineitemdealassociation and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Tripletex Orderline Property
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


HubSpot User to Tripletex Employee
----------------------------------
Every HubSpot User will be synchronized with a Tripletex Employee.

Once a link between a HubSpot User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Tripletex Employee Property
     - Tripletex Data Type

