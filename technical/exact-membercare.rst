============================
Exact to Membercare Dataflow
============================

Generated: 2024-09-03 09:11:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Membercare Companies
--------------------------------------
Every Exact Accounts will be synchronized with a Membercare Companies.

Once a link between a Exact Accounts and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Membercare Companies Property
     - Membercare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - ID
     - addresses.id
     - "string"
   * - Name
     - companyName
     - "string"
   * - Postcode
     - addresses.postalCode.zipCode
     - "string"
   * - Website
     - url
     - "string"


Exact Currencies to Membercare Companycategories
------------------------------------------------
Every Exact Currencies will be synchronized with a Membercare Companycategories.

Once a link between a Exact Currencies and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Membercare Companycategories Property
     - Membercare Data Type


Exact Departments to Membercare Companies
-----------------------------------------
Every Exact Departments will be synchronized with a Membercare Companies.

Once a link between a Exact Departments and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Membercare Companies Property
     - Membercare Data Type


Exact Divisions to Membercare Companies
---------------------------------------
Every Exact Divisions will be synchronized with a Membercare Companies.

Once a link between a Exact Divisions and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Website
     - url
     - "string"


Exact Units to Membercare Companycategories
-------------------------------------------
Every Exact Units will be synchronized with a Membercare Companycategories.

Once a link between a Exact Units and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Membercare Companycategories Property
     - Membercare Data Type


Exact Vatcodes to Membercare Companycategories
----------------------------------------------
Every Exact Vatcodes will be synchronized with a Membercare Companycategories.

Once a link between a Exact Vatcodes and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - Description
     - description
     - "string"


Exact Addresses to Membercare Countries
---------------------------------------
Every Exact Addresses will be synchronized with a Membercare Countries.

Once a link between a Exact Addresses and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Membercare Countries Property
     - Membercare Data Type
   * - CountryName
     - name
     - "string"

