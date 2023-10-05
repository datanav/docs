=================================
Wix.com to PowerOfficeGo Dataflow
=================================

Generated: 2023-10-05 06:06:18

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to PowerOfficeGo Currency
--------------------------------------------
Before any synchronization can take place, a link between a Wix.com Currencies and a PowerOfficeGo Currency must be established.

A Wix.com Currencies will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Wix.com Currencies and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Wix.com Contacts to PowerOfficeGo Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - EmailAddress
     - "string"


Wix.com Contacts to PowerOfficeGo Customers
-------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Wix.com Members to PowerOfficeGo Customers
------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Wix.com Members if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Members and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - loginEmail
     - EmailAddress
     - "string"


Wix.com Orders to PowerOfficeGo Salesorders
-------------------------------------------
Before any synchronization can take place, a link between a Wix.com Orders and a PowerOfficeGo Salesorders must be established.

A new PowerOfficeGo Salesorders will be created from a Wix.com Orders if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Orders and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type


Wix.com Orders to PowerOfficeGo Outgoinginvoices
------------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Wix.com Orders and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - buyerInfo.contactId
     - customerId
     - "string"
   * - buyerInfo.id
     - customerId
     - "string"
   * - currency
     - CurrencyCode
     - "string"
   * - id
     - OrderNo
     - "string"
   * - totals.total
     - NetAmount
     - "string"

