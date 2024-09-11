===============================
BusinessNxt to HubSpot Dataflow
===============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Address to HubSpot Company
--------------------------------------
Every BusinessNxt Address will be synchronized with a HubSpot Company.

Once a link between a BusinessNxt Address and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"
   * - phone
     - properties.phone
     - "string"


BusinessNxt Company to HubSpot Company
--------------------------------------
Every BusinessNxt Company will be synchronized with a HubSpot Company.

Once a link between a BusinessNxt Company and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"


BusinessNxt Orderline to HubSpot Lineitem
-----------------------------------------
Every BusinessNxt Orderline will be synchronized with a HubSpot Lineitem.

Once a link between a BusinessNxt Orderline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


BusinessNxt Product to HubSpot Product
--------------------------------------
Every BusinessNxt Product will be synchronized with a HubSpot Product.

Once a link between a BusinessNxt Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - description
     - properties.description
     - "string"
   * - priceQuantity
     - properties.price
     - "string"

