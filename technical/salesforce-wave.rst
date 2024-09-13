===========================
Salesforce to Wave Dataflow
===========================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Wave Customer person
-------------------------------------------
Every Salesforce Customer will be synchronized with a Wave Customer person.

Once a link between a Salesforce Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Wave Customer person Property
     - Wave Data Type
   * - Name
     - name
     - N/A


Salesforce Order to Wave Invoice
--------------------------------
Every Salesforce Order will be synchronized with a Wave Invoice.

Once a link between a Salesforce Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - CurrencyIsoCode
     - currency.code
     - "string"
   * - Description
     - memo
     - "string"
   * - Name
     - title
     - "string"


Salesforce Product2 to Wave Product
-----------------------------------
Every Salesforce Product2 will be synchronized with a Wave Product.

Once a link between a Salesforce Product2 and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Description	
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"

