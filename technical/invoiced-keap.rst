=========================
Invoiced to Keap Dataflow
=========================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Items to Keap Product
------------------------------
Every Invoiced Items will be synchronized with a Keap Product.

Once a link between a Invoiced Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"

