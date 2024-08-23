==============================
ZohoCRM to Salesforce Dataflow
==============================

Generated: 2024-08-23 09:01:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Salesforce Organization
------------------------------------------
Every ZohoCRM Account will be synchronized with a Salesforce Organization.

Once a link between a ZohoCRM Account and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Salesforce Organization Property
     - Salesforce Data Type

