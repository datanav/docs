======================
Freshteam to  Dataflow
======================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to  Avdeling
---------------------------------
Every Freshteam Department will be synchronized with a  Avdeling.

Once a link between a Freshteam Department and a  Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a  Avdeling:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     -  Avdeling Property
     -  Data Type
   * - name
     - Navn
     - "string"


Freshteam Employee to  Ansatt
-----------------------------
Every Freshteam Employee will be synchronized with a  Ansatt.

If a matching  Ansatt already exists, the Freshteam Employee will be merged with the existing one.
If no matching  Ansatt is found, a new  Ansatt will be created.

A Freshteam Employee will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Ansatt Property
   * - employee_id
     - Id

Once a link between a Freshteam Employee and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Ansatt Property
     -  Data Type
   * - date_of_birth
     - Fodt
     - "string"
   * - designation
     - AvdelingId
     - "string"
   * - designation
     - Tittel
     - "string"
   * - designation
     - sesam_ansattId
     - "integer"
   * - employee_id
     - Id
     - "string"
   * - first_name
     - Fornavn
     - "string"
   * - last_name
     - Etternavn
     - "string"
   * - official_email
     - Epost
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - Mobil
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - TlfPrivat
     - "string"

