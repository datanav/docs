===================================
PowerOffice GO to Invoiced Dataflow
===================================

Generated: 2024-09-11 07:52:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Customers to Invoiced Customers company
---------------------------------------------------
Every PowerOffice Customers will be synchronized with a Invoiced Customers company.

Once a link between a PowerOffice Customers and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


PowerOffice Customers person to Invoiced Customers person
---------------------------------------------------------
Every PowerOffice Customers person will be synchronized with a Invoiced Customers person.

Once a link between a PowerOffice Customers person and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
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


PowerOffice Product to Invoiced Items
-------------------------------------
Every PowerOffice Product will be synchronized with a Invoiced Items.

Once a link between a PowerOffice Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
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


PowerOffice Salesorderlines to Invoiced Lineitem
------------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a PowerOffice Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
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


PowerOffice Salesorders to Invoiced Invoices
--------------------------------------------
Every PowerOffice Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a PowerOffice Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
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

