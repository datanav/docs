=============================
Zendesk to Tripletex Dataflow
=============================

Generated: 2023-06-20 09:25:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Tripletex Contact
----------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Tripletex Contact must be established.

A Zendesk Users will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Zendesk Users and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tripletex Contact Property
     - Tripletex Data Type


Zendesk Users to Tripletex Employee
-----------------------------------
Every Zendesk Users will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Zendesk Users will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Zendesk Users will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tripletex Employee Property
   * - email
     - email

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

