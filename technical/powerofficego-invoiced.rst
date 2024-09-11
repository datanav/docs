===================================
PowerOffice GO to Invoiced Dataflow
===================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Customers to Invoiced Customers company
-----------------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a Invoiced Customers company.

Once a link between a PowerOfficeGO Customers and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


PowerOfficeGO Customers person to Invoiced Customers person
-----------------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a Invoiced Customers person.

Once a link between a PowerOfficeGO Customers person and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Invoiced Customers person Property
     - Invoiced Data Type
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - address1
     - "string"
   * - MailAddress.AddressLine2
     - address2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - postal_code
     - "string"


PowerOfficeGO Product to Invoiced Items
---------------------------------------
Every PowerOfficeGO Product will be synchronized with a Invoiced Items.

Once a link between a PowerOfficeGO Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - costPrice
     - unit_cost
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"


PowerOfficeGO Salesorderlines to Invoiced Lineitem
--------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a PowerOfficeGO Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - Allowance
     - items.discounts
     - "string"
   * - Description
     - items.name
     - "string"
   * - ProductUnitPrice
     - items.amount
     - "string"
   * - Quantity
     - items.quantity
     - "string"


PowerOfficeGO Salesorders to Invoiced Invoices
----------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a PowerOfficeGO Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer
     - "string"
   * - CustomerReferenceContactPersonId
     - customer
     - "string"

