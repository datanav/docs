=================================
Tidsbanken to Unieconomy Dataflow
=================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to  Companies
------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a  Companies must be established.

A Tidsbanken Kunde will merge with a  Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
   * - Organisasjonsnummer
     - OrganizationNumber

Once a link between a Tidsbanken Kunde and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
     -  Data Type
   * - Navn
     - Name
     - "string"
   * - Organisasjonsnummer
     - OrganizationNumber
     - "string"


Tidsbanken Avdeling to  Departments
-----------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Departments.

Once a link between a Tidsbanken Avdeling and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Departments Property
     -  Data Type
   * - Navn
     - Name
     - "string"


Tidsbanken Kunde to  Customers
------------------------------
Every Tidsbanken Kunde will be synchronized with a  Customers.

If a matching  Customers already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching  Customers is found, a new  Customers will be created.

A Tidsbanken Kunde will merge with a  Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Customers Property
   * - Organisasjonsnummer
     - OrgNumber

Once a link between a Tidsbanken Kunde and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Customers Property
     -  Data Type
   * - Organisasjonsnummer
     - OrgNumber
     - "string"
   * - Url
     - WebUrl
     - "string"

