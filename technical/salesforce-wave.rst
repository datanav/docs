===========================
Salesforce to Wave Dataflow
===========================

Generated: 2024-08-25 00:00:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Product2 to Wave Product
-----------------------------------
Every Salesforce Product2 will be synchronized with a Wave Product.

Once a link between a Salesforce Product2 and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Wave Product Property
     - Wave Data Type
   * - Description	
     - description
     - "string"
   * - Name	
     - name
     - "string"

