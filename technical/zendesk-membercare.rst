==============================
Zendesk to Membercare Dataflow
==============================

Generated: 2024-09-03 09:00:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Companies
-----------------------------------
Every Zendesk Organizations will be synchronized with a  Companies.

Once a link between a Zendesk Organizations and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Companies:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Companies Property
     -  Data Type
   * - name
     - companyName
     - "string"

