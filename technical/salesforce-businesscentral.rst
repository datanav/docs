=======================================
Salesforce to Business Central Dataflow
=======================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Businesscentral Salesorders
-----------------------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a Businesscentral Salesorders must be established.

A new Businesscentral Salesorders will be created from a Salesforce Order if it is connected to a Salesforce Order, Seller, Orderitem, Invoiceline, or Quotelineitem that is synchronized into Businesscentral.

Once a link between a Salesforce Order and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type


Salesforce Product2 to Businesscentral Items
--------------------------------------------
Before any synchronization can take place, a link between a Salesforce Product2 and a Businesscentral Items must be established.

A new Businesscentral Items will be created from a Salesforce Product2 if it is connected to a Salesforce Order, Seller, Orderitem, Invoiceline, or Quotelineitem that is synchronized into Businesscentral.

Once a link between a Salesforce Product2 and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Businesscentral Items Property
     - Businesscentral Data Type


Salesforce Division to Business Central Companies
-------------------------------------------------
Every Salesforce Division will be synchronized with a Business Central Companies.

Once a link between a Salesforce Division and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Business Central Companies Property
     - Business Central Data Type


Salesforce Organization to Business Central Companies
-----------------------------------------------------
Every Salesforce Organization will be synchronized with a Business Central Companies.

Once a link between a Salesforce Organization and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Central Companies Property
     - Business Central Data Type


Salesforce Contact to Business Central Contacts person
------------------------------------------------------
Every Salesforce Contact will be synchronized with a Business Central Contacts person.

Once a link between a Salesforce Contact and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Business Central Contacts person Property
     - Business Central Data Type


Salesforce Customer to Business Central Customers company
---------------------------------------------------------
Every Salesforce Customer will be synchronized with a Business Central Customers company.

Once a link between a Salesforce Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Salesforce Customer to Business Central Customers person
--------------------------------------------------------
Every Salesforce Customer will be synchronized with a Business Central Customers person.

Once a link between a Salesforce Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Business Central Customers person Property
     - Business Central Data Type


Salesforce Invoiceline to Business Central Salesorderlines
----------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Invoiceline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Salesforce Order to Business Central Salesorders
------------------------------------------------
Every Salesforce Order will be synchronized with a Business Central Salesorders.

Once a link between a Salesforce Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Business Central Salesorders Property
     - Business Central Data Type


Salesforce Orderitem to Business Central Salesorderlines
--------------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Orderitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Salesforce Organization to Business Central Customers company
-------------------------------------------------------------
Every Salesforce Organization will be synchronized with a Business Central Customers company.

Once a link between a Salesforce Organization and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Central Customers company Property
     - Business Central Data Type


Salesforce Product2 to Business Central Items
---------------------------------------------
Every Salesforce Product2 will be synchronized with a Business Central Items.

Once a link between a Salesforce Product2 and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Business Central Items Property
     - Business Central Data Type


Salesforce Quotelineitem to Business Central Salesorderlines
------------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Business Central Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Salesforce User to Business Central Employees
---------------------------------------------
Every Salesforce User will be synchronized with a Business Central Employees.

Once a link between a Salesforce User and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Business Central Employees Property
     - Business Central Data Type

