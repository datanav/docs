===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Users
------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Users must be established.

A Wave Customer person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Users Property
   * - email
     - email

Once a link between a Wave Customer person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Users Property
     -  Data Type
   * - name
     - name
     - "string"


Wave Customer to  Users
-----------------------
Before any synchronization can take place, a link between a Wave Customer and a  Users must be established.

A Wave Customer will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Users Property
   * - email
     - email

Once a link between a Wave Customer and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Users Property
     -  Data Type
   * - id
     - organization_id
     - "string"


Wave Vendor to  Users
---------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Users must be established.

A Wave Vendor will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Users Property
   * - email
     - email

Once a link between a Wave Vendor and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Users:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Users Property
     -  Data Type
   * - id
     - organization_id
     - "string"


Wave Customer to  Organizations
-------------------------------
Every Wave Customer will be synchronized with a  Organizations.

Once a link between a Wave Customer and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"

