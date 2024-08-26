======================
Tripletex to  Dataflow
======================

Generated: 2024-08-26 15:51:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Company
------------------------------
Every Tripletex Customer will be synchronized with a  Company.

Once a link between a Tripletex Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Company Property
     -  Data Type
   * - customerNumber
     - companyBusinessNo (Dependant on having wd:Q852835 in countryIsoCode)
     - "string"
   * - name
     - name
     - "string"
   * - organizationNumber
     - companyBusinessNo (Dependant on having NO in countryIsoCode)
     - "string"


Tripletex Department to  Company
--------------------------------
Every Tripletex Department will be synchronized with a  Company.

Once a link between a Tripletex Department and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Company:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Company Property
     -  Data Type
   * - departmentNumber
     - companyBusinessNo (Dependant on having wd:Q2366457 in countryIsoCode)
     - "string"
   * - name
     - name
     - "string"


Tripletex Country to  Country
-----------------------------
Every Tripletex Country will be synchronized with a  Country.

Once a link between a Tripletex Country and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a  Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     -  Country Property
     -  Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to  Currency
-------------------------------
Every Tripletex Currency will be synchronized with a  Currency.

Once a link between a Tripletex Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     -  Currency Property
     -  Data Type
   * - displayName
     - name
     - "string"

