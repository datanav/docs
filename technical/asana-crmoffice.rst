==================
Asana to  Dataflow
==================

Generated: 2024-08-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to  Activities
-----------------------------
Every Asana Projects will be synchronized with a  Activities.

Once a link between a Asana Projects and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a  Activities:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     -  Activities Property
     -  Data Type
   * - name
     - subject
     - "string"
   * - owner.gid
     - ownerId
     - "string"


Asana Tasks to  Activities
--------------------------
Every Asana Tasks will be synchronized with a  Activities.

Once a link between a Asana Tasks and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a  Activities:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     -  Activities Property
     -  Data Type
   * - name
     - subject
     - "string"

