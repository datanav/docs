============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-26 15:45:37

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Company
-------------------------------------
Every Businesscentral Companies will be synchronized with a  Company.

Once a link between a Businesscentral Companies and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Company Property
     -  Data Type


Businesscentral Currencies to  Currency
---------------------------------------
Every Businesscentral Currencies will be synchronized with a  Currency.

Once a link between a Businesscentral Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
     -  Data Type


Businesscentral Customers company to  Company
---------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Company.

Once a link between a Businesscentral Customers company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Company Property
     -  Data Type
   * - displayName
     - name
     - "string"


Businesscentral Salesorders to  Country
---------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Country.

Once a link between a Businesscentral Salesorders and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Country Property
     -  Data Type
   * - billToCountry
     - isoCode
     - "string"
   * - shipToCountry
     - isoCode
     - "string"


Businesscentral Salesquotes to  Country
---------------------------------------
Every Businesscentral Salesquotes will be synchronized with a  Country.

Once a link between a Businesscentral Salesquotes and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a  Country:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     -  Country Property
     -  Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

