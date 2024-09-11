===================================
BusinessCentral to Zendesk Dataflow
===================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Companies to Zendesk Organizations
-------------------------------------------
Every Business Companies will be synchronized with a Zendesk Organizations.

Once a link between a Business Companies and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - Zendesk Organizations Property
     - Zendesk Data Type


Business Customers company to Zendesk Organizations
---------------------------------------------------
Every Business Customers company will be synchronized with a Zendesk Organizations.

Once a link between a Business Customers company and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - displayName
     - name
     - "string"

