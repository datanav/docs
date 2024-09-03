================================
Chargebee to Salesforce Dataflow
================================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Salesforce Organization
----------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Salesforce Organization.

Once a link between a Chargebee Business_entity and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Chargebee Item to Salesforce Product2
-------------------------------------
Every Chargebee Item will be synchronized with a Salesforce Product2.

Once a link between a Chargebee Item and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Salesforce Product2 Property
     - Salesforce Data Type

