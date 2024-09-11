================================
Exact Online to ZohoCRM Dataflow
================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to ZohoCRM Account
---------------------------------------
Every ExactOnline Accounts will be synchronized with a ZohoCRM Account.

Once a link between a ExactOnline Accounts and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"
   * - Website
     - Website
     - "string"


ExactOnline Departments to ZohoCRM Account
------------------------------------------
Every ExactOnline Departments will be synchronized with a ZohoCRM Account.

Once a link between a ExactOnline Departments and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Description
     - Created_Time
     - "string"


ExactOnline Divisions to ZohoCRM Account
----------------------------------------
Every ExactOnline Divisions will be synchronized with a ZohoCRM Account.

Once a link between a ExactOnline Divisions and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Description
     - Created_Time
     - "string"
   * - Website
     - Website
     - "string"

