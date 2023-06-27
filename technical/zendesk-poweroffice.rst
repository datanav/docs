===============================
Zendesk to PowerOffice Dataflow
===============================

Generated: 2023-06-27 05:12:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOffice Employee
-------------------------------------
Every Zendesk Users will be synchronized with a PowerOffice Employee.

Once a link between a Zendesk Users and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOffice Employee Property
     - PowerOffice Data Type
   * - updated_at
     - LastChanged
     - "string"

