=================================
Tidsbanken to Unieconomy Dataflow
=================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Unieconomy Companies
----------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Unieconomy Companies must be established.

A Tidsbanken Kunde will merge with a Unieconomy Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Unieconomy Companies Property
   * - Organisasjonsnummer
     - OrganizationNumber

Once a link between a Tidsbanken Kunde and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - Navn
     - Name
     - "string"
   * - Organisasjonsnummer
     - OrganizationNumber
     - "string"


Tidsbanken Avdeling to Unieconomy Departments
---------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Unieconomy Departments.

Once a link between a Tidsbanken Avdeling and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - Navn
     - Name
     - "string"


Tidsbanken Kunde to Unieconomy Customers
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Unieconomy Customers.

If a matching Unieconomy Customers already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching Unieconomy Customers is found, a new Unieconomy Customers will be created.

A Tidsbanken Kunde will merge with a Unieconomy Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Unieconomy Customers Property
   * - Organisasjonsnummer
     - OrgNumber

Once a link between a Tidsbanken Kunde and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - Organisasjonsnummer
     - OrgNumber
     - "string"
   * - Url
     - WebUrl
     - "string"

