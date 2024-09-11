===============================
WebCRM to Exact Online Dataflow
===============================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to ExactOnline Quotations
----------------------------------------------
Every WebCRM Opportunities will be synchronized with a ExactOnline Quotations.

Once a link between a WebCRM Opportunities and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - OpportunityCurrencyName
     - Currency
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


WebCRM Organisations to ExactOnline Accounts
--------------------------------------------
Every WebCRM Organisations will be synchronized with a ExactOnline Accounts.

Once a link between a WebCRM Organisations and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - OrganisationName
     - Name
     - "string"


WebCRM Quotationline to ExactOnline Quotations
----------------------------------------------
Every WebCRM Quotationline will be synchronized with a ExactOnline Quotations.

Once a link between a WebCRM Quotationline and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


WebCRM Users to ExactOnline Contacts
------------------------------------
Every WebCRM Users will be synchronized with a ExactOnline Contacts.

Once a link between a WebCRM Users and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type


WebCRM Persons to Exact Online Contacts
---------------------------------------
Every WebCRM Persons will be synchronized with a Exact Online Contacts.

Once a link between a WebCRM Persons and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - document_number
     - BirthDate
     - "string"


WebCRM Products to Exact Online Items
-------------------------------------
Every WebCRM Products will be synchronized with a Exact Online Items.

Once a link between a WebCRM Products and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Exact Online Items Property
     - Exact Online Data Type


WebCRM Quotationline to Exact Online Salesorderlines
----------------------------------------------------
Every WebCRM Quotationline will be synchronized with a Exact Online Salesorderlines.

Once a link between a WebCRM Quotationline and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - QuotationLineCostPrice
     - CostPriceFC
     - "string"
   * - QuotationLineDiscount
     - CostPriceFC
     - "string"
   * - QuotationLineOpportunityId
     - OrderID
     - "string"
   * - QuotationLinePrice
     - CostPriceFC
     - "string"
   * - QuotationLineQuantity
     - CostPriceFC
     - "string"
   * - QuotationLineVatPercentage
     - CostPriceFC
     - "string"

