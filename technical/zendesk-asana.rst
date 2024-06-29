=========================
Zendesk to Asana Dataflow
=========================

Generated: 2024-06-29 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Asana Workspaces
-----------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a Asana Workspaces must be established.

A new Asana Workspaces will be created from a Zendesk Organizations if it is connected to a Zendesk Tickets that is synchronized into Asana.

Once a link between a Zendesk Organizations and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Asana Workspaces Property
     - Asana Data Type
   * - name
     - name
     - "string"
   * - url
     - email_domains
     - "string"

