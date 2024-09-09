========================
Webcrm to Exact Dataflow
========================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Exact Quotations
----------------------------------------
Every Webcrm Opportunities will be synchronized with a Exact Quotations.

Once a link between a Webcrm Opportunities and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Exact Quotations Property
     - Exact Data Type
   * - OpportunityCurrencyName
     - Currency
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


Webcrm Organisations to Exact Accounts
--------------------------------------
Every Webcrm Organisations will be synchronized with a Exact Accounts.

Once a link between a Webcrm Organisations and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Exact Accounts Property
     - Exact Data Type
   * - OrganisationName
     - Name
     - "string"


Webcrm Quotationline to Exact Quotations
----------------------------------------
Every Webcrm Quotationline will be synchronized with a Exact Quotations.

Once a link between a Webcrm Quotationline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Exact Quotations Property
     - Exact Data Type


Webcrm Users to Exact Contacts
------------------------------
Every Webcrm Users will be synchronized with a Exact Contacts.

Once a link between a Webcrm Users and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Exact Contacts Property
     - Exact Data Type


Webcrm Persons to Exact Contacts
--------------------------------
Every Webcrm Persons will be synchronized with a Exact Contacts.

Once a link between a Webcrm Persons and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Exact Contacts Property
     - Exact Data Type
   * - document_number
     - BirthDate
     - "string"


Webcrm Products to Exact Items
------------------------------
Every Webcrm Products will be synchronized with a Exact Items.

Once a link between a Webcrm Products and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Exact Items Property
     - Exact Data Type


Webcrm Quotationline to Exact Salesorderlines
---------------------------------------------
Every Webcrm Quotationline will be synchronized with a Exact Salesorderlines.

Once a link between a Webcrm Quotationline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
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

