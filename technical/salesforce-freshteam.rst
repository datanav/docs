================================
Salesforce to Freshteam Dataflow
================================

Generated: 2024-09-14 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce User to Freshteam Employee
-------------------------------------
Every Salesforce User will be synchronized with a Freshteam Employee.

Once a link between a Salesforce User and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - Division
     - designation
     - "string"
   * - Email
     - personal_email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MobilePhone
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"

