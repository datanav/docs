=================================
Salesforce to Salesforce Dataflow
=================================

Generated: 2024-09-05 13:35:37

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Currencytype to Salesforce Customer
----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Salesforce Customer.

Once a link between a Salesforce Currencytype and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - IsoCode
     - IsoCode
     - "string"


Salesforce Customer to Salesforce Currencytype
----------------------------------------------
Every Salesforce Customer will be synchronized with a Salesforce Currencytype.

Once a link between a Salesforce Customer and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - IsoCode
     - IsoCode
     - "string"

