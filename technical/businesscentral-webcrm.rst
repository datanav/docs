==================================
Businesscentral to Webcrm Dataflow
==================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Webcrm Organisations
-------------------------------------------------
Every Businesscentral Companies will be synchronized with a Webcrm Organisations.

Once a link between a Businesscentral Companies and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Webcrm Organisations Property
     - Webcrm Data Type


Businesscentral Customers company to Webcrm Organisations
---------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Webcrm Organisations.

Once a link between a Businesscentral Customers company and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - displayName
     - OrganisationName
     - "string"
   * - phoneNumber
     - OrganisationTelephone
     - "string"


Businesscentral Contacts person to Webcrm Persons
-------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Webcrm Persons.

Once a link between a Businesscentral Contacts person and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - displayName
     - PersonName
     - "string"
   * - mobilePhoneNumber
     - PersonMobilePhone
     - "string"
   * - phoneNumber
     - PersonDirectPhone
     - "string"


Businesscentral Items to Webcrm Products
----------------------------------------
Every Businesscentral Items will be synchronized with a Webcrm Products.

Once a link between a Businesscentral Items and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - inventory
     - ProductQuantity
     - "string"
   * - unitCost
     - ProductCostPrice
     - "string"
   * - unitPrice
     - ProductPrice
     - "string"


Businesscentral Salesorderlines to Webcrm Quotationline
-------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Webcrm Quotationline.

Once a link between a Businesscentral Salesorderlines and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - discountPercent
     - QuotationLineDiscount
     - "string"
   * - documentId
     - QuotationLineOpportunityId
     - "string"
   * - quantity
     - QuotationLineQuantity
     - "string"
   * - taxPercent
     - QuotationLineVatPercentage
     - "string"
   * - unitPrice
     - QuotationLinePrice
     - "string"

