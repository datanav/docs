==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-28 10:47:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Customer
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Customer.

Once a link between a Powerofficego Contactperson and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Customer Property
     -  Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Powerofficego Customers to  Business_entity
-------------------------------------------
Every Powerofficego Customers will be synchronized with a  Business_entity.

Once a link between a Powerofficego Customers and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to  Business_entity
---------------------------------------------
Every Powerofficego Departments will be synchronized with a  Business_entity.

Once a link between a Powerofficego Departments and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Employees to  Customer
------------------------------------
Every Powerofficego Employees will be synchronized with a  Customer.

Once a link between a Powerofficego Employees and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Customer Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Powerofficego Customers person to  Customer
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customer.

Once a link between a Powerofficego Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customer Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"

