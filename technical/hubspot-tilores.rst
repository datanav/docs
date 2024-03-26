===========================
HubSpot to Tilores Dataflow
===========================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Human
-------------------------
Every HubSpot Contact will be synchronized with a  Human.

Once a link between a HubSpot Contact and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Human:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Human Property
     -  Data Type
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


HubSpot Contactcompanyassociation to  Human
-------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a  Human.

Once a link between a HubSpot Contactcompanyassociation and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a  Human:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     -  Human Property
     -  Data Type


HubSpot User to  Human
----------------------
Every HubSpot User will be synchronized with a  Human.

Once a link between a HubSpot User and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Human:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Human Property
     -  Data Type

