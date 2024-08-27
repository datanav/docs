=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-27 09:25:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to  Country
------------------------------
Every Salesforce Contact will be synchronized with a  Country.

Once a link between a Salesforce Contact and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Country Property
     -  Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Organization to  Address
-----------------------------------
Every Salesforce Organization will be synchronized with a  Address.

Once a link between a Salesforce Organization and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Address Property
     -  Data Type
   * - City
     - postalArea
     - "string"
   * - Country
     - countryNo
     - "string"
   * - Fax	
     - fax
     - "string"
   * - Name	
     - name
     - "string"
   * - Phone	
     - phone
     - "string"
   * - PostalCode	
     - postCode
     - "string"


Salesforce Organization to  Company
-----------------------------------
Every Salesforce Organization will be synchronized with a  Company.

Once a link between a Salesforce Organization and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Company Property
     -  Data Type
   * - Name	
     - name
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
     - description
     - "string"

