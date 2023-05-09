=============================
Freshteam to HubSpot Dataflow
=============================

Generated: 2023-05-01 16:25:05

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to HubSpot Contact
-------------------------------------
Every Freshteam Employee will be synchronized with a HubSpot Contact.

Once a link between a Freshteam Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - first_name
     - properties.firstname
     - "string"
   * - last_name
     - properties.lastname
     - "string"
   * - official_email
     - properties.work_email
     - "string"


Freshteam Employee to HubSpot User
----------------------------------
Every Freshteam Employee will be synchronized with a HubSpot User.

If a matching HubSpot User already exists, the Freshteam Employee will be merged with the existing one.
If no matching HubSpot User is found, a new HubSpot User will be created.

A Freshteam Employee will merge with a HubSpot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - HubSpot User Property
   * - official_email
     - email

Once a link between a Freshteam Employee and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - HubSpot User Property
     - HubSpot Data Type
   * - official_email
     - email
     - "string"

