===============================
Freshteam to Tripletex Dataflow
===============================

Generated: 2023-05-23 06:26:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Tripletex Department
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Tripletex Department must be established.

A new Tripletex Department will be created from a HubSpot Contact if it is connected to a HubSpot User, Superoffice-user, Tripletex-contact, Freshteam-employee, Superoffice-person, Tripletex-employee, Poweroffice-employee, or Tripletex-department that is synchronized into Tripletex.

Once a link between a HubSpot Contact and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


HubSpot Customer to Tripletex Department
----------------------------------------
Before any synchronization can take place, a link between a HubSpot Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a HubSpot Customer if it is connected to a HubSpot User, Superoffice-user, Tripletex-contact, Freshteam-employee, Superoffice-person, Tripletex-employee, Poweroffice-employee, or Tripletex-department that is synchronized into Tripletex.

Once a link between a HubSpot Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - HubSpot Customer Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Freshteam Employee to Tripletex Employee
----------------------------------------
Every Freshteam Employee will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Freshteam Employee will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

A Freshteam Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Employee Property
   * - employee_id
     - employeeNumber

Once a link between a Freshteam Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"

