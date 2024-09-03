============================
Membercare to Exact Dataflow
============================

Generated: 2024-09-03 09:11:47

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Exact Accounts
--------------------------------------
Every Membercare Companies will be synchronized with a Exact Accounts.

Once a link between a Membercare Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Exact Accounts Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.id
     - ID
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - Postcode
     - "string"
   * - companyName
     - Name
     - "string"
   * - url
     - Website
     - "string"


Membercare Companycategories to Exact Currencies
------------------------------------------------
Every Membercare Companycategories will be synchronized with a Exact Currencies.

Once a link between a Membercare Companycategories and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companycategories and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Membercare Companycategories Property
     - Exact Currencies Property
     - Exact Data Type


Membercare Countries to Exact Currencies
----------------------------------------
Every Membercare Countries will be synchronized with a Exact Currencies.

Once a link between a Membercare Countries and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Countries and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Membercare Countries Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Membercare Companies to Exact Addresses
---------------------------------------
Every Membercare Companies will be synchronized with a Exact Addresses.

Once a link between a Membercare Companies and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"

