=================================
Zendesk to Powerofficego Dataflow
=================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Powerofficego Contactperson
--------------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Powerofficego Contactperson must be established.

A Zendesk Users will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Powerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Zendesk Users and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - email
     - emailAddress
     - "string"
   * - organization_id
     - partyId
     - "integer"


Zendesk Users to Powerofficego Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Powerofficego Customers person must be established.

A Zendesk Users will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Powerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a Zendesk Users and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - email
     - EmailAddress
     - "string"
   * - role
     - IsPerson
     - N/A

