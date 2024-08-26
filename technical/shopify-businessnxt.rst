====================
Shopify to  Dataflow
====================

Generated: 2024-08-26 15:45:37

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Country
----------------------------
Every Shopify Customer will be synchronized with a  Country.

Once a link between a Shopify Customer and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Country Property
     -  Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to  Currency
-----------------------------
Every Shopify Customer will be synchronized with a  Currency.

Once a link between a Shopify Customer and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Currency Property
     -  Data Type


Shopify Order to  Country
-------------------------
Every Shopify Order will be synchronized with a  Country.

Once a link between a Shopify Order and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Country Property
     -  Data Type
   * - billing_address.country
     - name
     - "string"
   * - billing_address.country_code
     - isoCode
     - "string"
   * - shipping_address.country
     - name
     - "string"
   * - shipping_address.country_code
     - isoCode
     - "string"

