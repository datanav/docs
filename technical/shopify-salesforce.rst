==============================
Shopify to Salesforce Dataflow
==============================

Generated: 2024-08-23 08:51:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Sesamproduct to Salesforce Product2
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Salesforce Product2.

Once a link between a Shopify Sesamproduct and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - title
     - Name	
     - "string"
   * - variants.title
     - Description	
     - "string"

