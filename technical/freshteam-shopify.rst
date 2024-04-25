======================
Freshteam to  Dataflow
======================

Generated: 2024-04-25 18:19:25

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to  Customer
-------------------------------
Every Freshteam Employee will be synchronized with a  Customer.

Once a link between a Freshteam Employee and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Customer:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Customer Property
     -  Data Type
   * - personal_email
     - email
     - "string"

