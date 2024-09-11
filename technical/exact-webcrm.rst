==============================
ExactOnline to WebCRM Dataflow
==============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to WebCRM Organisations
--------------------------------------
Every Exact Accounts will be synchronized with a WebCRM Organisations.

Once a link between a Exact Accounts and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"


Exact Departments to WebCRM Organisations
-----------------------------------------
Every Exact Departments will be synchronized with a WebCRM Organisations.

Once a link between a Exact Departments and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


Exact Divisions to WebCRM Organisations
---------------------------------------
Every Exact Divisions will be synchronized with a WebCRM Organisations.

Once a link between a Exact Divisions and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


ExactOnline Contacts to WebCRM Persons
--------------------------------------
Every ExactOnline Contacts will be synchronized with a WebCRM Persons.

Once a link between a ExactOnline Contacts and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - BirthDate
     - document_number
     - "string"


ExactOnline Items to WebCRM Products
------------------------------------
Every ExactOnline Items will be synchronized with a WebCRM Products.

Once a link between a ExactOnline Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - WebCRM Products Property
     - WebCRM Data Type


ExactOnline Salesorderlines to WebCRM Quotationline
---------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a ExactOnline Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - CostPriceFC
     - QuotationLineCostPrice
     - "string"
   * - CostPriceFC
     - QuotationLineDiscount
     - "string"
   * - CostPriceFC
     - QuotationLinePrice
     - "string"
   * - CostPriceFC
     - QuotationLineQuantity
     - "string"
   * - CostPriceFC
     - QuotationLineVatPercentage
     - "string"
   * - OrderID
     - QuotationLineOpportunityId
     - "string"

