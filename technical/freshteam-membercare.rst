================================
Freshteam to Membercare Dataflow
================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Membercare Companies
--------------------------------------------
Every Freshteam Department will be synchronized with a Membercare Companies.

Once a link between a Freshteam Department and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Freshteam Employee to Membercare Persons
----------------------------------------
Every Freshteam Employee will be synchronized with a Membercare Persons.

Once a link between a Freshteam Employee and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Membercare Persons Property
     - Membercare Data Type
   * - date_of_birth
     - birthDate
     - "string"
   * - employee_id
     - socialSecurityNumber.number (Dependant on having wd:Q36218176 in socialSecurityNumber.iso2Letter)
     - "string"
   * - first_name
     - firstname
     - "string"
   * - last_name
     - lastname
     - "string"
   * - official_email
     - socialSecurityNumber.number (Dependant on having wd:Q28378282 in socialSecurityNumber.iso2Letter)
     - "string"

