==========================
Wix.com to WebCRM Dataflow
==========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to WebCRM Persons
----------------------------------
Every Wix.com Contacts will be synchronized with a WebCRM Persons.

Once a link between a Wix.com Contacts and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - info.name.first
     - PersonFirstName
     - "string"
   * - info.name.last
     - PersonLastName
     - "string"
   * - primaryInfo.phone
     - PersonDirectPhone
     - "string"


Wix.com Orders to WebCRM Quotationline
--------------------------------------
Every Wix.com Orders will be synchronized with a WebCRM Quotationline.

Once a link between a Wix.com Orders and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - lineItems.price
     - QuotationLinePrice
     - "string"
   * - lineItems.quantity
     - QuotationLineQuantity
     - "string"


Wix.com Products to WebCRM Products
-----------------------------------
Every Wix.com Products will be synchronized with a WebCRM Products.

Once a link between a Wix.com Products and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - costAndProfitData.itemCost
     - ProductCostPrice
     - "string"
   * - costRange.maxValue
     - ProductCostPrice
     - "string"
   * - priceData.price
     - ProductPrice
     - "string"

