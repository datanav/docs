============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-18 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Employee to  Employee
-------------------------------------
Every Businesscentral Employee will be synchronized with a  Employee.

Once a link between a Businesscentral Employee and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employee and a  Employee:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employee Property
     -  Employee Property
     -  Data Type
   * - birthDate
     - date_of_birth
     - "string"

