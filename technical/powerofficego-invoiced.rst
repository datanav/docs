===================================
PowerOffice GO to Invoiced Dataflow
===================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Invoiced Customers (organisation data)
------------------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Invoiced Customers (organisation data).

Once a link between a PowerOffice GO Customers and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Customers to Invoiced Customers (human data)
-----------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Invoiced Customers (human data).

Once a link between a PowerOffice GO Customers and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type


PowerOffice GO Customers (organisation data) to Invoiced Customers (organisation data)
--------------------------------------------------------------------------------------
Every PowerOffice GO Customers (organisation data) will be synchronized with a Invoiced Customers (organisation data).

Once a link between a PowerOffice GO Customers (organisation data) and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (organisation data) and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (organisation data) Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


PowerOffice GO Customers (human data) to Invoiced Customers (human data)
------------------------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a Invoiced Customers (human data).

Once a link between a PowerOffice GO Customers (human data) and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - Invoiced Customers (human data) Property
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

