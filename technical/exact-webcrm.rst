========================
Exact to Webcrm Dataflow
========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Webcrm Organisations
--------------------------------------
Every Exact Accounts will be synchronized with a Webcrm Organisations.

Once a link between a Exact Accounts and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Name
     - OrganisationName
     - "string"


Exact Departments to Webcrm Organisations
-----------------------------------------
Every Exact Departments will be synchronized with a Webcrm Organisations.

Once a link between a Exact Departments and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


Exact Divisions to Webcrm Organisations
---------------------------------------
Every Exact Divisions will be synchronized with a Webcrm Organisations.

Once a link between a Exact Divisions and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Description
     - OrganisationCompanyDescription
     - "string"


Exact Contacts to Webcrm Persons
--------------------------------
Every Exact Contacts will be synchronized with a Webcrm Persons.

Once a link between a Exact Contacts and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - BirthDate
     - document_number
     - "string"


Exact Items to Webcrm Products
------------------------------
Every Exact Items will be synchronized with a Webcrm Products.

Once a link between a Exact Items and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Webcrm Products Property
     - Webcrm Data Type


Exact Salesorderlines to Webcrm Quotationline
---------------------------------------------
Every Exact Salesorderlines will be synchronized with a Webcrm Quotationline.

Once a link between a Exact Salesorderlines and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
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

