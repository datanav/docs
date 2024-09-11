===============================
WebCRM to Exact Online Dataflow
===============================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Exact Quotations
----------------------------------------
Every WebCRM Opportunities will be synchronized with a Exact Quotations.

Once a link between a WebCRM Opportunities and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Exact Quotations Property
     - Exact Data Type
   * - OpportunityCurrencyName
     - Currency
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


WebCRM Organisations to Exact Accounts
--------------------------------------
Every WebCRM Organisations will be synchronized with a Exact Accounts.

Once a link between a WebCRM Organisations and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Exact Accounts Property
     - Exact Data Type
   * - OrganisationName
     - Name
     - "string"


WebCRM Quotationline to Exact Quotations
----------------------------------------
Every WebCRM Quotationline will be synchronized with a Exact Quotations.

Once a link between a WebCRM Quotationline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Exact Quotations Property
     - Exact Data Type


WebCRM Users to Exact Contacts
------------------------------
Every WebCRM Users will be synchronized with a Exact Contacts.

Once a link between a WebCRM Users and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Exact Contacts Property
     - Exact Data Type


WebCRM Persons to Exact Contacts
--------------------------------
Every WebCRM Persons will be synchronized with a Exact Contacts.

Once a link between a WebCRM Persons and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Exact Contacts Property
     - Exact Data Type
   * - document_number
     - BirthDate
     - "string"


WebCRM Products to Exact Items
------------------------------
Every WebCRM Products will be synchronized with a Exact Items.

Once a link between a WebCRM Products and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Exact Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Exact Items Property
     - Exact Data Type


WebCRM Quotationline to Exact Salesorderlines
---------------------------------------------
Every WebCRM Quotationline will be synchronized with a Exact Salesorderlines.

Once a link between a WebCRM Quotationline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Exact Salesorderlines Property
     - Exact Data Type
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

