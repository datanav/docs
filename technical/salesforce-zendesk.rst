==============================
Salesforce to Zendesk Dataflow
==============================

Generated: 2024-09-14 00:00:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to Zendesk Organizations
--------------------------------------------
Every Salesforce Division will be synchronized with a Zendesk Organizations.

Once a link between a Salesforce Division and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


Salesforce Organization to Zendesk Organizations
------------------------------------------------
Every Salesforce Organization will be synchronized with a Zendesk Organizations.

Once a link between a Salesforce Organization and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"

