=====================================
Business Central to Invoiced Dataflow
=====================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers (organisation data) to Invoiced Customers (organisation data)
----------------------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Business Central Customers (organisation data) and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type
   * - displayName
     - name
     - "string"


Business Central Customers (human data) to Invoiced Customers (human data)
--------------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Invoiced Customers (human data).

Once a link between a Business Central Customers (human data) and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type


Business Central Customers (organisation data) to Invoiced Customers (organisation data)
----------------------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Business Central Customers (organisation data) and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


Business Central Customers (human data) to Invoiced Customers (human data)
--------------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Invoiced Customers (human data).

Once a link between a Business Central Customers (human data) and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type
   * - addressLine1
     - address1
     - "string"
   * - addressLine2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - displayName
     - name
     - "string"
   * - id
     - id
     - "string"
   * - postalCode
     - postal_code
     - "string"


Business Central Items to Invoiced Items
----------------------------------------
Every Business Central Items will be synchronized with a Invoiced Items.

Once a link between a Business Central Items and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - unit_cost
     - "string"


Business Central Salesorderlines to Invoiced Lineitem
-----------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a Business Central Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - description
     - items.name
     - "string"
   * - discountPercent
     - items.discounts
     - "string"
   * - quantity
     - items.quantity
     - "string"
   * - unitPrice
     - items.amount
     - "string"


Business Central Salesorders to Invoiced Invoices
-------------------------------------------------
Every Business Central Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a Business Central Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer
     - "string"

