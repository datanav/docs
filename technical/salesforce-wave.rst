===========================
Salesforce to Wave Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Wave Country
----------------------------------
Every Salesforce Contact will be synchronized with a Wave Country.

Once a link between a Salesforce Contact and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Wave Country Property
     - Wave Data Type


Salesforce Currencytype to Wave Currency
----------------------------------------
Every Salesforce Currencytype will be synchronized with a Wave Currency.

Once a link between a Salesforce Currencytype and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Wave Currency Property
     - Wave Data Type


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


Salesforce Order to Wave Country
--------------------------------
Every Salesforce Order will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Salesforce Order will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Salesforce Order will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Wave Country Property
   * - BillingCountryCode
     - code
   * - ShippingCountryCode
     - code

Once a link between a Salesforce Order and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Wave Country Property
     - Wave Data Type


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


Salesforce Quote to Wave Country
--------------------------------
Every Salesforce Quote will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Salesforce Quote will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Salesforce Quote will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Wave Country Property
   * - BillingCountryCode
     - code
   * - ShippingCountryCode
     - code

Once a link between a Salesforce Quote and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Wave Country Property
     - Wave Data Type


Salesforce User to Wave Country
-------------------------------
Every Salesforce User will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Salesforce User will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Salesforce User will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Wave Country Property
   * - CountryCode
     - code

Once a link between a Salesforce User and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Wave Country Property
     - Wave Data Type

