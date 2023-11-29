======================
Tripletex to  Dataflow
======================

Generated: 2023-11-29 23:45:21

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Users
---------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Users must be established.

A Tripletex Contact will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Users Property
   * - email
     - email

Once a link between a Tripletex Contact and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Users Property
     -  Data Type
   * - customer.id
     - organization_id
     - "string"
   * - email
     - email
     - "string"


Tripletex Employee to  Users
----------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a  Users must be established.

A Tripletex Employee will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Users Property
   * - email
     - email

Once a link between a Tripletex Employee and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Users Property
     -  Data Type
   * - department.id
     - organization_id
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumberHome
     - phone
     - "string"


Tripletex Customer to  Organizations
------------------------------------
Every Tripletex Customer will be synchronized with a  Organizations.

Once a link between a Tripletex Customer and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Department to  Organizations
--------------------------------------
Every Tripletex Department will be synchronized with a  Organizations.

Once a link between a Tripletex Department and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"

