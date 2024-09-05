==============================
HubSpot to Salesforce Dataflow
==============================

Generated: 2024-09-05 13:50:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Salesforce Currencytype
------------------------------------------
Every HubSpot Company will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Company and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


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


HubSpot Account to Salesforce Currencytype
------------------------------------------
Every HubSpot Account will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Account and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - accountType
     - IsoCode
     - "string"


HubSpot Deal to Salesforce Currencytype
---------------------------------------
Every HubSpot Deal will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Deal and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - properties.deal_currency_code
     - IsoCode
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

