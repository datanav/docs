===============================
PowerOffice GO to Keap Dataflow
===============================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Customers to Keap Companies
-----------------------------------------
Every PowerOfficeGO Customers will be synchronized with a Keap Companies.

Once a link between a PowerOfficeGO Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
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


PowerOfficeGO Contactperson to Keap Contacts
--------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a Keap Contacts.

Once a link between a PowerOfficeGO Contactperson and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - Keap Contacts Property
     - Keap Data Type
   * - dateOfBirth
     - birthday
     - "string"


PowerOfficeGO Customers person to Keap Contacts
-----------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a Keap Contacts.

Once a link between a PowerOfficeGO Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


PowerOfficeGO Departments to Keap Companies
-------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a Keap Companies.

Once a link between a PowerOfficeGO Departments and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - Keap Companies Property
     - Keap Data Type
   * - Name
     - company_name
     - "string"


PowerOfficeGO Employees to Keap Contacts
----------------------------------------
Every PowerOfficeGO Employees will be synchronized with a Keap Contacts.

Once a link between a PowerOfficeGO Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


PowerOfficeGO Product to Keap Product
-------------------------------------
Every PowerOfficeGO Product will be synchronized with a Keap Product.

Once a link between a PowerOfficeGO Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
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

