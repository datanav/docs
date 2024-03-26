==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Users
-------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Users must be established.

A Powerofficego Contactperson will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Users Property
   * - emailAddress
     - email

Once a link between a Powerofficego Contactperson and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Users Property
     -  Data Type
   * - emailAddress
     - email
     - "string"
   * - partyId
     - organization_id
     - "string"


Powerofficego Customers person to  Users
----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Users must be established.

A Powerofficego Customers person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Users Property
   * - EmailAddress
     - email

Once a link between a Powerofficego Customers person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Users Property
     -  Data Type


Powerofficego Customers to  Organizations
-----------------------------------------
Every Powerofficego Customers will be synchronized with a  Organizations.

Once a link between a Powerofficego Customers and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to  Organizations
-------------------------------------------
Every Powerofficego Departments will be synchronized with a  Organizations.

Once a link between a Powerofficego Departments and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"

