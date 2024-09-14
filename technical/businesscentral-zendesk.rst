====================================
Business Central to Zendesk Dataflow
====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to Zendesk Organizations
---------------------------------------------------
Every Business Central Companies will be synchronized with a Zendesk Organizations.

Once a link between a Business Central Companies and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Zendesk Organizations Property
     - Zendesk Data Type


Business Central Customers company to Zendesk Organizations
-----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Zendesk Organizations.

Once a link between a Business Central Customers company and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - displayName
     - name
     - "string"

