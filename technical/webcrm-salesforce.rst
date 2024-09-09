=============================
Webcrm to Salesforce Dataflow
=============================

Generated: 2024-09-09 10:36:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Salesforce Invoice
------------------------------------------
Every Webcrm Opportunities will be synchronized with a Salesforce Invoice.

Once a link between a Webcrm Opportunities and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - OpportunityCurrencyName
     - CurrencyIsoCode
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


Webcrm Organisations to Salesforce Division
-------------------------------------------
Every Webcrm Organisations will be synchronized with a Salesforce Division.

Once a link between a Webcrm Organisations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - OrganisationName
     - Name
     - "string"


Webcrm Quotationline to Salesforce Invoice
------------------------------------------
Every Webcrm Quotationline will be synchronized with a Salesforce Invoice.

Once a link between a Webcrm Quotationline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Webcrm Persons to Salesforce Contact
------------------------------------
Every Webcrm Persons will be synchronized with a Salesforce Contact.

Once a link between a Webcrm Persons and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - PersonDirectPhone
     - Phone
     - "string"
   * - PersonFirstName
     - FirstName
     - "string"
   * - PersonLastName
     - LastName
     - "string"
   * - PersonMobilePhone
     - MobilePhone
     - "string"
   * - document_number
     - Birthdate
     - "string"


Webcrm Products to Salesforce Product2
--------------------------------------
Every Webcrm Products will be synchronized with a Salesforce Product2.

Once a link between a Webcrm Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Webcrm Quotationline to Salesforce Invoiceline
----------------------------------------------
Every Webcrm Quotationline will be synchronized with a Salesforce Invoiceline.

Once a link between a Webcrm Quotationline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - QuotationLineCostPrice
     - Description
     - "string"
   * - QuotationLineDiscount
     - Description
     - "string"
   * - QuotationLinePrice
     - Description
     - "string"
   * - QuotationLineQuantity
     - Description
     - "string"
   * - QuotationLineVatPercentage
     - Description
     - "string"


Webcrm Quotationline to Salesforce Orderitem
--------------------------------------------
Every Webcrm Quotationline will be synchronized with a Salesforce Orderitem.

Once a link between a Webcrm Quotationline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type


Webcrm Quotationline to Salesforce Quotelineitem
------------------------------------------------
Every Webcrm Quotationline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Webcrm Quotationline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


Webcrm Quotationline to Salesforce Seller
-----------------------------------------
Every Webcrm Quotationline will be synchronized with a Salesforce Seller.

Once a link between a Webcrm Quotationline and a Salesforce Seller is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Salesforce Seller:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Salesforce Seller Property
     - Salesforce Data Type

