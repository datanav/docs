========================
HubSpot to Keap Dataflow
========================

Generated: 2024-09-14 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Keap Companies
---------------------------------
Every HubSpot Company will be synchronized with a Keap Companies.

Once a link between a HubSpot Company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Keap Companies Property
     - Keap Data Type
   * - id
     - id
     - "string"
   * - properties.city
     - address.locality
     - "string"
   * - properties.name
     - company_name
     - "string"
   * - properties.zip
     - address.zip_code
     - "string"


HubSpot Contact to Keap Contacts
--------------------------------
Every HubSpot Contact will be synchronized with a Keap Contacts.

Once a link between a HubSpot Contact and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Keap Contacts Property
     - Keap Data Type
   * - properties.date_of_birth
     - birthday
     - "string"


HubSpot Contactcompanyassociation to Keap Contacts
--------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Keap Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Keap Contacts Property
     - Keap Data Type


HubSpot User to Keap Contacts
-----------------------------
Every HubSpot User will be synchronized with a Keap Contacts.

Once a link between a HubSpot User and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Keap Contacts Property
     - Keap Data Type


HubSpot Deal to Keap Opportunity
--------------------------------
Every HubSpot Deal will be synchronized with a Keap Opportunity.

Once a link between a HubSpot Deal and a Keap Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Keap Opportunity:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Keap Opportunity Property
     - Keap Data Type
   * - properties.dealname
     - opportunity_title
     - "string"
   * - properties.hubspot_owner_id
     - contact.id
     - "string"


HubSpot Product to Keap Product
-------------------------------
Every HubSpot Product will be synchronized with a Keap Product.

Once a link between a HubSpot Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Keap Product Property
     - Keap Data Type
   * - properties.description
     - product_desc
     - "string"
   * - properties.name
     - product_name
     - "string"
   * - properties.price
     - product_price
     - "string"

