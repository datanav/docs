===============================
Exact Online to WebCRM Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to WebCRM Organisations
---------------------------------------------
Every Exact Online Accounts will be synchronized with a WebCRM Organisations.

Once a link between a Exact Online Accounts and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Name
     - OrganisationName
     - "string"


Exact Online Departments to WebCRM Organisations
------------------------------------------------
Every Exact Online Departments will be synchronized with a WebCRM Organisations.

Once a link between a Exact Online Departments and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


Exact Online Divisions to WebCRM Organisations
----------------------------------------------
Every Exact Online Divisions will be synchronized with a WebCRM Organisations.

Once a link between a Exact Online Divisions and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Divisions and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Online Divisions Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


Exact Online Contacts to WebCRM Persons
---------------------------------------
Every Exact Online Contacts will be synchronized with a WebCRM Persons.

Once a link between a Exact Online Contacts and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Contacts and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Exact Online Contacts Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - BirthDate
     - document_number
     - "string"


Exact Online Items to WebCRM Products
-------------------------------------
Every Exact Online Items will be synchronized with a WebCRM Products.

Once a link between a Exact Online Items and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - WebCRM Products Property
     - WebCRM Data Type


Exact Online Salesorderlines to WebCRM Quotationline
----------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a WebCRM Quotationline.

Once a link between a Exact Online Salesorderlines and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
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

