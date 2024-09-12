=====================================
Unieconomy to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Currencycodes to PowerOffice GO Currency
---------------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a PowerOffice GO Currency.

If a matching PowerOffice GO Currency already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching PowerOffice GO Currency is found, a new PowerOffice GO Currency will be created.

A Unieconomy Currencycodes will merge with a PowerOffice GO Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - PowerOffice GO Currency Property
   * - Code
     - code

Once a link between a Unieconomy Currencycodes and a PowerOffice GO Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a PowerOffice GO Currency:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - PowerOffice GO Currency Property
     - PowerOffice GO Data Type


Unieconomy Customers to PowerOffice GO Customers
------------------------------------------------
Every Unieconomy Customers will be synchronized with a PowerOffice GO Customers.

Once a link between a Unieconomy Customers and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - WebUrl
     - WebsiteUrl
     - "string"


Unieconomy Departments to PowerOffice GO Departments
----------------------------------------------------
Every Unieconomy Departments will be synchronized with a PowerOffice GO Departments.

Once a link between a Unieconomy Departments and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type
   * - Name
     - Name
     - "string"

