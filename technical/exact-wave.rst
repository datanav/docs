=============================
Exact Online to Wave Dataflow
=============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to Wave Customer
--------------------------------------
Every Exact Online Accounts will be synchronized with a Wave Customer.

Once a link between a Exact Online Accounts and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - Wave Customer Property
     - Wave Data Type
   * - Name
     - name
     - N/A
   * - Website
     - website
     - "string"


Exact Online Addresses to Wave Country
--------------------------------------
Every Exact Online Addresses will be synchronized with a Wave Country.

Once a link between a Exact Online Addresses and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Addresses and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Exact Online Addresses Property
     - Wave Country Property
     - Wave Data Type


Exact Online Currencies to Wave Currency
----------------------------------------
Every Exact Online Currencies will be synchronized with a Wave Currency.

Once a link between a Exact Online Currencies and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Currencies and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Exact Online Currencies Property
     - Wave Currency Property
     - Wave Data Type


Exact Online Items to Wave Product
----------------------------------
Every Exact Online Items will be synchronized with a Wave Product.

Once a link between a Exact Online Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - Wave Product Property
     - Wave Data Type


Exact Online Salesorders to Wave Invoice
----------------------------------------
Every Exact Online Salesorders will be synchronized with a Wave Invoice.

Once a link between a Exact Online Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - Currency
     - currency.code
     - "string"
   * - Description
     - memo
     - "string"

