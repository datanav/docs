======================================
Businesscentral to Salesforce Dataflow
======================================

Generated: 2024-08-22 13:53:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to Salesforce Contact
-----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Salesforce Contact.

Once a link between a Businesscentral Contacts person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - city
     - MailingCity
     - "string"

