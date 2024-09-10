===========================
Exact to Customcrm Dataflow
===========================

Generated: 2024-09-10 14:11:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Customcrm Customer
------------------------------------
Every Exact Accounts will be synchronized with a Customcrm Customer.

Once a link between a Exact Accounts and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - ID
     - Id
     - "string"
   * - Name
     - Name
     - "string"
   * - Postcode
     - ZipCode
     - "string"
   * - Website
     - Website
     - "string"


Exact Contacts to Customcrm Contact
-----------------------------------
Every Exact Contacts will be synchronized with a Customcrm Contact.

Once a link between a Exact Contacts and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Customcrm Contact Property
     - Customcrm Data Type


Exact Contacts to Customcrm Product
-----------------------------------
Every Exact Contacts will be synchronized with a Customcrm Product.

Once a link between a Exact Contacts and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Customcrm Product Property
     - Customcrm Data Type

