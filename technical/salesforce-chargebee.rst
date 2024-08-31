=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-31 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to  Customer
-------------------------------
Every Salesforce Contact will be synchronized with a  Customer.

Once a link between a Salesforce Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Customer Property
     -  Data Type
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


Salesforce Organization to  Business_entity
-------------------------------------------
Every Salesforce Organization will be synchronized with a  Business_entity.

Once a link between a Salesforce Organization and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Business_entity Property
     -  Data Type
   * - Name	
     - name
     - "string"


Salesforce Product2 to  Item
----------------------------
Every Salesforce Product2 will be synchronized with a  Item.

Once a link between a Salesforce Product2 and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a  Item:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     -  Item Property
     -  Data Type
   * - Name	
     - name
     - "string"

