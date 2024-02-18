==================
Asana to  Dataflow
==================

Generated: 2024-02-18 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Users to  Employee
------------------------
Every Asana Users will be synchronized with a  Employee.

Once a link between a Asana Users and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Employee:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Employee Property
     -  Data Type
   * - email
     - personal_email
     - "string"
   * - name
     - first_name
     - "string"

