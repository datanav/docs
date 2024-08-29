=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-29 08:03:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Product2 to  Items
-----------------------------
Every Salesforce Product2 will be synchronized with a  Items.

Once a link between a Salesforce Product2 and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a  Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     -  Items Property
     -  Data Type
   * - Description	
     - description
     - "string"
   * - Name	
     - name
     - "string"

