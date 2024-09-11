==============================
Keap to PowerOfficeGO Dataflow
==============================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to PowerOfficeGO Product
-------------------------------------
Every Keap Product will be synchronized with a PowerOfficeGO Product.

Once a link between a Keap Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - product_desc
     - description
     - "string"
   * - product_name
     - name
     - "string"
   * - product_price
     - salesPrice
     - N/A

