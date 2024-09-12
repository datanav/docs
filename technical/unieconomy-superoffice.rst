==================================
Unieconomy to SuperOffice Dataflow
==================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Currencycodes to SuperOffice Pricelist
-------------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Currencycodes and a SuperOffice Pricelist must be established.

A Unieconomy Currencycodes will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - SuperOffice Pricelist Property
   * - Code
     - Currency

Once a link between a Unieconomy Currencycodes and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type


Unieconomy Companies to SuperOffice Contact
-------------------------------------------
Every Unieconomy Companies will be synchronized with a SuperOffice Contact.

Once a link between a Unieconomy Companies and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


Unieconomy Customers to SuperOffice Contact
-------------------------------------------
Every Unieconomy Customers will be synchronized with a SuperOffice Contact.

Once a link between a Unieconomy Customers and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - WebUrl
     - Urls.Value
     - "string"


Unieconomy Departments to SuperOffice Contact
---------------------------------------------
Every Unieconomy Departments will be synchronized with a SuperOffice Contact.

Once a link between a Unieconomy Departments and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


Unieconomy Countries to SuperOffice Listcountryitems
----------------------------------------------------
Every Unieconomy Countries will be synchronized with a SuperOffice Listcountryitems.

If a matching SuperOffice Listcountryitems already exists, the Unieconomy Countries will be merged with the existing one.
If no matching SuperOffice Listcountryitems is found, a new SuperOffice Listcountryitems will be created.

A Unieconomy Countries will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - SuperOffice Listcountryitems Property
   * - Name
     - Name
   * - CountryCode
     - TwoLetterISOCountry

Once a link between a Unieconomy Countries and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Countries and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Unieconomy Currencycodes to SuperOffice Listcurrencyitems
---------------------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a SuperOffice Listcurrencyitems.

If a matching SuperOffice Listcurrencyitems already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching SuperOffice Listcurrencyitems is found, a new SuperOffice Listcurrencyitems will be created.

A Unieconomy Currencycodes will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - SuperOffice Listcurrencyitems Property
   * - Code
     - Name

Once a link between a Unieconomy Currencycodes and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type

