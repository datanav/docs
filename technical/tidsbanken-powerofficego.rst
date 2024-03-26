====================================
Tidsbanken to Powerofficego Dataflow
====================================

Generated: 2024-03-26 14:23:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Powerofficego Contactperson
------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Powerofficego Contactperson must be established.

A Tidsbanken Ansatt will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Contactperson Property
   * - Epost
     - emailAddress
   * - Personnummer
     - SocialSecurityNumber

Once a link between a Tidsbanken Ansatt and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


Tidsbanken Ansatt to Powerofficego Employees
--------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Powerofficego Employees must be established.

A Tidsbanken Ansatt will merge with a Powerofficego Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Employees Property
   * - Id
     - Number

Once a link between a Tidsbanken Ansatt and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Powerofficego Employees Property
     - Powerofficego Data Type


Tidsbanken Kunde to Powerofficego Customers
-------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Powerofficego Customers must be established.

A Tidsbanken Kunde will merge with a Powerofficego Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Powerofficego Customers Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Kunde and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Powerofficego Customers Property
     - Powerofficego Data Type

