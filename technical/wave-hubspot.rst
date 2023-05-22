==================================
Wave Financial to HubSpot Dataflow
==================================

Generated: 2023-05-22 13:53:26

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to HubSpot Company
--------------------------------
Every Wave Customer will be synchronized with a HubSpot Company.

Once a link between a Wave Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.addressLine2
     - properties.address2
     - "string"
   * - internalNotes
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - phone
     - properties.phone
     - "string"
   * - website
     - properties.website
     - "string"

