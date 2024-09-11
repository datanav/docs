==================================
BusinessCentral to WebCRM Dataflow
==================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


BusinessCentral Contacts person to WebCRM Persons
-------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a WebCRM Persons.

Once a link between a BusinessCentral Contacts person and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
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


BusinessCentral Items to WebCRM Products
----------------------------------------
Every BusinessCentral Items will be synchronized with a WebCRM Products.

Once a link between a BusinessCentral Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
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


BusinessCentral Salesorderlines to WebCRM Quotationline
-------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a BusinessCentral Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
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

