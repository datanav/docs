===========================
Zohocrm to Hubspot Dataflow
===========================

Generated: 2024-03-26 14:19:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zohocrm to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zohocrm Deal to Hubspot Deal
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Hubspot Deal.

Once a link between a Zohocrm Deal and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zohocrm Deal and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - Zohocrm Deal Property
     - Hubspot Deal Property
     - Hubspot Data Type

