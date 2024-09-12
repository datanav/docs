===========================
Zendesk to HubSpot Dataflow
===========================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to HubSpot Contact
--------------------------------
Every Zendesk Users will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Zendesk Users will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Zendesk Users will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Zendesk Users and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.email
     - "string"
   * - role
     - properties.country
     - "string"


Zendesk Organizations to HubSpot Company
----------------------------------------
Every Zendesk Organizations will be synchronized with a HubSpot Company.

Once a link between a Zendesk Organizations and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Zendesk Users to HubSpot User
-----------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a HubSpot User.

Once a link between a Zendesk Users and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - HubSpot User Property
     - HubSpot Data Type

