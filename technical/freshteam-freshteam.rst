===============================
Freshteam to Freshteam Dataflow
===============================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Freshteam Employee
----------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Freshteam Employee must be established.

A Freshteam Employee will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Freshteam Employee Property
   * - employee_id
     - employee_id
   * - official_email
     - official_email

Once a link between a Freshteam Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - address.city
     - address.city
     - "string"
   * - address.city
     - communication_address.communication_city
     - "string"
   * - address.country
     - communication_address.communication_country
     - "string"
   * - address.country_code
     - address.country_code
     - "string"
   * - address.street
     - address.street
     - "string"
   * - address.street
     - communication_address.communication_street
     - "string"
   * - address.zip_code
     - address.zip_code
     - "string"
   * - address.zip_code
     - communication_address.communication_zip_code
     - "string"
   * - branch_id
     - branch_id
     - "string"
   * - branch_id
     - business_unit_id
     - "string"
   * - branch_id
     - department_id
     - "string"
   * - branch_id
     - hr_incharge_id
     - "string"
   * - branch_id
     - sub_department_id
     - "string"
   * - business_unit_id
     - branch_id
     - "string"
   * - business_unit_id
     - business_unit_id
     - "string"
   * - business_unit_id
     - department_id
     - "string"
   * - business_unit_id
     - hr_incharge_id
     - "string"
   * - business_unit_id
     - sub_department_id
     - "string"
   * - communication_address.communication_city
     - address.city
     - "string"
   * - communication_address.communication_city
     - communication_address.communication_city
     - "string"
   * - communication_address.communication_country
     - address.country
     - "string"
   * - communication_address.communication_country_code
     - communication_address.communication_country_code
     - "string"
   * - communication_address.communication_street
     - address.street
     - "string"
   * - communication_address.communication_street
     - communication_address.communication_street
     - "string"
   * - communication_address.communication_zip_code
     - address.zip_code
     - "string"
   * - communication_address.communication_zip_code
     - communication_address.communication_zip_code
     - "string"
   * - date_of_birth
     - date_of_birth
     - "string"
   * - department_id
     - branch_id
     - "string"
   * - department_id
     - business_unit_id
     - "string"
   * - department_id
     - department_id
     - "string"
   * - department_id
     - hr_incharge_id
     - "string"
   * - department_id
     - sub_department_id
     - "string"
   * - designation
     - designation
     - "string"
   * - first_name
     - first_name
     - "string"
   * - hr_incharge_id
     - branch_id
     - "string"
   * - hr_incharge_id
     - business_unit_id
     - "string"
   * - hr_incharge_id
     - department_id
     - "string"
   * - hr_incharge_id
     - hr_incharge_id
     - "string"
   * - hr_incharge_id
     - sub_department_id
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - last_name
     - "string"
   * - official_email
     - official_email
     - "string"
   * - personal_email
     - personal_email
     - "string"
   * - phone_numbers.number
     - phone_numbers.number (Dependant on having  in phone_numbers.nameDependant on having  in phone_numbers.name)
     - "string"
   * - sub_department_id
     - branch_id
     - "string"
   * - sub_department_id
     - business_unit_id
     - "string"
   * - sub_department_id
     - department_id
     - "string"
   * - sub_department_id
     - hr_incharge_id
     - "string"
   * - sub_department_id
     - sub_department_id
     - "string"
   * - updated_at
     - updated_at
     - "string"

