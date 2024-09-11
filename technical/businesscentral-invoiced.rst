====================================
BusinessCentral to Invoiced Dataflow
====================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Customers company to Invoiced Customers company
---------------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Invoiced Customers company.

Once a link between a BusinessCentral Customers company and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - displayName
     - name
     - "string"


BusinessCentral Customers person to Invoiced Customers person
-------------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Invoiced Customers person.

Once a link between a BusinessCentral Customers person and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Invoiced Customers person Property
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


BusinessCentral Items to Invoiced Items
---------------------------------------
Every BusinessCentral Items will be synchronized with a Invoiced Items.

Once a link between a BusinessCentral Items and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - unit_cost
     - "string"


BusinessCentral Salesorderlines to Invoiced Lineitem
----------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a BusinessCentral Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
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


BusinessCentral Salesorders to Invoiced Invoices
------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a BusinessCentral Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer
     - "string"

