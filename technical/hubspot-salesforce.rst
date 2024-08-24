==============================
HubSpot to Salesforce Dataflow
==============================

Generated: 2024-08-24 00:00:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Salesforce Organization
------------------------------------------
Every HubSpot Company will be synchronized with a Salesforce Organization.

Once a link between a HubSpot Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - properties.name
     - Name	
     - "string"
   * - properties.phone
     - Phone	
     - "string"


HubSpot Product to Salesforce Product2
--------------------------------------
Every HubSpot Product will be synchronized with a Salesforce Product2.

Once a link between a HubSpot Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - properties.description
     - Description	
     - "string"
   * - properties.name
     - Name	
     - "string"

