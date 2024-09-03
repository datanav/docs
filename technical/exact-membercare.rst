============================
Exact to Membercare Dataflow
============================

Generated: 2024-09-03 09:02:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Companies
----------------------------
Every Exact Accounts will be synchronized with a  Companies.

Once a link between a Exact Accounts and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Companies:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Companies Property
     -  Data Type
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


Exact Currencies to  Companycategories
--------------------------------------
Every Exact Currencies will be synchronized with a  Companycategories.

Once a link between a Exact Currencies and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     -  Companycategories Property
     -  Data Type


Exact Departments to  Companies
-------------------------------
Every Exact Departments will be synchronized with a  Companies.

Once a link between a Exact Departments and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a  Companies:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     -  Companies Property
     -  Data Type


Exact Divisions to  Companies
-----------------------------
Every Exact Divisions will be synchronized with a  Companies.

Once a link between a Exact Divisions and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a  Companies:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     -  Companies Property
     -  Data Type
   * - Website
     - url
     - "string"


Exact Units to  Companycategories
---------------------------------
Every Exact Units will be synchronized with a  Companycategories.

Once a link between a Exact Units and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     -  Companycategories Property
     -  Data Type


Exact Vatcodes to  Companycategories
------------------------------------
Every Exact Vatcodes will be synchronized with a  Companycategories.

Once a link between a Exact Vatcodes and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     -  Companycategories Property
     -  Data Type
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

