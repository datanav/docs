=============================
Exact Online to Wave Dataflow
=============================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Wave Customer
-------------------------------------
Every ExactOnline Accounts will be synchronized with a Wave Customer.

Once a link between a ExactOnline Accounts and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Wave Customer Property
     - Wave Data Type
   * - Name
     - name
     - N/A
   * - Website
     - website
     - "string"


ExactOnline Items to Wave Product
---------------------------------
Every ExactOnline Items will be synchronized with a Wave Product.

Once a link between a ExactOnline Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - Wave Product Property
     - Wave Data Type


ExactOnline Salesorders to Wave Invoice
---------------------------------------
Every ExactOnline Salesorders will be synchronized with a Wave Invoice.

Once a link between a ExactOnline Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - Currency
     - currency.code
     - "string"
   * - Description
     - memo
     - "string"

