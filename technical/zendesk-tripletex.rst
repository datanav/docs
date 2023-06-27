=============================
Zendesk to Tripletex Dataflow
=============================

Generated: 2023-06-27 11:28:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Tripletex Employee
-----------------------------------
Every Zendesk Users will be synchronized with a Tripletex Employee.

Once a link between a Zendesk Users and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - phone
     - phoneNumberHome
     - "string"

