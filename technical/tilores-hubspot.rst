===========================
Tilores to HubSpot Dataflow
===========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to HubSpot Contact
--------------------------------
Every Tilores Human will be synchronized with a HubSpot Contact.

Once a link between a Tilores Human and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"

