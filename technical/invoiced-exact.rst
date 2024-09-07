==========================
Invoiced to Exact Dataflow
==========================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers person to Exact Contacts
-------------------------------------------
Every Invoiced Customers person will be synchronized with a Exact Contacts.

Once a link between a Invoiced Customers person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Exact Contacts Property
     - Exact Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"


Invoiced Invoices to Exact Quotations
-------------------------------------
Every Invoiced Invoices will be synchronized with a Exact Quotations.

Once a link between a Invoiced Invoices and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"


Invoiced Lineitem to Exact Quotations
-------------------------------------
Every Invoiced Lineitem will be synchronized with a Exact Quotations.

Once a link between a Invoiced Lineitem and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Exact Quotations Property
     - Exact Data Type


Invoiced Contacts to Exact Addresses
------------------------------------
Every Invoiced Contacts will be synchronized with a Exact Addresses.

Once a link between a Invoiced Contacts and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Exact Addresses Property
     - Exact Data Type
   * - city
     - City
     - "string"


Invoiced Contacts to Exact Contacts
-----------------------------------
Every Invoiced Contacts will be synchronized with a Exact Contacts.

Once a link between a Invoiced Contacts and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Exact Contacts Property
     - Exact Data Type
   * - city
     - City
     - "string"


Invoiced Customers company to Exact Accounts
--------------------------------------------
Every Invoiced Customers company will be synchronized with a Exact Accounts.

Once a link between a Invoiced Customers company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Exact Accounts Property
     - Exact Data Type
   * - name
     - Name
     - "string"


Invoiced Customers person to Exact Addresses
--------------------------------------------
Every Invoiced Customers person will be synchronized with a Exact Addresses.

Once a link between a Invoiced Customers person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Exact Addresses Property
     - Exact Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"


Invoiced Invoices to Exact Salesorders
--------------------------------------
Every Invoiced Invoices will be synchronized with a Exact Salesorders.

Once a link between a Invoiced Invoices and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - discounts
     - Discount
     - "string"


Invoiced Items to Exact Items
-----------------------------
Every Invoiced Items will be synchronized with a Exact Items.

Once a link between a Invoiced Items and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Exact Items Property
     - Exact Data Type


Invoiced Lineitem to Exact Salesorderlines
------------------------------------------
Every Invoiced Lineitem will be synchronized with a Exact Salesorderlines.

Once a link between a Invoiced Lineitem and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Exact Salesorderlines Property
     - Exact Data Type

