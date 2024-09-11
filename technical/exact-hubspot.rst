===============================
ExactOnline to HubSpot Dataflow
===============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to HubSpot Company
---------------------------------
Every Exact Accounts will be synchronized with a HubSpot Company.

Once a link between a Exact Accounts and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"
   * - Website
     - properties.website
     - "string"


Exact Contacts to HubSpot Contact
---------------------------------
Every Exact Contacts will be synchronized with a HubSpot Contact.

Once a link between a Exact Contacts and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - BirthDate
     - properties.date_of_birth
     - "string"


Exact Departments to HubSpot Company
------------------------------------
Every Exact Departments will be synchronized with a HubSpot Company.

Once a link between a Exact Departments and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"


Exact Divisions to HubSpot Company
----------------------------------
Every Exact Divisions will be synchronized with a HubSpot Company.

Once a link between a Exact Divisions and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - Website
     - properties.website
     - "string"


Exact Employees to HubSpot Contact
----------------------------------
Every Exact Employees will be synchronized with a HubSpot Contact.

Once a link between a Exact Employees and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - BirthDate
     - properties.date_of_birth
     - "string"
   * - City
     - properties.city
     - "string"
   * - Country
     - properties.country
     - "string"
   * - ID
     - id
     - "string"
   * - Postcode
     - properties.zip
     - "string"


ExactOnline Items to HubSpot Product
------------------------------------
Every ExactOnline Items will be synchronized with a HubSpot Product.

Once a link between a ExactOnline Items and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - HubSpot Product Property
     - HubSpot Data Type


ExactOnline Quotations to HubSpot Quote
---------------------------------------
Every ExactOnline Quotations will be synchronized with a HubSpot Quote.

Once a link between a ExactOnline Quotations and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - HubSpot Quote Property
     - HubSpot Data Type


ExactOnline Salesorderlines to HubSpot Lineitem
-----------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a HubSpot Lineitem.

Once a link between a ExactOnline Salesorderlines and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - HubSpot Lineitem Property
     - HubSpot Data Type

