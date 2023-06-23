=============================
Tripletex to Zendesk Dataflow
=============================

Generated: 2023-06-23 07:31:52

Introduction.
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
   * - phoneNumberHome
     - phone
     - "string"

