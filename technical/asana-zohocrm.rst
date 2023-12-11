==================
Asana to  Dataflow
==================

Generated: 2023-12-11 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to  Account
-----------------------
Every Asana Teams will be synchronized with a  Account.

Once a link between a Asana Teams and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a  Account:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     -  Account Property
     -  Data Type
   * - description
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to  Account
----------------------------
Every Asana Workspaces will be synchronized with a  Account.

Once a link between a Asana Workspaces and a  Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Account:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Account Property
     -  Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Account_Name
     - "string"

