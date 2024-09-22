===============================
SuperOffice to Shopify Dataflow
===============================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to Shopify Sesamproduct
-------------------------------------------
Every SuperOffice Product will be synchronized with a Shopify Sesamproduct.

Once a link between a SuperOffice Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - Description
     - variants.title
     - "string"
   * - Name
     - title
     - "string"
   * - UnitListPrice
     - sesam_priceExclVAT
     - "string"

