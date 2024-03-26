====================
Zendesk to  Dataflow
====================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to  Contact
-------------------------
Before any synchronization can take place, a link between a Zendesk Users and a  Contact must be established.

A Zendesk Users will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contact Property
   * - email
     - email

Once a link between a Zendesk Users and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contact Property
     -  Data Type
   * - email
     - email
     - "string"
   * - organization_id
     - customer.id
     - "integer"


Zendesk Users to  Employee
--------------------------
Before any synchronization can take place, a link between a Zendesk Users and a  Employee must be established.

A Zendesk Users will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Employee Property
   * - email
     - email

Once a link between a Zendesk Users and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Employee Property
     -  Data Type
   * - phone
     - phoneNumberHome
     - "string"

