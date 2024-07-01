===========================
Unieconomy to Wave Dataflow
===========================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

