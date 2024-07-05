===========================
Zendesk to Hubspot Dataflow
===========================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Hubspot Contact
--------------------------------
Every Zendesk Users will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Zendesk Users will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Zendesk Users will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Zendesk Users and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - email
     - properties.email
     - "string"
   * - role
     - properties.country
     - "string"


Zendesk Organizations to Hubspot Company
----------------------------------------
Every Zendesk Organizations will be synchronized with a Hubspot Company.

Once a link between a Zendesk Organizations and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Zendesk Users to Hubspot User
-----------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a Hubspot User.

Once a link between a Zendesk Users and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Hubspot User Property
     - Hubspot Data Type

