===============================
WebCRM to Exact Online Dataflow
===============================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Exact Online Quotations
-----------------------------------------------
Every WebCRM Opportunities will be synchronized with a Exact Online Quotations.

Once a link between a WebCRM Opportunities and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - OpportunityCurrencyName
     - Currency
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


WebCRM Organisations to Exact Online Accounts
---------------------------------------------
Every WebCRM Organisations will be synchronized with a Exact Online Accounts.

Once a link between a WebCRM Organisations and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - OrganisationName
     - Name
     - "string"


WebCRM Quotationline to Exact Online Quotations
-----------------------------------------------
Every WebCRM Quotationline will be synchronized with a Exact Online Quotations.

Once a link between a WebCRM Quotationline and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Exact Online Quotations Property
     - Exact Online Data Type


WebCRM Users to Exact Online Contacts
-------------------------------------
Every WebCRM Users will be synchronized with a Exact Online Contacts.

Once a link between a WebCRM Users and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Exact Online Contacts Property
     - Exact Online Data Type


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

