===========================
HubSpot to Tilores Dataflow
===========================

Generated: 2024-07-01 00:00:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Tilores Human
--------------------------------
Every HubSpot Contact will be synchronized with a Tilores Human.

Once a link between a HubSpot Contact and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tilores Human Property
     - Tilores Data Type
   * - id
     - id
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.date_of_birth
     - dateOfBirth
     - "string"
   * - properties.email
     - email
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.zip
     - postalCode
     - "string"


HubSpot Contactcompanyassociation to Tilores Human
--------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Tilores Human.

Once a link between a HubSpot Contactcompanyassociation and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Tilores Human Property
     - Tilores Data Type


HubSpot User to Tilores Human
-----------------------------
Every HubSpot User will be synchronized with a Tilores Human.

Once a link between a HubSpot User and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Tilores Human Property
     - Tilores Data Type

