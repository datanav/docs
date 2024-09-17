=====================================
Tidsbanken to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to PowerOffice GO Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOffice GO Contactperson must be established.

A Tidsbanken Ansatt will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Contactperson Property
   * - Epost
     - emailAddress
   * - Personnummer
     - SocialSecurityNumber

Once a link between a Tidsbanken Ansatt and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - Adresse
     - address1
     - "string"
   * - Etternavn
     - lastName
     - "string"
   * - Fodt
     - dateOfBirth
     - N/A
   * - Fornavn
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
   * - Postnummer
     - zipCode
     - "string"
   * - Poststed
     - city
     - "string"


Tidsbanken Ansatt to PowerOffice GO Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOffice GO Customers person must be established.

A Tidsbanken Ansatt will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Customers person Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Ansatt and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
   * - Adresse
     - MailAddress.AddressLine1
     - "string"
   * - Etternavn
     - LastName
     - "string"
   * - Fodt
     - DateOfBirth
     - N/A
   * - Fornavn
     - FirstName
     - "string"
   * - Id
     - Id
     - "integer"
   * - Postnummer
     - MailAddress.ZipCode
     - "string"
   * - Poststed
     - MailAddress.City
     - "string"


Tidsbanken Ansatt to PowerOffice GO Employees
---------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a PowerOffice GO Employees must be established.

A Tidsbanken Ansatt will merge with a PowerOffice GO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Employees Property
   * - Id
     - Number

Once a link between a Tidsbanken Ansatt and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type


Tidsbanken Avdeling to PowerOffice GO Departments
-------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Avdeling and a PowerOffice GO Departments must be established.

A new PowerOffice GO Departments will be created from a Tidsbanken Avdeling if it is connected to a Tidsbanken Ansatt, or Prosjekt that is synchronized into PowerOffice GO.

A Tidsbanken Avdeling will merge with a PowerOffice GO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOffice GO Departments Property
   * - Id
     - Code

Once a link between a Tidsbanken Avdeling and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type


Tidsbanken Kunde to PowerOffice GO Customers
--------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into PowerOffice GO.

A Tidsbanken Kunde will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice GO Customers Property
   * - Epost
     - EmailAddress

Once a link between a Tidsbanken Kunde and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Tidsbanken Kunde to PowerOffice GO Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a Tidsbanken Kunde if it is connected to a Tidsbanken Prosjekt that is synchronized into PowerOffice GO.

Once a link between a Tidsbanken Kunde and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Tidsbanken Ansatt to PowerOffice GO Employees
---------------------------------------------
Every Tidsbanken Ansatt will be synchronized with a PowerOffice GO Employees.

Once a link between a Tidsbanken Ansatt and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type


Tidsbanken Avdeling to PowerOffice GO Departments
-------------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a PowerOffice GO Departments.

Once a link between a Tidsbanken Avdeling and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type


Tidsbanken Kunde to PowerOffice GO Customers
--------------------------------------------
Every Tidsbanken Kunde will be synchronized with a PowerOffice GO Customers.

Once a link between a Tidsbanken Kunde and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Tidsbanken Kunde to PowerOffice GO Customers person
---------------------------------------------------
Every Tidsbanken Kunde will be synchronized with a PowerOffice GO Customers person.

Once a link between a Tidsbanken Kunde and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


Tidsbanken Prosjekt to PowerOffice GO Projects
----------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a PowerOffice GO Projects.

Once a link between a Tidsbanken Prosjekt and a PowerOffice GO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a PowerOffice GO Projects:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - PowerOffice GO Projects Property
     - PowerOffice GO Data Type

