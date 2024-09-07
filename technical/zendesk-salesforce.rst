==============================
Zendesk to Salesforce Dataflow
==============================

Generated: 2024-09-07 00:36:25

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Salesforce Division
--------------------------------------------
Every Zendesk Organizations will be synchronized with a Salesforce Division.

Once a link between a Zendesk Organizations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"

