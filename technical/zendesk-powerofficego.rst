==================================
Zendesk to PowerOffice GO Dataflow
==================================

Generated: 2024-10-02 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOffice GO Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOffice GO Contactperson must be established.

A Zendesk Users will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOffice GO Contactperson Property
   * - email
     - emailAddress

Once a link between a Zendesk Users and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - email
     - emailAddress
     - "string"


Zendesk Users to PowerOffice GO Customers
-----------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOffice GO Customers must be established.

A Zendesk Users will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOffice GO Customers Property
   * - email
     - EmailAddress

Once a link between a Zendesk Users and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - email
     - EmailAddress
     - "string"
   * - role
     - IsPerson
     - N/A

