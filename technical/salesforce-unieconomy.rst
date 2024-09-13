=================================
Salesforce to Unieconomy Dataflow
=================================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to Unieconomy Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Unieconomy Companies.

Once a link between a Salesforce Organization and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - Name
     - Name
     - "string"
   * - Name	
     - Name
     - "string"

