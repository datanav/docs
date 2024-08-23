=================================
Unieconomy to Salesforce Dataflow
=================================

Generated: 2024-08-23 08:20:28

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Salesforce Organization
-----------------------------------------------
Every Unieconomy Companies will be synchronized with a Salesforce Organization.

Once a link between a Unieconomy Companies and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - Name
     - Name	
     - "string"

