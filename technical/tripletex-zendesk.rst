=============================
Tripletex to Zendesk Dataflow
=============================

Generated: 2024-06-29 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Zendesk Users
----------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Zendesk Users must be established.

A Tripletex Contact will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Tripletex Contact and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - customer.id
     - organization_id
     - "string"
   * - email
     - email
     - "string"


Tripletex Customer person to Zendesk Users
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a Zendesk Users must be established.

A Tripletex Customer person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Tripletex Customer person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - email
     - email
     - "string"
   * - isPrivateIndividual
     - role
     - "string"
   * - name
     - name
     - "string"


Tripletex Employee to Zendesk Users
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Zendesk Users must be established.

A Tripletex Employee will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Zendesk Users Property
   * - email
     - email

Once a link between a Tripletex Employee and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - department.id (Dependant on having wd:Q703534 in  )
     - organization_id
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - name
     - "string"
   * - lastName
     - name
     - "string"
   * - phoneNumberHome
     - phone
     - "string"


Tripletex Customer to Zendesk Organizations
-------------------------------------------
Every Tripletex Customer will be synchronized with a Zendesk Organizations.

Once a link between a Tripletex Customer and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Tripletex Department to Zendesk Organizations
---------------------------------------------
Every Tripletex Department will be synchronized with a Zendesk Organizations.

Once a link between a Tripletex Department and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"

