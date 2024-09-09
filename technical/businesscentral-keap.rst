================================
Businesscentral to Keap Dataflow
================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to Keap Companies
-------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Keap Companies must be established.

A new Keap Companies will be created from a Businesscentral Customers if it is connected to a Businesscentral Employees, Contacts-person, or Customers-person that is synchronized into Keap.

Once a link between a Businesscentral Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Keap Companies Property
     - Keap Data Type


Businesscentral Companies to Keap Companies
-------------------------------------------
Every Businesscentral Companies will be synchronized with a Keap Companies.

Once a link between a Businesscentral Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Keap Companies Property
     - Keap Data Type


Businesscentral Contacts person to Keap Contacts
------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Keap Contacts.

Once a link between a Businesscentral Contacts person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Keap Contacts Property
     - Keap Data Type


Businesscentral Customers company to Keap Companies
---------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Keap Companies.

Once a link between a Businesscentral Customers company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
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


Businesscentral Customers person to Keap Contacts
-------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Keap Contacts.

Once a link between a Businesscentral Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Keap Contacts Property
     - Keap Data Type


Businesscentral Employees to Keap Contacts
------------------------------------------
Every Businesscentral Employees will be synchronized with a Keap Contacts.

Once a link between a Businesscentral Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - birthDate
     - birthday
     - "string"


Businesscentral Items to Keap Product
-------------------------------------
Every Businesscentral Items will be synchronized with a Keap Product.

Once a link between a Businesscentral Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Keap Product Property
     - Keap Data Type
   * - displayName
     - product_name
     - "string"
   * - unitPrice
     - product_price
     - "string"

