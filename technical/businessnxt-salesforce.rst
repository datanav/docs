==================================
Businessnxt to Salesforce Dataflow
==================================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Salesforce Organization
----------------------------------------------
Every Businessnxt Address will be synchronized with a Salesforce Organization.

Once a link between a Businessnxt Address and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - countryNo
     - Country
     - "string"
   * - fax
     - Fax	
     - "string"
   * - name
     - Name	
     - "string"
   * - phone
     - Phone	
     - "string"
   * - postCode
     - PostalCode	
     - "string"
   * - postalArea
     - City
     - "string"


Businessnxt Company to Salesforce Organization
----------------------------------------------
Every Businessnxt Company will be synchronized with a Salesforce Organization.

Once a link between a Businessnxt Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Businessnxt Product to Salesforce Product2
------------------------------------------
Every Businessnxt Product will be synchronized with a Salesforce Product2.

Once a link between a Businessnxt Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description	
     - "string"
   * - webPage
     - DisplayUrl	
     - "string"

