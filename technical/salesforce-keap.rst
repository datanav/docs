===========================
Salesforce to Keap Dataflow
===========================

Generated: 2024-09-04 00:00:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Keap Contacts
-----------------------------------
Every Salesforce Contact will be synchronized with a Keap Contacts.

Once a link between a Salesforce Contact and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Keap Contacts Property
     - Keap Data Type
   * - Birthdate
     - birthday
     - "string"
   * - Name
     - family_name
     - "string"
   * - Name
     - given_name
     - "string"


Salesforce Organization to Keap Companies
-----------------------------------------
Every Salesforce Organization will be synchronized with a Keap Companies.

Once a link between a Salesforce Organization and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Keap Companies Property
     - Keap Data Type
   * - Name	
     - company_name
     - "string"


Salesforce Product2 to Keap Product
-----------------------------------
Every Salesforce Product2 will be synchronized with a Keap Product.

Once a link between a Salesforce Product2 and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Keap Product Property
     - Keap Data Type
   * - Description	
     - product_desc
     - "string"
   * - Name	
     - product_name
     - "string"

