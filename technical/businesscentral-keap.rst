=================================
Business Central to Keap Dataflow
=================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers to Keap Companies
--------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a Keap Companies must be established.

A new Keap Companies will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-employees, Businesscentral-contacts-person, or Businesscentral-customers-person that is synchronized into Keap.

Once a link between a Business Central Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - Keap Companies Property
     - Keap Data Type


Business Central Companies to Keap Companies
--------------------------------------------
Every Business Central Companies will be synchronized with a Keap Companies.

Once a link between a Business Central Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Keap Companies Property
     - Keap Data Type


Business Central Contacts person to Keap Contacts
-------------------------------------------------
Every Business Central Contacts person will be synchronized with a Keap Contacts.

Once a link between a Business Central Contacts person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Keap Contacts Property
     - Keap Data Type


Business Central Customers company to Keap Companies
----------------------------------------------------
Every Business Central Customers company will be synchronized with a Keap Companies.

Once a link between a Business Central Customers company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Keap Companies Property
     - Keap Data Type
   * - city
     - address.locality
     - "string"
   * - displayName
     - company_name
     - "string"
   * - id
     - id
     - "string"
   * - postalCode
     - address.zip_code
     - "string"


Business Central Customers person to Keap Contacts
--------------------------------------------------
Every Business Central Customers person will be synchronized with a Keap Contacts.

Once a link between a Business Central Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Keap Contacts Property
     - Keap Data Type


Business Central Employees to Keap Contacts
-------------------------------------------
Every Business Central Employees will be synchronized with a Keap Contacts.

Once a link between a Business Central Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - birthDate
     - birthday
     - "string"


Business Central Items to Keap Product
--------------------------------------
Every Business Central Items will be synchronized with a Keap Product.

Once a link between a Business Central Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Keap Product Property
     - Keap Data Type
   * - displayName
     - product_name
     - "string"
   * - unitPrice
     - product_price
     - "string"

