================================
Tidsbanken to Tripletex Dataflow
================================

Generated: 2024-03-26 14:23:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Tripletex Contact
--------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Tripletex Contact must be established.

A Tidsbanken Ansatt will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Contact Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Contact Property
     - Tripletex Data Type


Tidsbanken Kunde to Tripletex Customer person
---------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into Tripletex.

Once a link between a Tidsbanken Kunde and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Tidsbanken Ansatt to Tripletex Employee
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Tidsbanken Ansatt will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Employee Property
   * - Epost
     - email
   * - Id
     - employeeNumber
   * - Personnummer
     - nationalIdentityNumber

Once a link between a Tidsbanken Ansatt and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Tripletex Employee Property
     - Tripletex Data Type


Tidsbanken Avdeling to Tripletex Department
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Tripletex Department.

Once a link between a Tidsbanken Avdeling and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Tripletex Department Property
     - Tripletex Data Type


Tidsbanken Kunde to Tripletex Customer
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the Tidsbanken Kunde will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

A Tidsbanken Kunde will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer Property
   * - Epost
     - email
   * - Id
     - customerNumber
   * - Organisasjonsnummer
     - organizationNumber

Once a link between a Tidsbanken Kunde and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Tripletex Customer Property
     - Tripletex Data Type


Tidsbanken Prosjekt to Tripletex Project
----------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Tripletex Project.

Once a link between a Tidsbanken Prosjekt and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Tripletex Project Property
     - Tripletex Data Type

