==============================
Salesforce to Shopify Dataflow
==============================

Generated: 2024-08-24 00:00:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Product2 to Shopify Sesamproduct
-------------------------------------------
Every Salesforce Product2 will be synchronized with a Shopify Sesamproduct.

Once a link between a Salesforce Product2 and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - Description	
     - variants.title
     - "string"
   * - Name	
     - title
     - "string"

