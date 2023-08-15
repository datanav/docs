=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-08-15 09:01:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Supplier to PowerOfficeGo Address
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Address must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


Powerofficego Suppliers to PowerOfficeGo Address
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGo Address must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


Powerofficego Salesorders to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - CreatedDateTimeOffset
     - createdDateTimeOffset
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - TotalAmount
     - NetAmount
     - "string"

