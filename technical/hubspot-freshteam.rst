====================
HubSpot to  Dataflow
====================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Owner to  Employee
--------------------------
Before any synchronization can take place, a link between a HubSpot Owner and a  Employee must be established.

A HubSpot Owner will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     -  Employee Property
   * - email
     - official_email

Once a link between a HubSpot Owner and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Owner and a  Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot Owner Property
     -  Employee Property
     -  Data Type
   * - email
     - official_email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


HubSpot User to  Employee
-------------------------
Before any synchronization can take place, a link between a HubSpot User and a  Employee must be established.

A HubSpot User will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Employee Property
   * - email
     - official_email

Once a link between a HubSpot User and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Employee:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Employee Property
     -  Data Type
   * - email
     - official_email
     - "string"

