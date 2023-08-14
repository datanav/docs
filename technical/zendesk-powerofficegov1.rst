===================================
Zendesk to PowerOfficeGov1 Dataflow
===================================

Generated: 2023-08-14 08:48:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOfficeGov1 Employee
-----------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOfficeGov1 Employee must be established.

A Zendesk Users will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Zendesk Users and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type


Zendesk Users to PowerOfficeGov1 Person
---------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOfficeGov1 Person must be established.

A Zendesk Users will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Zendesk Users and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type

