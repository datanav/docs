=============================
HubSpot to Freshteam Dataflow
=============================

Generated: 2023-06-23 11:20:27

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Owner to Freshteam Employee
-----------------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a Freshteam Employee must be established.

A HubSpot Owner will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - Freshteam Employee Property
   * - email
     - official_email

Once a link between a HubSpot Owner and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - email
     - official_email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


HubSpot User to Freshteam Employee
----------------------------------
Before any synchronization can take place, a link between a HubSpot User and a Freshteam Employee must be established.

A HubSpot User will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Freshteam Employee Property
   * - email
     - official_email

Once a link between a HubSpot User and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - email
     - official_email
     - "string"


HubSpot Contact to Freshteam Employee
-------------------------------------
Every HubSpot Contact will be synchronized with a Freshteam Employee.

Once a link between a HubSpot Contact and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - properties.date_of_birth
     - date_of_birth
     - "string"
   * - properties.firstname
     - first_name
     - "string"
   * - properties.lastname
     - last_name
     - "string"
   * - properties.mobilephone
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - properties.phone
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - "string"
   * - properties.work_email
     - official_email
     - "string"

