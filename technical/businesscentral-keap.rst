================================
BusinessCentral to Keap Dataflow
================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Business Companies to Keap Companies
------------------------------------
Every Business Companies will be synchronized with a Keap Companies.

Once a link between a Business Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - Keap Companies Property
     - Keap Data Type


Business Contacts person to Keap Contacts
-----------------------------------------
Every Business Contacts person will be synchronized with a Keap Contacts.

Once a link between a Business Contacts person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - Keap Contacts Property
     - Keap Data Type


Business Customers company to Keap Companies
--------------------------------------------
Every Business Customers company will be synchronized with a Keap Companies.

Once a link between a Business Customers company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
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


Business Customers person to Keap Contacts
------------------------------------------
Every Business Customers person will be synchronized with a Keap Contacts.

Once a link between a Business Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - Keap Contacts Property
     - Keap Data Type


Business Employees to Keap Contacts
-----------------------------------
Every Business Employees will be synchronized with a Keap Contacts.

Once a link between a Business Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - birthDate
     - birthday
     - "string"


BusinessCentral Items to Keap Product
-------------------------------------
Every BusinessCentral Items will be synchronized with a Keap Product.

Once a link between a BusinessCentral Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Keap Product Property
     - Keap Data Type
   * - displayName
     - product_name
     - "string"
   * - unitPrice
     - product_price
     - "string"

