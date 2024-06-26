=================================
Unieconomy to Tidsbanken Dataflow
=================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Tidsbanken Kunde
----------------------------------------
Before any synchronization can take place, a link between a Unieconomy Companies and a Tidsbanken Kunde must be established.

A Unieconomy Companies will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tidsbanken Kunde Property
   * - OrganizationNumber
     - Organisasjonsnummer

Once a link between a Unieconomy Companies and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - Name
     - Navn
     - "string"


Unieconomy Customers to Tidsbanken Kunde
----------------------------------------
Every Unieconomy Customers will be synchronized with a Tidsbanken Kunde.

If a matching Tidsbanken Kunde already exists, the Unieconomy Customers will be merged with the existing one.
If no matching Tidsbanken Kunde is found, a new Tidsbanken Kunde will be created.

A Unieconomy Customers will merge with a Tidsbanken Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tidsbanken Kunde Property
   * - OrgNumber
     - Organisasjonsnummer

Once a link between a Unieconomy Customers and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - WebUrl
     - Url
     - "string"


Unieconomy Departments to Tidsbanken Avdeling
---------------------------------------------
Every Unieconomy Departments will be synchronized with a Tidsbanken Avdeling.

Once a link between a Unieconomy Departments and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type
   * - Name
     - Navn
     - "string"

