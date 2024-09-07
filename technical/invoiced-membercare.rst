===============================
Invoiced to Membercare Dataflow
===============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Membercare Companies
--------------------------------------------------
Every Invoiced Customers company will be synchronized with a Membercare Companies.

Once a link between a Invoiced Customers company and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Invoiced Customers person to Membercare Persons
-----------------------------------------------
Every Invoiced Customers person will be synchronized with a Membercare Persons.

Once a link between a Invoiced Customers person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Membercare Persons Property
     - Membercare Data Type
   * - city
     - addresses.postalCode.city
     - "string"
   * - country
     - addresses.country.id
     - "string"
   * - id
     - addresses.id
     - "string"
   * - name
     - name
     - "string"
   * - postal_code
     - addresses.postalCode.zipCode
     - "string"


Invoiced Invoices to Membercare Invoices
----------------------------------------
Every Invoiced Invoices will be synchronized with a Membercare Invoices.

Once a link between a Invoiced Invoices and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Membercare Invoices Property
     - Membercare Data Type


Invoiced Items to Membercare Products
-------------------------------------
Every Invoiced Items will be synchronized with a Membercare Products.

Once a link between a Invoiced Items and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"


Invoiced Lineitem to Membercare Invoices
----------------------------------------
Every Invoiced Lineitem will be synchronized with a Membercare Invoices.

Once a link between a Invoiced Lineitem and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - items.amount
     - invoiceItems.unitPrice
     - "string"
   * - items.description
     - invoiceItems.description
     - "string"
   * - items.quantity
     - invoiceItems.quantity
     - "string"

