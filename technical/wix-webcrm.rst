==========================
Wix.com to Webcrm Dataflow
==========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Webcrm Persons
----------------------------------
Every Wix.com Contacts will be synchronized with a Webcrm Persons.

Once a link between a Wix.com Contacts and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - info.name.first
     - PersonFirstName
     - "string"
   * - info.name.last
     - PersonLastName
     - "string"
   * - primaryInfo.phone
     - PersonDirectPhone
     - "string"


Wix.com Orders to Webcrm Quotationline
--------------------------------------
Every Wix.com Orders will be synchronized with a Webcrm Quotationline.

Once a link between a Wix.com Orders and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - lineItems.price
     - QuotationLinePrice
     - "string"
   * - lineItems.quantity
     - QuotationLineQuantity
     - "string"


Wix.com Products to Webcrm Products
-----------------------------------
Every Wix.com Products will be synchronized with a Webcrm Products.

Once a link between a Wix.com Products and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - costAndProfitData.itemCost
     - ProductCostPrice
     - "string"
   * - costRange.maxValue
     - ProductCostPrice
     - "string"
   * - priceData.price
     - ProductPrice
     - "string"

