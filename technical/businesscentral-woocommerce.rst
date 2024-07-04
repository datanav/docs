============================
Businesscentral to  Dataflow
============================

Generated: 2024-07-04 09:43:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Products
----------------------------------
Every Businesscentral Items will be synchronized with a  Products.

Once a link between a Businesscentral Items and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Products Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - price
     - "string"
   * - unitPrice
     - sale_price
     - "string"

