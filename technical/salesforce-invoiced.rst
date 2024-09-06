===============================
Salesforce to Invoiced Dataflow
===============================

Generated: 2024-09-06 06:50:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Invoiced Customers person
------------------------------------------------
Every Salesforce Customer will be synchronized with a Invoiced Customers person.

Once a link between a Salesforce Customer and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Invoiced Customers person Property
     - Invoiced Data Type


Salesforce Product2 to Invoiced Items
-------------------------------------
Every Salesforce Product2 will be synchronized with a Invoiced Items.

Once a link between a Salesforce Product2 and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - Description	
     - description
     - "string"
   * - Name	
     - name
     - "string"

