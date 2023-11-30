====================
Zendesk to  Dataflow
====================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to  Employee
--------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a  Employee.

Once a link between a Zendesk Users and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Employee Property
     -  Data Type
   * - email
     - personal_email
     - "string"
   * - organization_id
     - designation
     - "string"
   * - phone
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - "string"
   * - updated_at
     - updated_at
     - "string"

