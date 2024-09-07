============================
Exact to Tidsbanken Dataflow
============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Tidsbanken Kunde
----------------------------------
Every Exact Accounts will be synchronized with a Tidsbanken Kunde.

Once a link between a Exact Accounts and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - Name
     - Navn
     - "string"
   * - Website
     - Url
     - "string"


Exact Departments to Tidsbanken Avdeling
----------------------------------------
Every Exact Departments will be synchronized with a Tidsbanken Avdeling.

If a matching Tidsbanken Avdeling already exists, the Exact Departments will be merged with the existing one.
If no matching Tidsbanken Avdeling is found, a new Tidsbanken Avdeling will be created.

A Exact Departments will merge with a Tidsbanken Avdeling if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Tidsbanken Avdeling Property
   * - Code
     - Id

Once a link between a Exact Departments and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type
   * - Code
     - sesam_avdelingId
     - "string"


Exact Employees to Tidsbanken Ansatt
------------------------------------
Every Exact Employees will be synchronized with a Tidsbanken Ansatt.

Once a link between a Exact Employees and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - BirthDate
     - Fodt
     - "string"
   * - City
     - Poststed
     - "string"
   * - ID
     - Id
     - "integer"
   * - Postcode
     - Postnummer
     - "string"

