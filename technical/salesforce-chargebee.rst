================================
Salesforce to Chargebee Dataflow
================================

Generated: 2024-09-06 00:34:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Chargebee Customer
----------------------------------------
Every Salesforce Contact will be synchronized with a Chargebee Customer.

Once a link between a Salesforce Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Email
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MailingCountry
     - billing_address.country
     - "string"


Salesforce Currencytype to Chargebee Currency
---------------------------------------------
Every Salesforce Currencytype will be synchronized with a Chargebee Currency.

Once a link between a Salesforce Currencytype and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Chargebee Currency Property
     - Chargebee Data Type


Salesforce Customer to Chargebee Customer
-----------------------------------------
Every Salesforce Customer will be synchronized with a Chargebee Customer.

Once a link between a Salesforce Customer and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Chargebee Customer Property
     - Chargebee Data Type


Salesforce Organization to Chargebee Business_entity
----------------------------------------------------
Every Salesforce Organization will be synchronized with a Chargebee Business_entity.

Once a link between a Salesforce Organization and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name	
     - name
     - "string"


Salesforce Product2 to Chargebee Item
-------------------------------------
Every Salesforce Product2 will be synchronized with a Chargebee Item.

Once a link between a Salesforce Product2 and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - Name	
     - name
     - "string"

