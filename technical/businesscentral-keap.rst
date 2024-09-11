================================
BusinessCentral to Keap Dataflow
================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Customers to Keap Companies
------------------------------------
Before any synchronization can take place, a link between a Business Customers and a Keap Companies must be established.

A new Keap Companies will be created from a Business Customers if it is connected to a Business Businesscentral-employees, Businesscentral-contacts-person, or Businesscentral-customers-person that is synchronized into Keap.

Once a link between a Business Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - Keap Companies Property
     - Keap Data Type


BusinessCentral Companies to Keap Companies
-------------------------------------------
Every BusinessCentral Companies will be synchronized with a Keap Companies.

Once a link between a BusinessCentral Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Companies Property
     - Keap Companies Property
     - Keap Data Type


BusinessCentral Contacts person to Keap Contacts
------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a Keap Contacts.

Once a link between a BusinessCentral Contacts person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Keap Contacts Property
     - Keap Data Type


BusinessCentral Customers company to Keap Companies
---------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Keap Companies.

Once a link between a BusinessCentral Customers company and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
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


BusinessCentral Customers person to Keap Contacts
-------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Keap Contacts.

Once a link between a BusinessCentral Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Keap Contacts Property
     - Keap Data Type


BusinessCentral Employees to Keap Contacts
------------------------------------------
Every BusinessCentral Employees will be synchronized with a Keap Contacts.

Once a link between a BusinessCentral Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
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

