===================================
Business Central to WebCRM Dataflow
===================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to WebCRM Organisations
--------------------------------------------------
Every Business Central Companies will be synchronized with a WebCRM Organisations.

Once a link between a Business Central Companies and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - WebCRM Organisations Property
     - WebCRM Data Type


Business Central Customers company to WebCRM Organisations
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a WebCRM Organisations.

Once a link between a Business Central Customers company and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - displayName
     - OrganisationName
     - "string"
   * - phoneNumber
     - OrganisationTelephone
     - "string"


Business Central Contacts person to WebCRM Persons
--------------------------------------------------
Every Business Central Contacts person will be synchronized with a WebCRM Persons.

Once a link between a Business Central Contacts person and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
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


Business Central Items to WebCRM Products
-----------------------------------------
Every Business Central Items will be synchronized with a WebCRM Products.

Once a link between a Business Central Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
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


Business Central Salesorderlines to WebCRM Quotationline
--------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a Business Central Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
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

