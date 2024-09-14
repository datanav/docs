======================
WebCRM to Wix Dataflow
======================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Persons to Wix Contacts
------------------------------
Every WebCRM Persons will be synchronized with a Wix Contacts.

Once a link between a WebCRM Persons and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Wix Contacts Property
     - Wix Data Type
   * - PersonDirectPhone
     - primaryInfo.phone
     - "string"
   * - PersonFirstName
     - info.name.first
     - "string"
   * - PersonLastName
     - info.name.last
     - "string"


WebCRM Products to Wix Products
-------------------------------
Every WebCRM Products will be synchronized with a Wix Products.

Once a link between a WebCRM Products and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Wix Products:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Wix Products Property
     - Wix Data Type
   * - ProductCostPrice
     - costAndProfitData.itemCost
     - N/A
   * - ProductPrice
     - priceData.price
     - N/A

