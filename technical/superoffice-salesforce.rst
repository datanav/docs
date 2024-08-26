==================================
SuperOffice to Salesforce Dataflow
==================================

Generated: 2024-08-26 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Salesforce Organization
----------------------------------------------
Every SuperOffice Contact will be synchronized with a Salesforce Organization.

Once a link between a SuperOffice Contact and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - Name
     - Name	
     - "string"
   * - Phones.Value
     - Phone	
     - "string"


SuperOffice Product to Salesforce Product2
------------------------------------------
Every SuperOffice Product will be synchronized with a Salesforce Product2.

Once a link between a SuperOffice Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - Description
     - Description	
     - "string"
   * - Name
     - Name	
     - "string"
   * - Url
     - DisplayUrl	
     - "string"

