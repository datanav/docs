==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-09-02 13:39:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Companies
-------------------------------------
Every Powerofficego Customers will be synchronized with a  Companies.

Once a link between a Powerofficego Customers and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Companies Property
     -  Data Type
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


Powerofficego Contactperson to  Contacts
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contacts.

Once a link between a Powerofficego Contactperson and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contacts Property
     -  Data Type
   * - dateOfBirth
     - birthday
     - "string"


Powerofficego Customers person to  Contacts
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Customers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contacts Property
     -  Data Type
   * - DateOfBirth
     - birthday
     - "string"


Powerofficego Departments to  Companies
---------------------------------------
Every Powerofficego Departments will be synchronized with a  Companies.

Once a link between a Powerofficego Departments and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Companies Property
     -  Data Type
   * - Name
     - company_name
     - "string"


Powerofficego Employees to  Contacts
------------------------------------
Every Powerofficego Employees will be synchronized with a  Contacts.

Once a link between a Powerofficego Employees and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Contacts Property
     -  Data Type
   * - DateOfBirth
     - birthday
     - "string"


Powerofficego Product to  Product
---------------------------------
Every Powerofficego Product will be synchronized with a  Product.

Once a link between a Powerofficego Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Product Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - salesPrice
     - product_price
     - "string"

