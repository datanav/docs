===========================
HubSpot to Zendesk Dataflow
===========================

Generated: 2023-10-24 19:04:22

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Zendesk Users
--------------------------------
Every HubSpot Contact will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the HubSpot Contact will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A HubSpot Contact will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Zendesk Users Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Zendesk Users Property
     - Zendesk Data Type


HubSpot Company to Zendesk Organisations
----------------------------------------
Every HubSpot Company will be synchronized with a Zendesk Organisations.

Once a link between a HubSpot Company and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - properties.name
     - name
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Company to Zendesk Organizations
----------------------------------------
Every HubSpot Company will be synchronized with a Zendesk Organizations.

Once a link between a HubSpot Company and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - properties.country
     - tags
     - "string"
   * - properties.industry
     - tags
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.type
     - tags
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Contactcompanyassociation to Zendesk Users
--------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Zendesk Users.

Once a link between a HubSpot Contactcompanyassociation and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - toObjectId (Dependant on having wd:Q703534 in sesam_simpleAssociationTypes)
     - organization_id
     - "string"


HubSpot Ticket to Zendesk Ticketcomments
----------------------------------------
Every HubSpot Ticket will be synchronized with a Zendesk Ticketcomments.

Once a link between a HubSpot Ticket and a Zendesk Ticketcomments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Zendesk Ticketcomments:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Zendesk Ticketcomments Property
     - Zendesk Data Type
   * - properties.createdate
     - created_at
     - "string"


HubSpot User to Zendesk Users
-----------------------------
Every HubSpot User will be synchronized with a Zendesk Users.

Once a link between a HubSpot User and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Zendesk Users Property
     - Zendesk Data Type

