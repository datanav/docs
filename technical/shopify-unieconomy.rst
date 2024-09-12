==============================
Shopify to Unieconomy Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Unieconomy Countries
----------------------------------------
Every Shopify Customer will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Shopify Customer will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Shopify Customer will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Unieconomy Countries Property
   * - default_address.country_code
     - CountryCode

Once a link between a Shopify Customer and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Shopify Customer to Unieconomy Currencycodes
--------------------------------------------
Every Shopify Customer will be synchronized with a Unieconomy Currencycodes.

Once a link between a Shopify Customer and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


Shopify Order to Unieconomy Countries
-------------------------------------
Every Shopify Order will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Shopify Order will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Shopify Order will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Unieconomy Countries Property
   * - billing_address.country_code
     - CountryCode
   * - shipping_address.country_code
     - CountryCode

Once a link between a Shopify Order and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

