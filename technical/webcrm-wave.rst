=======================
WebCRM to Wave Dataflow
=======================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Products to Wave Product
-------------------------------
Every WebCRM Products will be synchronized with a Wave Product.

Once a link between a WebCRM Products and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Wave Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Wave Product Property
     - Wave Data Type
   * - ProductPrice
     - unitPrice
     - "string"

