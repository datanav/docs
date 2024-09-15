==============================
Custom PMS to ZohoCRM Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom PMS to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom PMS Customer to ZohoCRM Account
--------------------------------------
Every Custom PMS Customer will be synchronized with a ZohoCRM Account.

Once a link between a Custom PMS Customer and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom PMS Customer and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Custom PMS Customer Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type

