=======================
Unieconomy to  Dataflow
=======================

Generated: 2024-08-29 10:58:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Customers to  Accounts
---------------------------------
Every Unieconomy Customers will be synchronized with a  Accounts.

Once a link between a Unieconomy Customers and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     -  Accounts Property
     -  Data Type
   * - CurrencyCodeID
     - Currency
     - "string"

