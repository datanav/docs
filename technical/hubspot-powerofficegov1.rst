===================================
HubSpot to PowerOfficeGov1 Dataflow
===================================

Generated: 2023-08-14 08:49:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOfficeGov1 Employee
-------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGov1 Employee must be established.

A HubSpot Contact will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Employee Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


HubSpot Contact to PowerOfficeGov1 Person
-----------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGov1 Person must be established.

A HubSpot Contact will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Person Property
   * - properties.email
     - Emails.Value

Once a link between a HubSpot Contact and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type


HubSpot Account to PowerOfficeGov1 Teams
----------------------------------------
Every HubSpot Account will be synchronized with a PowerOfficeGov1 Teams.

Once a link between a HubSpot Account and a PowerOfficeGov1 Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a PowerOfficeGov1 Teams:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - PowerOfficeGov1 Teams Property
     - PowerOfficeGov1 Data Type


HubSpot Deal to PowerOfficeGov1 Invoice
---------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a HubSpot Deal and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type


HubSpot Deal to PowerOfficeGov1 Order
-------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGov1 Order.

Once a link between a HubSpot Deal and a PowerOfficeGov1 Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGov1 Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Order Property
     - PowerOfficeGov1 Data Type


HubSpot Deal to PowerOfficeGov1 Salesorder
------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a HubSpot Deal and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type


HubSpot Lineitemdealassociation to PowerOfficeGov1 Orderline
------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGov1 Orderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Orderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGov1 Orderline Property
     - PowerOfficeGov1 Data Type


HubSpot Lineitemdealassociation to PowerOfficeGov1 Quoteline
------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGov1 Quoteline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Quoteline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGov1 Quoteline Property
     - PowerOfficeGov1 Data Type


HubSpot Lineitemdealassociation to PowerOfficeGov1 Salesorderline
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGov1 Salesorderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGov1 Salesorderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGov1 Salesorderline Property
     - PowerOfficeGov1 Data Type


HubSpot Product to PowerOfficeGov1 Product
------------------------------------------
Every HubSpot Product will be synchronized with a PowerOfficeGov1 Product.

Once a link between a HubSpot Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type


HubSpot Ticket to PowerOfficeGov1 Tickets
-----------------------------------------
Every HubSpot Ticket will be synchronized with a PowerOfficeGov1 Tickets.

Once a link between a HubSpot Ticket and a PowerOfficeGov1 Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a PowerOfficeGov1 Tickets:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - PowerOfficeGov1 Tickets Property
     - PowerOfficeGov1 Data Type

