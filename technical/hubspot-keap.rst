====================
HubSpot to  Dataflow
====================

Generated: 2024-09-02 13:38:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Companies
-----------------------------
Every HubSpot Company will be synchronized with a  Companies.

Once a link between a HubSpot Company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Companies Property
     -  Data Type


HubSpot Contact to  Contacts
----------------------------
Every HubSpot Contact will be synchronized with a  Contacts.

Once a link between a HubSpot Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contacts Property
     -  Data Type


HubSpot Contactcompanyassociation to  Contacts
----------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Contacts.

Once a link between a HubSpot Contactcompanyassociation and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Contacts Property
     -  Data Type


HubSpot User to  Contacts
-------------------------
Every HubSpot User will be synchronized with a  Contacts.

Once a link between a HubSpot User and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Contacts Property
     -  Data Type


HubSpot Deal to  Opportunity
----------------------------
Every HubSpot Deal will be synchronized with a  Opportunity.

Once a link between a HubSpot Deal and a  Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Opportunity:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Opportunity Property
     -  Data Type
   * - properties.dealname
     - opportunity_title
     - "string"
   * - properties.hubspot_owner_id
     - contact.id
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
   * - properties.description
     - product_desc
     - "string"
   * - properties.name
     - product_name
     - "string"
   * - properties.price
     - product_price
     - "string"

