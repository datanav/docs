=========================
Asana to ZohoCRM Dataflow
=========================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to ZohoCRM Account
------------------------------
Every Asana Teams will be synchronized with a ZohoCRM Account.

Once a link between a Asana Teams and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - description
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to ZohoCRM Account
-----------------------------------
Every Asana Workspaces will be synchronized with a ZohoCRM Account.

Once a link between a Asana Workspaces and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Account_Name
     - "string"

