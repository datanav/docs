==============================
Powerofficego to Keap Dataflow
==============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Keap Companies
-----------------------------------------
Every Powerofficego Customers will be synchronized with a Keap Companies.

Once a link between a Powerofficego Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Keap Companies Property
     - Keap Data Type
   * - Id
     - id
     - "string"
   * - MailAddress.City
     - address.locality
     - "string"
   * - MailAddress.ZipCode
     - address.zip_code
     - "string"
   * - Name
     - company_name
     - "string"


Powerofficego Contactperson to Keap Contacts
--------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Keap Contacts.

Once a link between a Powerofficego Contactperson and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Keap Contacts Property
     - Keap Data Type
   * - dateOfBirth
     - birthday
     - "string"


Powerofficego Customers person to Keap Contacts
-----------------------------------------------
Every Powerofficego Customers person will be synchronized with a Keap Contacts.

Once a link between a Powerofficego Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


Powerofficego Departments to Keap Companies
-------------------------------------------
Every Powerofficego Departments will be synchronized with a Keap Companies.

Once a link between a Powerofficego Departments and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Keap Companies Property
     - Keap Data Type
   * - Name
     - company_name
     - "string"


Powerofficego Employees to Keap Contacts
----------------------------------------
Every Powerofficego Employees will be synchronized with a Keap Contacts.

Once a link between a Powerofficego Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


Powerofficego Product to Keap Product
-------------------------------------
Every Powerofficego Product will be synchronized with a Keap Product.

Once a link between a Powerofficego Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - salesPrice
     - product_price
     - "string"

