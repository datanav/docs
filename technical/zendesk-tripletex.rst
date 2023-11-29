====================
Zendesk to  Dataflow
====================

Generated: 2023-11-29 23:36:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - email
     - email
     - "string"
   * - organization_id
     - customer.id
     - "integer"


Zendesk Organizations to Tripletex Customer
-------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into Tripletex.

Once a link between a Zendesk Organizations and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Zendesk Organizations to Tripletex Department
---------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a Tripletex Department must be established.

A new Tripletex Department will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into Tripletex.

Once a link between a Zendesk Organizations and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Zendesk Users to Tripletex Employee
-----------------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a Tripletex Employee.

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
   * - email
     - email
     - "string"
   * - organization_id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - phone
     - phoneNumberHome
     - "string"

