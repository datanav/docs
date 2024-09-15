===================================
PowerOffice GO to Invoiced Dataflow
===================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Invoiced Customers company
------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Invoiced Customers company.

Once a link between a PowerOffice GO Customers and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Customers person to Invoiced Customers person
------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Invoiced Customers person.

Once a link between a PowerOffice GO Customers person and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Product to Invoiced Items
----------------------------------------
Every PowerOffice GO Product will be synchronized with a Invoiced Items.

Once a link between a PowerOffice GO Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
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


PowerOffice GO Salesorderlines to Invoiced Lineitem
---------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a PowerOffice GO Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
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


PowerOffice GO Salesorders to Invoiced Invoices
-----------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a PowerOffice GO Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
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

