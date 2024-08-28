====================
Wix.com to  Dataflow
====================

Generated: 2024-08-28 10:47:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Customer
-----------------------------
Every Wix.com Contacts will be synchronized with a  Customer.

Once a link between a Wix.com Contacts and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customer Property
     -  Data Type
   * - info.name.first
     - first_name
     - "string"
   * - info.name.last
     - last_name
     - "string"
   * - primaryInfo.email
     - email
     - "string"

