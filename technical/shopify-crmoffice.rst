====================
Shopify to  Dataflow
====================

Generated: 2024-08-23 13:10:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Contacts
-----------------------------
Every Shopify Customer will be synchronized with a  Contacts.

Once a link between a Shopify Customer and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Contacts Property
     -  Data Type
   * - default_address.phone
     - directPhone
     - "string"
   * - first_name
     - givenName
     - "string"
   * - last_name
     - familyName
     - "string"
   * - phone
     - mobilePhone
     - "string"


Shopify Inventoryitem to  Companies
-----------------------------------
Every Shopify Inventoryitem will be synchronized with a  Companies.

Once a link between a Shopify Inventoryitem and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Companies Property
     -  Data Type


Shopify Product to  Companies
-----------------------------
Every Shopify Product will be synchronized with a  Companies.

Once a link between a Shopify Product and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Companies Property
     -  Data Type


Shopify Sesamproduct to  Companies
----------------------------------
Every Shopify Sesamproduct will be synchronized with a  Companies.

Once a link between a Shopify Sesamproduct and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Companies Property
     -  Data Type

