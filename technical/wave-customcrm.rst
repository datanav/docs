===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-09-10 13:21:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Customer
--------------------------
Every Wave Customer will be synchronized with a  Customer.

Once a link between a Wave Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customer Property
     -  Data Type
   * - fax
     - Fax
     - "string"
   * - internalNotes
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - website
     - Website
     - "string"

