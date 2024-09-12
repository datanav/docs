===============================
PowerOffice GO to Keap Dataflow
===============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Keap Companies
------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Keap Companies.

Once a link between a PowerOffice GO Customers and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Contactperson to Keap Contacts
---------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Keap Contacts.

Once a link between a PowerOffice GO Contactperson and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Keap Contacts Property
     - Keap Data Type
   * - dateOfBirth
     - birthday
     - "string"


PowerOffice GO Customers person to Keap Contacts
------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Keap Contacts.

Once a link between a PowerOffice GO Customers person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


PowerOffice GO Departments to Keap Companies
--------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Keap Companies.

Once a link between a PowerOffice GO Departments and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Keap Companies Property
     - Keap Data Type
   * - Name
     - company_name
     - "string"


PowerOffice GO Employees to Keap Contacts
-----------------------------------------
Every PowerOffice GO Employees will be synchronized with a Keap Contacts.

Once a link between a PowerOffice GO Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - DateOfBirth
     - birthday
     - "string"


PowerOffice GO Product to Keap Product
--------------------------------------
Every PowerOffice GO Product will be synchronized with a Keap Product.

Once a link between a PowerOffice GO Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
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

