=============================
Customcrm to ZohoCRM Dataflow
=============================

Generated: 2024-09-10 15:02:06

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Customcrm to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Customcrm Customer to ZohoCRM Account
-------------------------------------
Every Customcrm Customer will be synchronized with a ZohoCRM Account.

Once a link between a Customcrm Customer and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Customcrm Customer and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Customcrm Customer Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type

