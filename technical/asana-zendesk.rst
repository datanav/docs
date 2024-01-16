==================
Asana to  Dataflow
==================

Generated: 2024-01-16 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to  Organizations
-----------------------------
Every Asana Teams will be synchronized with a  Organizations.

Once a link between a Asana Teams and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"
   * - permalink_url
     - url
     - "string"


Asana Workspaces to  Organizations
----------------------------------
Every Asana Workspaces will be synchronized with a  Organizations.

Once a link between a Asana Workspaces and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Organizations Property
     -  Data Type
   * - email_domains
     - url
     - "string"
   * - name
     - name
     - "string"

