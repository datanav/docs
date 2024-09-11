=============================
Keap to Exact Online Dataflow
=============================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to ExactOnline Accounts
--------------------------------------
Every Keap Companies will be synchronized with a ExactOnline Accounts.

Once a link between a Keap Companies and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - company_name
     - Name
     - "string"
   * - phone_number.number
     - Phone
     - "string"


Keap Contacts to ExactOnline Contacts
-------------------------------------
Every Keap Contacts will be synchronized with a ExactOnline Contacts.

Once a link between a Keap Contacts and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Keap Opportunity to ExactOnline Quotations
------------------------------------------
Every Keap Opportunity will be synchronized with a ExactOnline Quotations.

Once a link between a Keap Opportunity and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


Keap Product to Exact Online Items
----------------------------------
Every Keap Product will be synchronized with a Exact Online Items.

Once a link between a Keap Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Exact Online Items Property
     - Exact Online Data Type


Keap Users to Exact Online Addresses
------------------------------------
Every Keap Users will be synchronized with a Exact Online Addresses.

Once a link between a Keap Users and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - address.locality
     - City
     - "string"

