===================================
Wave Financial to Youtrack Dataflow
===================================

Generated: 2024-04-09 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Youtrack Users
--------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Youtrack Users must be established.

A Wave Customer person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Wave Customer person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email
     - "string"


Wave Customer to Youtrack Users
-------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Youtrack Users must be established.

A Wave Customer will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Wave Customer and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email
     - "string"


Wave Vendor to Youtrack Users
-----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Youtrack Users must be established.

A Wave Vendor will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Wave Vendor and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email
     - "string"


Wave Customer to Youtrack Groups
--------------------------------
Every Wave Customer will be synchronized with a Youtrack Groups.

Once a link between a Wave Customer and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - name
     - name
     - "string"

