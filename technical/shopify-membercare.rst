====================
Shopify to  Dataflow
====================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Countries
------------------------------
Every Shopify Customer will be synchronized with a  Countries.

Once a link between a Shopify Customer and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Countries Property
     -  Data Type
   * - currency
     - iso2Letter
     - "string"
   * - default_address.country_code
     - iso2Letter
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to  Countries
---------------------------
Every Shopify Order will be synchronized with a  Countries.

Once a link between a Shopify Order and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Countries Property
     -  Data Type
   * - billing_address.country
     - name
     - "string"
   * - billing_address.country_code
     - iso2Letter
     - "string"
   * - shipping_address.country
     - name
     - "string"
   * - shipping_address.country_code
     - iso2Letter
     - "string"

