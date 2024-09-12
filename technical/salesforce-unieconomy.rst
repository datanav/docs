=================================
Salesforce to Unieconomy Dataflow
=================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Unieconomy Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a Unieconomy Countries.

Once a link between a Salesforce Contact and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Salesforce Currencytype to Unieconomy Currencycodes
---------------------------------------------------
Every Salesforce Currencytype will be synchronized with a Unieconomy Currencycodes.

Once a link between a Salesforce Currencytype and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


Salesforce Order to Unieconomy Countries
----------------------------------------
Every Salesforce Order will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Salesforce Order will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Salesforce Order will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Unieconomy Countries Property
   * - BillingCountryCode
     - CountryCode
   * - ShippingCountryCode
     - CountryCode

Once a link between a Salesforce Order and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Salesforce Organization to Unieconomy Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Unieconomy Companies.

Once a link between a Salesforce Organization and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - Name
     - Name
     - "string"
   * - Name	
     - Name
     - "string"


Salesforce Quote to Unieconomy Countries
----------------------------------------
Every Salesforce Quote will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Salesforce Quote will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Salesforce Quote will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Unieconomy Countries Property
   * - BillingCountryCode
     - CountryCode
   * - ShippingCountryCode
     - CountryCode

Once a link between a Salesforce Quote and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Salesforce User to Unieconomy Countries
---------------------------------------
Every Salesforce User will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Salesforce User will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Salesforce User will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Unieconomy Countries Property
   * - CountryCode
     - CountryCode

Once a link between a Salesforce User and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

