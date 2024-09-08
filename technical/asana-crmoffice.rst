===========================
Asana to Crmoffice Dataflow
===========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to Crmoffice Activities
--------------------------------------
Every Asana Projects will be synchronized with a Crmoffice Activities.

Once a link between a Asana Projects and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"
   * - owner.gid
     - ownerId
     - "string"


Asana Tasks to Crmoffice Activities
-----------------------------------
Every Asana Tasks will be synchronized with a Crmoffice Activities.

Once a link between a Asana Tasks and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"

