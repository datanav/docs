=============================
Shopify to Crmoffice Dataflow
=============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Crmoffice Contacts
--------------------------------------
Every Shopify Customer will be synchronized with a Crmoffice Contacts.

Once a link between a Shopify Customer and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
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


Shopify Inventoryitem to Crmoffice Companies
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Crmoffice Companies.

Once a link between a Shopify Inventoryitem and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Shopify Product to Crmoffice Companies
--------------------------------------
Every Shopify Product will be synchronized with a Crmoffice Companies.

Once a link between a Shopify Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Shopify Sesamproduct to Crmoffice Companies
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Crmoffice Companies.

Once a link between a Shopify Sesamproduct and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Crmoffice Companies Property
     - Crmoffice Data Type

