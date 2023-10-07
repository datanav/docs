=================================
Powerofficego to ZohoCRM Dataflow
=================================

Generated: 2023-10-07 10:21:02

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to ZohoCRM Account
------------------------------------------
Every Powerofficego Customers will be synchronized with a ZohoCRM Account.

Once a link between a Powerofficego Customers and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"
   * - WebsiteUrl
     - Website
     - "string"

