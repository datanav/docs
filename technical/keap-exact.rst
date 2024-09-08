======================
Keap to Exact Dataflow
======================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Exact Accounts
--------------------------------
Every Keap Companies will be synchronized with a Exact Accounts.

Once a link between a Keap Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Exact Accounts Property
     - Exact Data Type
   * - company_name
     - Name
     - "string"
   * - phone_number.number
     - Phone
     - "string"


Keap Contacts to Exact Contacts
-------------------------------
Every Keap Contacts will be synchronized with a Exact Contacts.

Once a link between a Keap Contacts and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - Exact Contacts Property
     - Exact Data Type
   * - birthday
     - BirthDate
     - "string"
   * - family_name
     - FirstName
     - "string"
   * - family_name
     - FullName
     - "string"
   * - family_name
     - LastName
     - "string"
   * - given_name
     - FirstName
     - "string"
   * - given_name
     - FullName
     - "string"
   * - given_name
     - LastName
     - "string"


Keap Opportunity to Exact Quotations
------------------------------------
Every Keap Opportunity will be synchronized with a Exact Quotations.

Once a link between a Keap Opportunity and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Exact Quotations Property
     - Exact Data Type


Keap Product to Exact Items
---------------------------
Every Keap Product will be synchronized with a Exact Items.

Once a link between a Keap Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Exact Items Property
     - Exact Data Type


Keap Users to Exact Addresses
-----------------------------
Every Keap Users will be synchronized with a Exact Addresses.

Once a link between a Keap Users and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Exact Addresses Property
     - Exact Data Type
   * - address.locality
     - City
     - "string"

