=======================
Salesforce to  Dataflow
=======================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to  Contacts
-------------------------------
Every Salesforce Contact will be synchronized with a  Contacts.

Once a link between a Salesforce Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Contacts Property
     -  Data Type
   * - Birthdate
     - birthday
     - "string"
   * - Name
     - family_name
     - "string"
   * - Name
     - given_name
     - "string"


Salesforce Organization to  Companies
-------------------------------------
Every Salesforce Organization will be synchronized with a  Companies.

Once a link between a Salesforce Organization and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Companies Property
     -  Data Type
   * - Name	
     - company_name
     - "string"


Salesforce Product2 to  Product
-------------------------------
Every Salesforce Product2 will be synchronized with a  Product.

Once a link between a Salesforce Product2 and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a  Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     -  Product Property
     -  Data Type
   * - Description	
     - product_desc
     - "string"
   * - Name	
     - product_name
     - "string"

