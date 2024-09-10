================================
Customhrm to Salesforce Dataflow
================================

Generated: 2024-09-10 14:22:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Customhrm to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Customhrm Employee to Salesforce User
-------------------------------------
Every Customhrm Employee will be synchronized with a Salesforce User.

Once a link between a Customhrm Employee and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Customhrm Employee and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Customhrm Employee Property
     - Salesforce User Property
     - Salesforce Data Type

