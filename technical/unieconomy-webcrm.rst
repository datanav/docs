=============================
Unieconomy to Webcrm Dataflow
=============================

Generated: 2024-09-11 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Webcrm Organisations
--------------------------------------------
Every Unieconomy Companies will be synchronized with a Webcrm Organisations.

Once a link between a Unieconomy Companies and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - Name
     - OrganisationName
     - "string"


Unieconomy Customers to Webcrm Organisations
--------------------------------------------
Every Unieconomy Customers will be synchronized with a Webcrm Organisations.

Once a link between a Unieconomy Customers and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Webcrm Organisations Property
     - Webcrm Data Type


Unieconomy Departments to Webcrm Organisations
----------------------------------------------
Every Unieconomy Departments will be synchronized with a Webcrm Organisations.

Once a link between a Unieconomy Departments and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - DepartmentNumber
     - OrganisationCompanyDescription
     - "string"
   * - Name
     - OrganisationName
     - "string"

