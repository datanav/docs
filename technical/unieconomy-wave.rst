===========================
Unieconomy to Wave Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Countries to Wave Country
------------------------------------
Every Unieconomy Countries will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Unieconomy Countries will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Unieconomy Countries will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Wave Country Property
   * - Name
     - name
   * - CountryCode
     - code

Once a link between a Unieconomy Countries and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Countries and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Wave Country Property
     - Wave Data Type


Unieconomy Currencycodes to Wave Currency
-----------------------------------------
Every Unieconomy Currencycodes will be synchronized with a Wave Currency.

If a matching Wave Currency already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching Wave Currency is found, a new Wave Currency will be created.

A Unieconomy Currencycodes will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Wave Currency Property
   * - Code
     - code

Once a link between a Unieconomy Currencycodes and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Wave Currency Property
     - Wave Data Type


Unieconomy Customers to Wave Customer
-------------------------------------
Every Unieconomy Customers will be synchronized with a Wave Customer.

Once a link between a Unieconomy Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Wave Customer Property
     - Wave Data Type
   * - WebUrl
     - website
     - "string"

