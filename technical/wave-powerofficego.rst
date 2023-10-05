========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-10-05 06:06:17

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Currency to PowerOfficeGo Currency
---------------------------------------
Before any synchronization can take place, a link between a Wave Currency and a PowerOfficeGo Currency must be established.

A Wave Currency will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Wave Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Wave Customer to PowerOfficeGo Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wave Customer if it is connected to a Wave Invoice, or Customer that is synchronized into PowerOfficeGo.

Once a link between a Wave Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


Wave Customer to PowerOfficeGo Customers
----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Wave Customer if it is connected to a Wave Invoice, or Customer that is synchronized into PowerOfficeGo.

Once a link between a Wave Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - name
     - Name
     - "string"
   * - phone
     - Number
     - "string"
   * - shippingDetails.phone
     - Number
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Invoice to PowerOfficeGo Salesorders
-----------------------------------------
Before any synchronization can take place, a link between a Wave Invoice and a PowerOfficeGo Salesorders must be established.

A new PowerOfficeGo Salesorders will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into PowerOfficeGo.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type


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

