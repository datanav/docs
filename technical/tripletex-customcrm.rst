======================
Tripletex to  Dataflow
======================

Generated: 2024-09-10 13:18:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Customer
-------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customer.

Once a link between a Tripletex Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customer Property
     -  Data Type
   * - name
     - Name
     - "string"
   * - website
     - Website
     - "string"

