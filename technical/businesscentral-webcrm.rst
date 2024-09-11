===================================
Business Central to WebCRM Dataflow
===================================

Generated: 2024-09-11 07:52:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Business Contacts person to WebCRM Persons
------------------------------------------
Every Business Contacts person will be synchronized with a WebCRM Persons.

Once a link between a Business Contacts person and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - displayName
     - PersonName
     - "string"
   * - mobilePhoneNumber
     - PersonMobilePhone
     - "string"
   * - phoneNumber
     - PersonDirectPhone
     - "string"


Business Items to WebCRM Products
---------------------------------
Every Business Items will be synchronized with a WebCRM Products.

Once a link between a Business Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - inventory
     - ProductQuantity
     - "string"
   * - unitCost
     - ProductCostPrice
     - "string"
   * - unitPrice
     - ProductPrice
     - "string"


Business Salesorderlines to WebCRM Quotationline
------------------------------------------------
Every Business Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a Business Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
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

