==============================
Webcrm to Superoffice Dataflow
==============================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Superoffice Sale
----------------------------------------
Every Webcrm Opportunities will be synchronized with a Superoffice Sale.

Once a link between a Webcrm Opportunities and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Superoffice Sale Property
     - Superoffice Data Type
   * - OpportunityCurrencyName
     - Currency.Id
     - "integer"


Webcrm Products to Superoffice Product
--------------------------------------
Every Webcrm Products will be synchronized with a Superoffice Product.

Once a link between a Webcrm Products and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - ProductCostPrice
     - UnitCost
     - "string"
   * - ProductPrice
     - UnitListPrice
     - N/A
   * - ProductVatCode
     - VAT
     - N/A


Webcrm Quotationline to Superoffice Quoteline
---------------------------------------------
Every Webcrm Quotationline will be synchronized with a Superoffice Quoteline.

Once a link between a Webcrm Quotationline and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Superoffice Quoteline Property
     - Superoffice Data Type

