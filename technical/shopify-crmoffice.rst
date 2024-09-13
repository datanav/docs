=============================
Shopify to CRMOffice Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to CRMOffice Contacts
--------------------------------------
Every Shopify Customer will be synchronized with a CRMOffice Contacts.

Once a link between a Shopify Customer and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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


Shopify Inventoryitem to CRMOffice Companies
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a CRMOffice Companies.

Once a link between a Shopify Inventoryitem and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Shopify Product to CRMOffice Companies
--------------------------------------
Every Shopify Product will be synchronized with a CRMOffice Companies.

Once a link between a Shopify Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Shopify Sesamproduct to CRMOffice Companies
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a CRMOffice Companies.

Once a link between a Shopify Sesamproduct and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - CRMOffice Companies Property
     - CRMOffice Data Type

