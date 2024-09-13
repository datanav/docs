================================
Freshteam to Salesforce Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Salesforce Division
-------------------------------------------
Every Freshteam Department will be synchronized with a Salesforce Division.

Once a link between a Freshteam Department and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to Salesforce User
-------------------------------------
Every Freshteam Employee will be synchronized with a Salesforce User.

Once a link between a Freshteam Employee and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Salesforce User Property
     - Salesforce Data Type
   * - designation
     - Division
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"
   * - personal_email
     - Email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - MobilePhone
     - "string"

