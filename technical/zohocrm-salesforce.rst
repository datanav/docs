==============================
ZohoCRM to Salesforce Dataflow
==============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Salesforce Division
--------------------------------------
Every ZohoCRM Account will be synchronized with a Salesforce Division.

Once a link between a ZohoCRM Account and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Account_Name
     - Name
     - "string"


ZohoCRM Deal to Salesforce Invoice
----------------------------------
Every ZohoCRM Deal will be synchronized with a Salesforce Invoice.

Once a link between a ZohoCRM Deal and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Amount
     - TotalAmount
     - "string"


ZohoCRM Contact to Salesforce Customer
--------------------------------------
Every ZohoCRM Contact will be synchronized with a Salesforce Customer.

Once a link between a ZohoCRM Contact and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - Full_Name
     - Name
     - "string"

