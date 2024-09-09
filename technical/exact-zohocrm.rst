=========================
Exact to ZohoCRM Dataflow
=========================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to ZohoCRM Account
---------------------------------
Every Exact Accounts will be synchronized with a ZohoCRM Account.

Once a link between a Exact Accounts and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"
   * - Website
     - Website
     - "string"


Exact Departments to ZohoCRM Account
------------------------------------
Every Exact Departments will be synchronized with a ZohoCRM Account.

Once a link between a Exact Departments and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Description
     - Created_Time
     - "string"


Exact Divisions to ZohoCRM Account
----------------------------------
Every Exact Divisions will be synchronized with a ZohoCRM Account.

Once a link between a Exact Divisions and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Description
     - Created_Time
     - "string"
   * - Website
     - Website
     - "string"

