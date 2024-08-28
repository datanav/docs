====================
Zendesk to  Dataflow
====================

Generated: 2024-08-28 10:47:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Organisations
---------------------------------------
Every Zendesk Organizations will be synchronized with a  Organisations.

Once a link between a Zendesk Organizations and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Organisations Property
     -  Data Type
   * - name
     - OrganisationName
     - "string"

