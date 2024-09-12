==================================
WooCommerce to Unieconomy Dataflow
==================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Unieconomy Countries
--------------------------------------------
Before any synchronization can take place, a link between a WooCommerce Customer and a Unieconomy Countries must be established.

A WooCommerce Customer will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Unieconomy Countries Property
   * - billing.country
     - CountryCode
   * - shipping.country
     - CountryCode

Once a link between a WooCommerce Customer and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


WooCommerce Order to Unieconomy Countries
-----------------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Unieconomy Countries must be established.

A WooCommerce Order will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Unieconomy Countries Property
   * - billing.country
     - CountryCode
   * - shipping.country
     - CountryCode

Once a link between a WooCommerce Order and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


WooCommerce Order to Unieconomy Currencycodes
---------------------------------------------
Every WooCommerce Order will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the WooCommerce Order will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A WooCommerce Order will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Unieconomy Currencycodes Property
   * - currency
     - Code

Once a link between a WooCommerce Order and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type

