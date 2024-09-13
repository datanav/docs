===========================
Asana to CRMOffice Dataflow
===========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to CRMOffice Activities
--------------------------------------
Every Asana Projects will be synchronized with a CRMOffice Activities.

Once a link between a Asana Projects and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - name
     - subject
     - "string"
   * - owner.gid
     - ownerId
     - "string"


Asana Tasks to CRMOffice Activities
-----------------------------------
Every Asana Tasks will be synchronized with a CRMOffice Activities.

Once a link between a Asana Tasks and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - name
     - subject
     - "string"

