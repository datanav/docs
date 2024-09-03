==================
Exact to  Dataflow
==================

Generated: 2024-09-03 08:20:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Organisations
--------------------------------
Every Exact Accounts will be synchronized with a  Organisations.

Once a link between a Exact Accounts and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Organisations Property
     -  Data Type


Exact Departments to  Organisations
-----------------------------------
Every Exact Departments will be synchronized with a  Organisations.

Once a link between a Exact Departments and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     -  Organisations Property
     -  Data Type


Exact Divisions to  Organisations
---------------------------------
Every Exact Divisions will be synchronized with a  Organisations.

Once a link between a Exact Divisions and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     -  Organisations Property
     -  Data Type


Exact Contacts to  Persons
--------------------------
Every Exact Contacts will be synchronized with a  Persons.

Once a link between a Exact Contacts and a  Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a  Persons:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     -  Persons Property
     -  Data Type
   * - BirthDate
     - document_number
     - "string"


Exact Items to  Products
------------------------
Every Exact Items will be synchronized with a  Products.

Once a link between a Exact Items and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Products:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Products Property
     -  Data Type


Exact Salesorderlines to  Quotationline
---------------------------------------
Every Exact Salesorderlines will be synchronized with a  Quotationline.

Once a link between a Exact Salesorderlines and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Quotationline Property
     -  Data Type
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

