===============================
Invoiced to MemberCare Dataflow
===============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to MemberCare Companies
--------------------------------------------------
Every Invoiced Customers company will be synchronized with a MemberCare Companies.

Once a link between a Invoiced Customers company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"


Invoiced Customers person to MemberCare Persons
-----------------------------------------------
Every Invoiced Customers person will be synchronized with a MemberCare Persons.

Once a link between a Invoiced Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Invoiced Invoices to MemberCare Invoices
----------------------------------------
Every Invoiced Invoices will be synchronized with a MemberCare Invoices.

Once a link between a Invoiced Invoices and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Invoiced Items to MemberCare Products
-------------------------------------
Every Invoiced Items will be synchronized with a MemberCare Products.

Once a link between a Invoiced Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


Invoiced Lineitem to MemberCare Invoices
----------------------------------------
Every Invoiced Lineitem will be synchronized with a MemberCare Invoices.

Once a link between a Invoiced Lineitem and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - items.amount
     - invoiceItems.unitPrice
     - "string"
   * - items.description
     - invoiceItems.description
     - "string"
   * - items.quantity
     - invoiceItems.quantity
     - "string"

