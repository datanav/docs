========================
HubSpot to Wave Dataflow
========================

Generated: 2023-06-23 11:19:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Wave Customer
--------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Wave Customer must be established.

A new Wave Customer will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Wave.

Once a link between a HubSpot Company and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Wave Customer Property
     - Wave Data Type
   * - properties.description
     - internalNotes
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.phone
     - phone
     - "string"
   * - properties.website
     - website
     - "string"

