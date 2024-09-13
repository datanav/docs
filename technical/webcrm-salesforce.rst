=============================
WebCRM to Salesforce Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Salesforce Invoice
------------------------------------------
Every WebCRM Opportunities will be synchronized with a Salesforce Invoice.

Once a link between a WebCRM Opportunities and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - OpportunityCurrencyName
     - CurrencyIsoCode
     - "string"
   * - OpportunityCurrencySymbol
     - Description
     - "string"


WebCRM Organisations to Salesforce Division
-------------------------------------------
Every WebCRM Organisations will be synchronized with a Salesforce Division.

Once a link between a WebCRM Organisations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - OrganisationName
     - Name
     - "string"


WebCRM Quotationline to Salesforce Invoice
------------------------------------------
Every WebCRM Quotationline will be synchronized with a Salesforce Invoice.

Once a link between a WebCRM Quotationline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


WebCRM Persons to Salesforce Contact
------------------------------------
Every WebCRM Persons will be synchronized with a Salesforce Contact.

Once a link between a WebCRM Persons and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
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


WebCRM Products to Salesforce Product2
--------------------------------------
Every WebCRM Products will be synchronized with a Salesforce Product2.

Once a link between a WebCRM Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type


WebCRM Quotationline to Salesforce Invoiceline
----------------------------------------------
Every WebCRM Quotationline will be synchronized with a Salesforce Invoiceline.

Once a link between a WebCRM Quotationline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
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


WebCRM Quotationline to Salesforce Orderitem
--------------------------------------------
Every WebCRM Quotationline will be synchronized with a Salesforce Orderitem.

Once a link between a WebCRM Quotationline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type


WebCRM Quotationline to Salesforce Quotelineitem
------------------------------------------------
Every WebCRM Quotationline will be synchronized with a Salesforce Quotelineitem.

Once a link between a WebCRM Quotationline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type

