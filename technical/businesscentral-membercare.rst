======================================
Businesscentral to Membercare Dataflow
======================================

Generated: 2024-09-03 09:02:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Companies
---------------------------------------
Every Businesscentral Companies will be synchronized with a  Companies.

Once a link between a Businesscentral Companies and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Companies Property
     -  Data Type


Businesscentral Customers company to Membercare Companies
---------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Membercare Companies.

Once a link between a Businesscentral Customers company and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Membercare Companies Property
     - Membercare Data Type
   * - displayName
     - companyName
     - "string"
   * - displayName
     - name
     - "string"
   * - website
     - url
     - "string"


Businesscentral Salesorders to Membercare Countries
---------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Membercare Countries.

Once a link between a Businesscentral Salesorders and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billToCountry
     - iso2Letter
     - "string"
   * - shipToCountry
     - iso2Letter
     - "string"


Businesscentral Salesquotes to Membercare Countries
---------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Membercare Countries.

Once a link between a Businesscentral Salesquotes and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

