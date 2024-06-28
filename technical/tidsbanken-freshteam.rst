================================
Tidsbanken to Freshteam Dataflow
================================

Generated: 2024-06-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Freshteam Employee
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Freshteam Employee.

If a matching Freshteam Employee already exists, the Tidsbanken Ansatt will be merged with the existing one.
If no matching Freshteam Employee is found, a new Freshteam Employee will be created.

A Tidsbanken Ansatt will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Freshteam Employee Property
   * - Id
     - employee_id

Once a link between a Tidsbanken Ansatt and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - Epost
     - official_email
     - "string"
   * - Etternavn
     - last_name
     - "string"
   * - Fodt
     - date_of_birth
     - "string"
   * - Fornavn
     - first_name
     - "string"
   * - Mobil
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - TlfPrivat
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.name)
     - "string"


Tidsbanken Avdeling to Freshteam Department
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Freshteam Department.

Once a link between a Tidsbanken Avdeling and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - Navn
     - name
     - "string"

