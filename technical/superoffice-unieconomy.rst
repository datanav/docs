==================================
SuperOffice to Unieconomy Dataflow
==================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Pricelist to Unieconomy Currencycodes
-------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a Unieconomy Currencycodes must be established.

A SuperOffice Pricelist will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Unieconomy Currencycodes Property
   * - Currency
     - Code

Once a link between a SuperOffice Pricelist and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


SuperOffice Listcountryitems to Unieconomy Countries
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the SuperOffice Listcountryitems will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A SuperOffice Listcountryitems will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Unieconomy Countries Property
   * - Name
     - Name
   * - TwoLetterISOCountry
     - CountryCode

Once a link between a SuperOffice Listcountryitems and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


SuperOffice Listcurrencyitems to Unieconomy Currencycodes
---------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the SuperOffice Listcurrencyitems will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A SuperOffice Listcurrencyitems will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Unieconomy Currencycodes Property
   * - Name
     - Code

Once a link between a SuperOffice Listcurrencyitems and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type

