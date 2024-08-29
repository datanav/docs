============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-29 08:00:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Customers company
-------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customers company.

Once a link between a Businesscentral Customers company and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customers company Property
     -  Data Type
   * - displayName
     - name
     - "string"


Businesscentral Customers person to  Customers person
-----------------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customers person.

Once a link between a Businesscentral Customers person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customers person Property
     -  Data Type
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


Businesscentral Items to  Items
-------------------------------
Every Businesscentral Items will be synchronized with a  Items.

Once a link between a Businesscentral Items and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Items:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Items Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - unit_cost
     - "string"


Businesscentral Salesorderlines to  Lineitem
--------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Lineitem.

Once a link between a Businesscentral Salesorderlines and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Lineitem Property
     -  Data Type
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


Businesscentral Salesorders to  Invoices
----------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Invoices.

Once a link between a Businesscentral Salesorders and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Invoices Property
     -  Data Type
   * - currencyId
     - currency
     - "string"
   * - customerId
     - customer
     - "string"

