=================================
Business Central to Keap Dataflow
=================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Business Central Contacts (human data) to Keap Contacts
-------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a Keap Contacts.

Once a link between a Business Central Contacts (human data) and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - Keap Contacts Property
     - Keap Data Type


Business Central Customers (organisation data) to Keap Companies
----------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Keap Companies.

Once a link between a Business Central Customers (organisation data) and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
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


Business Central Customers (human data) to Keap Contacts
--------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Keap Contacts.

Once a link between a Business Central Customers (human data) and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
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

