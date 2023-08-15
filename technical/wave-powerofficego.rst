========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-08-15 08:59:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to PowerOfficeGo Outgoinginvoices
----------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Wave Invoice and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - createdAt
     - createdDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - id
     - OrderNo
     - "string"
   * - total.value
     - NetAmount
     - "string"


Wave Invoice to PowerOfficeGo Salesorders
-----------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - createdAt
     - CreatedDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
   * - total.value
     - NetAmount
     - "string"


Wave Vendor to PowerOfficeGo Suppliers
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Suppliers.

Once a link between a Wave Vendor and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - website
     - WebsiteUrl
     - "string"

