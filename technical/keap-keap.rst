=====================
Keap to Keap Dataflow
=====================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Keap Product
----------------------------
Before any synchronization can take place, a link between a Keap Product and a Keap Product must be established.

A Keap Product will merge with a Keap Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Keap Product Property
   * - sku
     - sku

Once a link between a Keap Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Keap Product Property
     - Keap Data Type

