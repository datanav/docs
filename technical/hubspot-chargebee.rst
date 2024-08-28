====================
HubSpot to  Dataflow
====================

Generated: 2024-08-28 09:40:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Business_entity
-----------------------------------
Every HubSpot Company will be synchronized with a  Business_entity.

Once a link between a HubSpot Company and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Business_entity Property
     -  Data Type
   * - properties.name
     - name
     - "string"

