=================================
Business Central to Wave Dataflow
=================================

Generated: 2024-09-17 07:28:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to Wave Customer
------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Wave Customer must be established.

A new Wave Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Customers-person, or Customers-company that is synchronized into Wave.

Once a link between a Businesscentral Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Wave Customer Property
     - Wave Data Type


Businesscentral Customers to Wave Customer person
-------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Customers-person, or Customers-company that is synchronized into Wave.

Once a link between a Businesscentral Customers and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Wave Customer person Property
     - Wave Data Type


Business Central Items to Wave Product
--------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Wave Product must be established.

A new Wave Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorders that is synchronized into Wave.

Once a link between a Business Central Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Wave Product Property
     - Wave Data Type
   * - displayName
     - name
     - "string"
   * - unitPrice
     - unitPrice
     - "string"


Business Central Salesorders to Wave Invoice
--------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a Wave Invoice must be established.

A new Wave Invoice will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorders that is synchronized into Wave.

Once a link between a Business Central Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - currencyId
     - currency.code
     - "string"
   * - customerId
     - customer.id
     - "string"


Business Central Customers company to Wave Customer
---------------------------------------------------
Every Business Central Customers company will be synchronized with a Wave Customer.

Once a link between a Business Central Customers company and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Wave Customer Property
     - Wave Data Type
   * - displayName
     - name
     - N/A
   * - phoneNumber
     - phone
     - "string"
   * - website
     - website
     - "string"


Business Central Customers company to Wave Customer person
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Wave Customer person.

Once a link between a Business Central Customers company and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Wave Customer person Property
     - Wave Data Type


Business Central Customers person to Wave Customer
--------------------------------------------------
Every Business Central Customers person will be synchronized with a Wave Customer.

Once a link between a Business Central Customers person and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"


Business Central Customers person to Wave Customer person
---------------------------------------------------------
Every Business Central Customers person will be synchronized with a Wave Customer person.

Once a link between a Business Central Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Wave Customer person Property
     - Wave Data Type


Business Central Items to Wave Product
--------------------------------------
Every Business Central Items will be synchronized with a Wave Product.

Once a link between a Business Central Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Wave Product Property
     - Wave Data Type


Business Central Salesorders to Wave Invoice
--------------------------------------------
Every Business Central Salesorders will be synchronized with a Wave Invoice.

Once a link between a Business Central Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wave Invoice Property
     - Wave Data Type

