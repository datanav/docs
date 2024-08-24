====================
HubSpot to  Dataflow
====================

Generated: 2024-08-24 08:14:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
     - currency
     - "string"


HubSpot Product to  Product
---------------------------
Every HubSpot Product will be synchronized with a  Product.

Once a link between a HubSpot Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Product Property
     -  Data Type

