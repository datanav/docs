=========================
Keap to Invoiced Dataflow
=========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Invoiced Items
------------------------------
Every Keap Product will be synchronized with a Invoiced Items.

Once a link between a Keap Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - product_desc
     - description
     - "string"
   * - product_name
     - name
     - "string"

