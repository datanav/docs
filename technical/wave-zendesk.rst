========================
Wave to Zendesk Dataflow
========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Zendesk Users
-------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Zendesk Users must be established.

A Wave Customer person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Wave Customer person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - email
     - email
     - "string"
   * - name
     - name
     - "string"


Wave Customer to Zendesk Users
------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Zendesk Users must be established.

A Wave Customer will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Wave Customer and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - id
     - organization_id
     - "string"


Wave Vendor to Zendesk Users
----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Zendesk Users must be established.

A Wave Vendor will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Wave Vendor and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - id
     - organization_id
     - "string"


Wave Customer to Zendesk Organizations
--------------------------------------
Every Wave Customer will be synchronized with a Zendesk Organizations.

Once a link between a Wave Customer and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Wave User to Zendesk Users
--------------------------
Every Wave User will be synchronized with a Zendesk Users.

Once a link between a Wave User and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - defaultEmail
     - email
     - "string"

