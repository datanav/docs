====================
Zendesk to  Dataflow
====================

Generated: 2023-11-29 23:38:14

Introduction.
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


Zendesk Organizations to  Customer
----------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a  Customer must be established.

A new  Customer will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into .

Once a link between a Zendesk Organizations and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Customer Property
     -  Data Type
   * - name
     - name
     - "string"


Zendesk Organizations to  Department
------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a  Department must be established.

A new  Department will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into .

Once a link between a Zendesk Organizations and a  Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Department:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Department Property
     -  Data Type
   * - name
     - name
     - "string"


Zendesk Users to  Employee
--------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a  Employee.

If a matching  Employee already exists, the Zendesk Users will be merged with the existing one.
If no matching  Employee is found, a new  Employee will be created.

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
   * - email
     - email
     - "string"
   * - organization_id
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - phone
     - phoneNumberHome
     - "string"

