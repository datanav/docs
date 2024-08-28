====================
HubSpot to  Dataflow
====================

Generated: 2024-08-28 12:31:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Customer
----------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Customer must be established.

A new  Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Customer Property
     -  Data Type


HubSpot Contact to  Customer
----------------------------
Every HubSpot Contact will be synchronized with a  Customer.

Once a link between a HubSpot Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Customer Property
     -  Data Type
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - first_name
     - "string"
   * - properties.lastname
     - last_name
     - "string"


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


HubSpot Contactcompanyassociation to  Customer
----------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Customer.

Once a link between a HubSpot Contactcompanyassociation and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Customer Property
     -  Data Type


HubSpot User to  Customer
-------------------------
Every HubSpot User will be synchronized with a  Customer.

Once a link between a HubSpot User and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Customer Property
     -  Data Type


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

