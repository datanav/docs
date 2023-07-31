=========================
Asana to HubSpot Dataflow
=========================

Generated: 2023-07-31 10:54:09

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to HubSpot Company
------------------------------
Every Asana Teams will be synchronized with a HubSpot Company.

Once a link between a Asana Teams and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - html_description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - permalink_url
     - properties.website
     - "string"


Asana Users to HubSpot Contact
------------------------------
Every Asana Users will be synchronized with a HubSpot Contact.

Once a link between a Asana Users and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.email
     - "string"
   * - name
     - properties.firstname
     - "string"


Asana Workspaces to HubSpot Company
-----------------------------------
Every Asana Workspaces will be synchronized with a HubSpot Company.

Once a link between a Asana Workspaces and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - email_domains
     - properties.website
     - "string"
   * - name
     - properties.name
     - "string"

