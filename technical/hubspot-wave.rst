========================
HubSpot to Wave Dataflow
========================

Generated: 2023-06-22 14:16:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Account to Wave Currency
--------------------------------
Every HubSpot Account will be synchronized with a Wave Currency.

Once a link between a HubSpot Account and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Wave Currency Property
     - Wave Data Type


HubSpot Deal to Wave Currency
-----------------------------
Every HubSpot Deal will be synchronized with a Wave Currency.

Once a link between a HubSpot Deal and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Wave Currency Property
     - Wave Data Type


HubSpot Product to Wave Product
-------------------------------
Every HubSpot Product will be synchronized with a Wave Product.

Once a link between a HubSpot Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Wave Product Property
     - Wave Data Type
   * - properties.description
     - description
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - unitPrice
     - "string"

